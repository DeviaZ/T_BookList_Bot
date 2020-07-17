import telebot
import config
import request

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    request.check_user(message.from_user.id, message.from_user.first_name)
    bot.send_message(message.from_user.id, """
    Добро пожаловать в личную библиотеку!
    Чтобы узнать список комманд напишите /help
    """)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    request.check_user(message.from_user.id, message.from_user.first_name)
    #mlist = func.m_split(message.text)
    mlist = message.text.partition(' ')
    try:
        if mlist[0] == "/help":
            bot.send_message(message.from_user.id, """
             Здесь можно хранить список книг.
             Список команд:
             /list - выводит список добавленных книг
             /book <Номер книги(в списке)> - Показать все данные о книге
             /add <Название книги>- Добавить книгу в список
             /del <Номер книги(в списке)> - Удалить книгу из списка
             /name <Номер книги(в списке)> <Название книги> - Изменить название книги
             /author <Номер книги(в списке)> <Автор книги> - Изменить/Добавить автора книги
             /url <Номер книги(в списке)> <Ссылка на книгу> - Изменить/Добавить ссылку на книгу
             /page <Номер книги(в списке)> <Страница> - Изменить/Добавить номер страницы книги,на которой остоновился(-лась)
             """)
        elif mlist[0] == "/list":
            st = request.show_list_books(message.from_user.id)
            bot.send_message(message.from_user.id, st)
        elif mlist[0] == "/book":
            if mlist[2].isdigit():
                st = request.show_book(message.from_user.id, mlist[2])
                bot.send_message(message.from_user.id, st)
            else:
                bot.send_message(message.from_user.id, "Неправильный формат! "
                                                       "Введите /help для помощи.")
        elif mlist[0] == "/add" and mlist[2] != '':
            request.add_book(message.from_user.id, mlist[2])
            bot.send_message(message.from_user.id, "Запрос успешно прошел!")
        elif mlist[0] == "/del":
            if mlist[2].isdigit():
                request.delete_book(message.from_user.id, mlist[2])
                bot.send_message(message.from_user.id, "Запрос успешно прошел!")
            else:
                bot.send_message(message.from_user.id, "Неправильный формат! "
                                                       "Введите /help для помощи.")
        else:
            if mlist[2] != '':
                mlist2 = list(mlist[2].partition(' '))
                mlist = list(mlist[:])
                mlist[1] = mlist2[0]
                mlist[2] = mlist2[2]
            if mlist[1].isdigit():
                if mlist[0] == "/name":
                    request.change_name_book(message.from_user.id, mlist[1],
                                             mlist[2])
                    bot.send_message(message.from_user.id,
                                     "Запрос успешно прошел!")
                elif mlist[0] == "/author":
                    request.change_author_book(message.from_user.id, mlist[1],
                                               mlist[2])
                    bot.send_message(message.from_user.id,
                                     "Запрос успешно прошел!")
                elif mlist[0] == "/url":
                    request.change_url_book(message.from_user.id, mlist[1],
                                               mlist[2])
                    bot.send_message(message.from_user.id,
                                     "Запрос успешно прошел!")
                elif mlist[0] == "/page":
                    if mlist[2].isdigit():
                        request.change_page_book(message.from_user.id, mlist[1],
                                             mlist[2])
                        bot.send_message(message.from_user.id,
                                         "Запрос успешно прошел!")
                    else:
                        bot.send_message(message.from_user.id,
                                "Страницы должны быть написаны в виде числа")
                else:
                    bot.send_message(message.from_user.id,
                                     "Такой команды не существует или написано "
                                     "неправильно! Напишите /help, "
                                     "чтобы узнать доступные комманды")
            else:
                bot.send_message(message.from_user.id,
                                 "Такой команды не существует или написано "
                                 "неправильно! Напишите /help, "
                                 "чтобы узнать доступные комманды")
    except Exception as LogicEx:
        print("Logic error ", LogicEx)
bot.polling()
request.db.close()







