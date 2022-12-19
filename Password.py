import sqlite3
from tkinter import *
def UserID():
    cursor.execute("""INSERT INTO Passwords(userid, password)VALUES(?, ?)""", (id_ent, pass_ent))
    cursor.execute("SELECT EXISTS(SELECT * FROM Passwords WHERE userid=?)", [id_ent])
    db.commit()

def Create():
      create_window = Toplevel(window)
      create_window.title("Login")
      create_window.geometry("250x200")
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
    userid integer NOT NULL,
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

