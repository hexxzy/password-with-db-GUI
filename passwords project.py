import sqlite3
from tkinter import *
import tkinter.ttk as ttk
import re
def UserID():
    error_window = Toplevel(create_window)
    error_window.title("Error")
    error_window.geometry("250x200")
    error_window["bg"] = "gray"
    succesful = Label(error_window, text="Успешная регистрация")
    succesful_btn = Button(error_window, text="Главное меню", command="", borderwidth=5)                #бесполезная кнопка
    succesful_btn.place(x=20, y=100, width=200, height=25)
    succesful_btn["relief"] = "raised"
    succesful.place(x=20, y=50, width=200, height=25)
    succesful["relief"] = "raised"
    id = id_ent.get()
    password = pass_ent.get()
    cursor.execute("""SELECT userid FROM Passwords WHERE userid=?""", (id,))
    result = cursor.fetchone()
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
    if result:
        err_msg = Label(error_window, text="Такой ID уже существует")
        err_msg.place(x=20, y=50, width=200, height=25)
        error_window["bg"] = "gray"
        err_msg["relief"] = "raised"
        err_msg1 = Label(error_window, text="Пожалуйста придумайте новый")
        err_msg1.place(x=20, y=75, width=200, height=25)
        err_msg1["relief"] = "raised"
    elif re.match(pattern, password) is None:
        error_window["bg"] = "gray"
        pass_err = Label(error_window, text="Ваш пароль слишком слабый")
        pass_err.place(x=20, y=50, width=200, height=25)
        pass_err["relief"] = "raised"
        err_msg1 = Label(error_window, text="Пожалуйста придумайте новый")
        err_msg1.place(x=20, y=75, width=200, height=25)
        err_msg1["relief"] = "raised"
    else:
        cursor.execute("""INSERT INTO Passwords(userid, password)VALUES(?, ?)""", (id, password))
        db.commit()
def Display():
    display_window = Toplevel(window)
    display_window.title("ID's")
    display_window.geometry("400x220")
    display_window["bg"] = "gray"
    select = cursor.execute("SELECT id, userid FROM Passwords")
    record = cursor.fetchall()
    table = ttk.Treeview(display_window, show="headings",)
    heads = ["Номер", "UserID"]
    table["columns"] = heads
    for header in heads:
        table.heading(header, text=header, anchor="center")
        table.column(header, anchor="center")
    for row in record:
        table.insert("", END, values=row)
    table.pack(expand=YES, fill=BOTH)
    table.place(x=0, y=0)
    scroll_pane = ttk.Scrollbar(display_window, command=table.yview())
    table.configure(yscrollcommand=scroll_pane.set)
    scroll_pane.pack(side=RIGHT, fill=Y)

def Change():
    global change_window, id_ent, pass_ent
    change_window = Toplevel(window)
    change_window.title("Change a password")
    change_window.geometry("250x200")
    id_lbl = Label(change_window, text="User ID")
    id_lbl.place(x=25, y=25, width=85, height=25)
    id_lbl["relief"] = "raised"
    pass_lbl = Label(change_window, text="New password ")
    pass_lbl.place(x=25, y=75, width=85, height=25)
    pass_lbl["relief"] = "raised"
    id_ent = Entry(change_window)
    id_ent.place(x=125, y=25, width=100, height=25)
    id_ent["relief"] = "raised"
    change_window["bg"] = "gray"
    pass_ent = Entry(change_window)
    pass_ent.place(x=125, y=75, width=100, height=25)
    pass_ent["relief"] = "raised"
    log_btn = Button(change_window, text="Change password", command=UserID, borderwidth=5)
    log_btn.place(x=75, y=130, width=120, height=25)
    log_btn["relief"] = "raised"
def changePass():
    error_change_window = Toplevel(change_window)
    id = id_ent.get()
    password = pass_ent.get()
    cursor.execute("""SELECT userid FROM Passwords WHERE userid=?""", (id,))
    result = cursor.fetchone()
    if result is None:
        err_msg = Label(error_change_window, text="Такого ID не существует")
        err_msg.place(x=20, y=50, width=200, height=25)
        error_change_window["bg"] = "gray"
        error_change_window["relief"] = "raised"




def Create():
      global id_ent, pass_ent, save_msg, create_window
      create_window = Toplevel(window)
      create_window.title("Login")
      create_window.geometry("250x200")
      id_lbl = Label(create_window, text="User ID")
      id_lbl.place(x=25, y=25, width=75, height=25)
      id_lbl["relief"] = "raised"
      pass_lbl = Label(create_window, text="Password ")
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
window.geometry("250x200")
window["bg"] = "gray"

create_btn = Button(text="Create a new User ID", command=Create,  borderwidth=5)
create_btn.place(x=50, y=25, width=150, height=25)
change_btn = Button(text="Change a password", command=Change,  borderwidth=5)
change_btn.place(x=50, y=75, width=150, height=25)
display_btn = Button(text="Display all User IDs", command=Display,  borderwidth=5)
display_btn.place(x=50, y=125, width=150, height=25)
cursor.execute("DELETE FROM Passwords")
window.mainloop()
db.commit()