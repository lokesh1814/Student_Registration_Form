from tkinter import *
import tkinter.messagebox as tmsg
from ttkthemes import themed_tk as tk
import mysql.connector as mysql


root = tk.ThemedTk()
root.get_themes()
root.set_theme("yaru")
root.geometry("600x300")
root.title("Student Registration Form")

def submit_data():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if(id=="" or name=="" or phone==""):
        tmsg.showinfo("Submit Status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="Student Registration") #For connecting with mysql database
        cursor = con.cursor() #for executing any query
        cursor.execute("insert into student values('"+ id +"', '"+ name +"', '"+ phone +"')")
        cursor.execute("commit");

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        show()
        tmsg.showinfo("Submit Status", "Data Inserted Successfully")
        con.close();

def update_data():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if (id == "" or name == "" or phone == ""):
        tmsg.showinfo("Update Status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="",
                            database="Student Registration")  # For connecting with mysql database
        cursor = con.cursor()  # for executing any query
        cursor.execute("update student set name='"+ name +"', phone='"+ phone +"' where id='"+ id +"'")
        cursor.execute("commit");

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        show()
        tmsg.showinfo("Update Status", "Data Updated Successfully")
        con.close();

def delete_data():
    if (e_id.get() == ""):
        tmsg.showinfo("Delete Status", "Id is compulsory for delete")
    else:
        con = mysql.connect(host="localhost", user="root", password="",
                            database="Student Registration")  # For connecting with mysql database
        cursor = con.cursor()  # for executing any query
        cursor.execute("delete from student where id = ('"+ e_id.get() +"')")
        cursor.execute("commit");

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        show()
        tmsg.showinfo("Delete Status", "Data Deleted Successfully")
        con.close();

def fetch_data():
    if (e_id.get() == ""):
        tmsg.showinfo("Fetch Status", "Id is compulsory for fetch")
    else:
        con = mysql.connect(host="localhost", user="root", password="",
                            database="Student Registration")  # For connecting with mysql database
        cursor = con.cursor()  # for executing any query
        cursor.execute("select * from student where id = ('" + e_id.get() + "')")
        rows = cursor.fetchall()

        for row in rows:
            e_name.insert(0, row[1])
            e_phone.insert(0, row[2])

        tmsg.showinfo("Fetch Status", "Data fetched Successfully")
        con.close();


def show():
    con = mysql.connect(host="localhost", user="root", password="",
                        database="Student Registration")  # For connecting with mysql database
    cursor = con.cursor()  # for executing any query
    cursor.execute("select * from student")
    rows = cursor.fetchall()
    list.delete(0, list.size())
    for row in rows:
        insertData = str(row[0])+ '           '+ row[1]
        list.insert(list.size()+1, insertData)

    con.close();


id = Label(root, text="Enter ID", font=("bold",10))
id.place(x=20, y=30)

name = Label(root, text="Enter Name", font=("bold",10))
name.place(x=20, y=60)

phone = Label(root, text="Enter Phone Number", font=("bold",10))
phone.place(x=20, y=90)

e_id = Entry()
e_id.place(x=150, y=30)

e_name = Entry()
e_name.place(x=150, y=60)

e_phone = Entry()
e_phone.place(x=150, y=90)

submit = Button(root, text="Submit", font=("italic", 10), relief=SUNKEN, bg="white", command=submit_data)
submit.place(x=40, y = 140)

update = Button(root, text="update", font=("italic", 10), relief=SUNKEN, bg="white", command=update_data)
update.place(x=120, y = 140)

delete = Button(root, text="delete", font=("italic", 10), relief=SUNKEN, bg="white", command=delete_data)
delete.place(x=200, y = 140)

fetch = Button(root, text="Fetch", font=("italic", 10), relief=SUNKEN, bg="white", command=fetch_data)
fetch.place(x=280, y = 140)

list = Listbox(root)
list.place(x=400, y=30)
show()

root.mainloop()
