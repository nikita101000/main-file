import tkinter
from tkinter import *
from tkinter import ttk
import sqlite3

root=Tk()
root.title("STUDENT DETAILS")
root.geometry("400x400")
root['bg']='light pink'

#Databases
# create a database or connect to one
conn = sqlite3.connect('student.db')

#create cursor
c = conn. cursor()

#create table
'''
c.execute("""CREATE TABLE STUDENT_DATA(
          roll_no integer,
          student_name text,
          marks integer,
          subject text,
          address text,
          phone_no integer,
          product_id integer
          )""")
'''
def mainpage():
    root.destroy()
    import mainfile
    
# create function to delete a record
def delete():
    # create a database or connect to one
    conn = sqlite3.connect('student.db')

    #create cursor
    c = conn. cursor()

    # delete a record
    c.execute("DELETE from STUDENT_DATA where oid=" + delete_box.get())

    #commit changes
    conn.commit()
    
    #close connection
    conn.close()
    

# create submit function for database
def submit():
    # create a database or connect to one
    conn = sqlite3.connect('student.db')

    #create cursor
    c = conn. cursor()
    # insert into table
    c.execute("INSERT INTO STUDENT_DATA VALUES(:roll_no,:student_name,:marks,:subject,:address,:phone_no,:product_id)",
            {
                 'roll_no': roll_no.get(),
                 'student_name': student_name.get(),
                 'marks': marks.get(),
                 'subject': subject.get(),
                 'address': address.get(),
                 'phone_no': phone_no.get(),
                 'product_id': product_id.get()
            })

    #commit changes
    conn.commit()

    #close connection
    conn.close()

    #clear the text boxes
    roll_no.delete(0, END)
    student_name.delete(0, END)
    marks.delete(0, END)
    subject.delete(0, END)
    address.delete(0, END)
    phone_no.delete(0, END)
    product_id.delete(0, END)

#create query function
def query():
    # create a database or connect to one
    conn = sqlite3.connect('student.db')

    #create cursor
    c = conn. cursor()
    #query the database
    c.execute("SELECT * ,oid FROM STUDENT_DATA")
    records = c.fetchall()
    print(records)

    # query the database
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=18, column=0, columnspan=2)

    #commit changes
    conn.commit()

    #close connection
    conn.close()

def close():
    root.destroy()
    
# create text box
roll_no = Entry(root, width = 30)
roll_no.grid(row=2, column=1, padx=20, pady=(10,0))

student_name = Entry(root, width = 30)
student_name.grid(row=3, column=1, pady=(10,0))

marks = Entry(root, width = 30)
marks.grid(row=4, column=1, pady=(10,0))

subject = Entry(root, width = 30)
subject.grid(row=5, column=1, pady=(10,0))

address = Entry(root, width = 30)
address.grid(row=6, column=1, pady=(10,0))

phone_no = Entry(root, width = 30)
phone_no.grid(row=7, column=1, pady=(10,0))


product_id = Entry(root, width = 30)
product_id.grid(row=8, column=1, pady=(10,0))


delete_box = Entry(root,width=30)
delete_box.grid(row=14, column=1,pady=4)


# create text box labels

roll_no_label = Label(root, text = "Roll No")
roll_no_label.grid(row=2, column=0, pady=(10,0))

student_name_label = Label(root, text = "Student Name")
student_name_label.grid(row=3, column=0, pady=(10,0))

marks_label = Label(root, text = "Marks")
marks_label.grid(row=4, column=0, pady=(10,0))

subject_label = Label(root, text = "Subject")
subject_label.grid(row=5, column=0, pady=(10,0))

address_label = Label(root, text = "Address")
address_label.grid(row=6, column=0, pady=(10,0))

phone_no_label = Label(root, text = "Phone No")
phone_no_label.grid(row=7, column=0, pady=(10,0))

product_id_label = Label(root, text = "Product Id")
product_id_label.grid(row=8, column=0, pady=(10,0))

delete_box_label= Label(root, text="Delete ID")
delete_box_label.grid(row=14,column=0,pady=4)

stud_detail_label=Label(root, text = "STUDENT DETAILS",font=("Times New Roman",20,"bold"), fg="sea green",bg="white")
stud_detail_label.grid(row=0,column=4,pady=4, ipadx=150)


# create submit button
submit_btn = Button(root, text="Add Record To Database",bg = "maroon",fg="white", command= submit)
submit_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=63)

# create a query button
query_btn = Button(root, text="Show Records",bg = "maroon",fg="white", command=query)
query_btn.grid(row=11, column=0, columnspan=2, pady=10, padx= 10, ipadx=90)

#create a delete button
delete_btn = Button(root, text="delete Record",bg = "maroon",fg="white", command=delete)
delete_btn.grid(row=16, column=0, columnspan=2, pady=10, padx= 10, ipadx=91)

# button for closing
exit_btn = Button(root, text="Exit Page",bg = "maroon",fg="white", command=close)
exit_btn.grid(row=16, column=4, columnspan=2,pady=10, padx= 10, ipadx=91)

# button for main page
main_btn = Button(root, text="Main Page",bg = "maroon",fg="white", command=mainpage)
main_btn.grid(row=16, column=6, columnspan=2,pady=10, padx= 10, ipadx=91)

#commit changes
conn.commit()

#close connection
conn.close()

root.mainloop()
