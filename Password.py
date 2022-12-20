import sqlite3
from tkinter import *
import re
def UserID():
    global error_window
    error_window = Toplevel(create_window)
    error_window.title("Ошибка")
    error_window.geometry("250x200")                                                                   #допилить кнопку выхода из меню ошибки
    id = id_ent.get()
    password = pass_ent.get()
    cursor.execute("""SELECT userid FROM Passwords WHERE userid=?""", (id,))
    result = cursor.fetchone()
    if result:
        err_msg = Label(error_window ,text="Такой ID уже существует")
        err_msg.place(x=20, y=50, width=200, height=25)
        error_window["bg"] = "gray"
        err_msg["relief"] = "raised"
        err_msg1 = Label(error_window ,text="Пожалуйста придумайте новый")
        err_msg1.place(x=20, y=75, width=200, height=25)
        err_msg1["relief"] = "raised"
    else:
        if len(password) < 8:
            len_msg = Label(error_window, text="Ваш пароль слишком короткий")
            len_msg.place(error_window, x=20, y=50)
        elif re.search("[0-9]", password) is None:
            digit_msg = Label(error_window, text="В вашем пароль нет цифр")
            digit_msg.place(error_window, x=20, y=30)
        elif re.search("[A-Z]", password) is None:
            upper_msg = Label(text="В вашем пароле нет заглавной буквы")
            upper_msg.place(error_window, x=20, y=70)
        else:
            cursor.execute("""INSERT INTO Passwords(userid, password)VALUES(?, ?)""", (id, password))
    db.commit()

def Create():
      global id_ent, pass_ent, save_msg, create_window
      create_window = Toplevel(window)
      create_window.title("Login")
      create_window.geometry("250x250")
      id_lbl = Label(create_window, text="User ID:")
      id_lbl.place(x=25, y=25, width=75, height=25)
      id_lbl["relief"] = "raised"
      pass_lbl = Label(create_window, text="Password: ")
      pass_lbl.place(x=25, y=75, width=75, height=25)
      pass_lbl["relief"] = "raised"
      id_ent = Entry(create_window)
      id_ent.place(x=125, y=25, width=100, height=25)
      id_ent["relief"] = "raised"
      create_window["bg"] = "gray"
      pass_ent = Entry(create_window)
      pass_ent.place(x=125, y=75, width=100, height=25)
      pass_ent["relief"] = "raised"
      log_btn = Button(create_window, text="Login", command=UserID, borderwidth=5)
      log_btn.place(x = 75, y=130, width=100, height=25)
      log_btn["relief"] = "raised"

with sqlite3.connect("passwords.db") as db:
    cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Passwords(
    id integer PRIMARY KEY,
    userid text NOT NULL,
    password text NOT NULL); """)

window = Tk()
window.title("Menu")
window.geometry("200x200")
window["bg"] = "gray"

create_btn = Button(text="Create a new User ID", command=Create,  borderwidth=5)
create_btn.place(x=50, y=25, width=120, height=25)
change_btn = Button(text="Change a password", command="",  borderwidth=5)
change_btn.place(x=50, y=75, width=120, height=25)
display_btn = Button(text="Display all User IDs", command="",  borderwidth=5)
display_btn.place(x=50, y=125, width=120, height=25)
window.mainloop()
db.commit()

