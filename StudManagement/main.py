from tkinter import *
from tkinter import ttk
import sqlite3
#sqlite3.connect("student.db")
#print("Database created")

'''c = sqlite3.connect("student.db")
curses = c.cursor()
curses.execute("CREATE TABLE IF NOT EXISTS Student(ID INTEGER, NAME VARCHAR(20), AGE INTEGER, DOB VARCHAR(20), GENDER VARCHAR(20), CITY VARCHAR(20))")
c.commit()
c.close()
print("Table created")'''

class Student:
    def __init__(self,main):
       self.main = main
       self.T_Frame = Frame(self.main, height=50, width=1200, background="red", bd=2)
       self.T_Frame.pack()
       self.Title = Label(self.T_Frame, text = "Student Management System", font="arial 20 bold", width=1200, bg="orange")
       self.Title.pack()



       self.Frame_1 = Frame(self.main, height=580, width=400, bd=2, bg="red")
       self.Frame_1.pack(side=LEFT)
       self.Frame_1.pack_propagate(0)


       Label(self.Frame_1, text="Student Details", background="red", font="arial 12 bold").place(x=20,y=20)

       #label 1
       self.Id = Label(self.Frame_1, text="Id", background="red", font="arial 11 bold")
       self.Id.place(x=40,y=60)
       self.Id_Entry = Entry(self.Frame_1,width=40)
       self.Id_Entry.place(x=130,y=60)

       # label 2
       self.Name = Label(self.Frame_1, text="Name", background="red", font="arial 11 bold")
       self.Name.place(x=40, y=100)
       self.Name_Entry = Entry(self.Frame_1, width=40)
       self.Name_Entry.place(x=130, y=100)

       # label 3
       self.Age = Label(self.Frame_1, text="Age", background="red", font="arial 11 bold")
       self.Age.place(x=40, y=140)
       self.Age_Entry = Entry(self.Frame_1, width=40)
       self.Age_Entry.place(x=130, y=140)

       # label 4
       self.DOB = Label(self.Frame_1, text="DOB", background="red", font="arial 11 bold")
       self.DOB.place(x=40, y=180)
       self.DOB_Entry = Entry(self.Frame_1, width=40)
       self.DOB_Entry.place(x=130, y=180)

       # label 5
       self.Gender = Label(self.Frame_1, text="Gender", background="red", font="arial 11 bold")
       self.Gender.place(x=40, y=220)
       self.Gender_Entry = Entry(self.Frame_1, width=40)
       self.Gender_Entry.place(x=130, y=220)

       # label 6
       self.City = Label(self.Frame_1, text="City", background="red", font="arial 11 bold")
       self.City.place(x=40, y=260)
       self.City_Entry = Entry(self.Frame_1, width=40)
       self.City_Entry.place(x=130, y=260)

    # **************Button Section*****************
       self.Button_Frame = Frame(self.Frame_1, height= 250, width=250, bd=2,relief="groove", background="red")
       self.Button_Frame.place(x=80,y=300)

       self.Add = Button(self.Button_Frame, text="Add", width=25, font="arial 11 bold",  command=self.Add)
       self.Add.pack()
       self.Delete = Button(self.Button_Frame, text="Delete", width=25, font="arial 11 bold", command=self.Delete)
       self.Delete.pack()
       self.Update = Button(self.Button_Frame, text="Update", width=25, font="arial 11 bold", command=self.Update)
       self.Update.pack()
       self.Clear = Button(self.Button_Frame, text="Clear", width=25, font="arial 11 bold", command=self.Clear)
       self.Clear.pack()

       self.Frame_2 = Frame(self.main, height=580, width=800, bd=2, bg="White")
       self.Frame_2.pack(side=RIGHT)


       self.tree = ttk.Treeview(self.Frame_2, columns=("c1","c2","c3","c4","c5","c6"), show="headings", height=25)
       self.tree.pack()

       self.tree.column("#1", anchor=CENTER, width=40)
       self.tree.heading("#1", text="ID")
       self.tree.column("#2", anchor=CENTER, width=100)
       self.tree.heading("#2", text="Name")
       self.tree.column("#3", anchor=CENTER, width=115)
       self.tree.heading("#3", text="DOB")
       self.tree.column("#4", anchor=CENTER, width=110)
       self.tree.heading("#4", text="Age")
       self.tree.column("#5", anchor=CENTER, width=110)
       self.tree.heading("#5", text="Gender")
       self.tree.column("#6", anchor=CENTER)
       self.tree.heading("#6", text="City")


       # self.tree.insert("", index=0, values=(1, "vijay", 18, "12-2-2002", "male", "chennai"))
       # self.tree.pack()

    def Add(self):
      id = self.Id_Entry.get()
      name = self.Name_Entry.get()
      age = self.Age_Entry.get()
      dob = self.Gender_Entry.get()
      gender = self.Gender_Entry.get()
      city = self.City_Entry.get()
      c = sqlite3.connect("student.db")
      curses = c.cursor()
      curses.execute("INSERT INTO Student(ID, NAME, AGE, DOB, GENDER, CITY) VALUES(?,?,?,?,?,?)",(id, name, age, dob, gender, city))
      c.commit()
      c.close()
      print("Value inserted")
      self.tree.insert("", index=0, values=(id, name, age, dob, gender, city))


    def Delete(self):
       item = self.tree.selection()[0]
       selected_item = self.tree.item(item)['values'][0]
       print(selected_item)
       c = sqlite3.connect("student.db")
       curses = c.cursor()
       curses.execute("DELETE FROM Student WHERE ID={}".format(selected_item))
       print("Value Deleted")
       c.commit()
       c.close()
       self.tree.delete(item)


    def Update(self):
       id = self.Id_Entry.get()
       name = self.Name_Entry.get()
       age = self.Age_Entry.get()
       dob = self.Gender_Entry.get()
       gender = self.Gender_Entry.get()
       city = self.City_Entry.get()
       item = self.tree.selection()[0]
       selected_item = self.tree.item(item)['values'][0]
       self.tree.item(item, values=(id, name, age, dob, gender, city))
       c = sqlite3.connect("student.db")
       curses = c.cursor()
       curses.execute("UPDATE Student SET ID=?, NAME=? ,AGE=?, DOB=?, GENDER=?, CITY=? WHERE ID=?",(selected_item, name, age, dob, gender, city, selected_item))
       c.commit()
       c.close()
       print("Values updated")
       self.tree.item(item, values=(id, name, age, dob, gender, city))

    def Clear(self):
       self.Id_Entry.delete(0,END)
       self.Name_Entry.delete(0, END)
       self.Age_Entry.delete(0, END)
       self.DOB_Entry.delete(0, END)
       self.Gender_Entry.delete(0, END)
       self.City_Entry.delete(0, END)


main = Tk()
main.title("STUDENT MANAGEMENT SYSTEM")
main.resizable(False, False)
main.geometry("1200x600")
Student(main)
main.mainloop()