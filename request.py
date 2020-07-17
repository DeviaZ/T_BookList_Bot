# Здесь запросы связанные с SQL

import sqlite3 as sql

db = sql.connect("books.db", check_same_thread=False)

# def create_books():
#     cur = db.cursor()
#     cur.executescript("""
#     """)
#     cur.close()

def check_user(id, username):
    try:
        cur = db.cursor()

        cur.execute("\
        SELECT count(id_user) FROM Users\
        where id_user ={}\
        ".format(id))

        if cur.fetchone()[0] == 0:
            cur.execute("\
            INSERT INTO Users (id_user, username)\
            VALUES (?, ?)\
            ", (id, username))
        else:
            pass
    except Exception as checkEx:
        print("Check user error", checkEx)
    finally:
        db.commit()
        cur.close()


# Добавление информации о книгах
def change_url_book(id_user, n_book, url):
    try:
        cur = db.cursor()
        cur.execute("\
            UPDATE Books set url = ?\
            where id_user =? and n_book =?", (url, id_user, n_book))
    except Exception as change_url_bookEX:
        print("change_url_book error: ", change_url_bookEX)
    finally:
        db.commit()
        cur.close()

def change_author_book(id_user, n_book, author):
    try:
        cur = db.cursor()
        cur.execute("\
            UPDATE Books set author = ?\
            where id_user =? and n_book =?", (author, id_user, n_book))
    except Exception as change_author_bookEx:
        print("change_author_book error: ", change_author_bookEx)
    finally:
        cur.close()

def change_name_book(id_user, n_book, book_name):
    try:
        cur = db.cursor()
        cur.execute("\
            UPDATE Books set book_name = ?\
            where id_user =? and n_book =?", (book_name, id_user, n_book))
    except Exception as change_name_bookEx:
        print("change_name_book error: ", change_name_bookEx)
    finally:
        db.commit()
        cur.close()


def change_page_book(id_user, n_book, page):
    try:
        cur = db.cursor()
        cur.execute("\
            UPDATE Books set count_page = ?\
            where id_user =? and n_book =?", (page, id_user, n_book))
    except Exception as change_page_bookEX:
        print("change_page_book error: ", change_page_bookEX)
    finally:
        db.commit()
        cur.close()

# Добавление и удаление книги
def add_book(id_user, name):
    try:
        cur = db.cursor()
        cur.execute("\
                SELECT MAX(n_book) FROM Books\
                where id_user ={}".format(id_user))
        n_book = cur.fetchone()[0]
        if n_book is None:
            n_book = 1
        else:
            n_book += 1
        cur.execute(("\
        INSERT INTO Books (n_book, id_user, book_name)\
        VALUES(?, ?, ?)"), (n_book, id_user, name))
    except Exception as add_bookEX:
        print("Add book error: ", add_bookEX)
    finally:
        db.commit()
        cur.close()


def delete_book(id_user, n_book):
    try:
        cur = db.cursor()
        cur.execute(("DELETE FROM Books\
        WHERE n_book= ? and id_user = ?"), (n_book, id_user))
    except Exception as delete_bookEx:
        print("Delete book error: ", delete_bookEx)
    finally:
        db.commit()
        cur.close()


# Вывод информации о книгах
def show_list_books(id_user):
    try:
        cur = db.cursor()
        cur.execute("\
                SELECT n_book,book_name,count_page FROM Books\
                where id_user ={} order by n_book".format(id_user))
        st = ''
        res = cur.fetchone()
        while not (res is None):
            st += str(res[0]) + ") " + str(res[1]) + " стр-" + \
                  str(res[2]) + '\n'
            res = cur.fetchone()

        return st
    except Exception as show_list_booksEX:
        print("Show_list_book error: ", show_list_booksEX)
    finally:
        cur.close()


def show_book(id_user, n_book):
    try:
        cur = db.cursor()
        cur.execute("\
        SELECT n_book,book_name,author,url,count_page FROM Books\
        where n_book = ? and id_user = ? order by n_book", (n_book, id_user))
        st = ''
        res = cur.fetchone()
        st += "Название книги- " + \
              str(res[1]) + "\nАвтор-" + str(res[2]) + "\nUrl- " + \
              str(res[3]) + "\nстр-" + str(res[4]) + '\n'

        return st
    except Exception as show_booksEx:
        print("Show book error:", show_booksEx)
    finally:
        cur.close()



