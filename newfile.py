import tkinter
from tkinter import *
from tkinter import ttk
import sqlite3

root=Tk()
root.title("PRODUCT DETAILS")
root.geometry("400x400")
root['bg']='light pink'

#Databases
# create a database or connect to one
conn = sqlite3.connect('fashion.db')

#create cursor
c = conn. cursor()

#create table
'''
c.execute("""CREATE TABLE FASHION_STORE(
          product_id integer,
          product_name text,
          price integer,
          product_type text,
          product_color text
          )""")
'''

def mainpage():
    root.destroy()
    import mainfile

# create function to delete a record
def delete():
    # create a database or connect to one
    conn = sqlite3.connect('fashion.db')

    #create cursor
    c = conn. cursor()

    # delete a record
    c.execute("DELETE from FASHION_STORE where oid=" + delete_box.get())

    #commit changes
    conn.commit()
    
    #close connection
    conn.close()
    

# create submit function for database
def submit():
    # create a database or connect to one
    conn = sqlite3.connect('fashion.db')

    #create cursor
    c = conn. cursor()
    # insert into table
    c.execute("INSERT INTO FASHION_STORE VALUES(:product_id,:product_name,:price,:product_type,:product_color)",
            {
                 'product_id': product_id.get(),
                 'product_name': product_name.get(),
                 'price': price.get(),
                 'product_type': product_type.get(),
                 'product_color': product_color.get()
            })

    #commit changes
    conn.commit()

    #close connection
    conn.close()

    #clear the text boxes
    product_id.delete(0, END)
    product_name.delete(0, END)
    price.delete(0, END)
    product_type.delete(0, END)
    product_color.delete(0, END)

#create query function
def query():
    # create a database or connect to one
    conn = sqlite3.connect('fashion.db')

    #create cursor
    c = conn. cursor()
    #query the database
    c.execute("SELECT * ,oid FROM FASHION_STORE")
    records = c.fetchall()
    print(records)

    # query the database
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=13, column=0, columnspan=2)

    #commit changes
    conn.commit()

    #close connection
    conn.close()

def close():
    root.destroy()
    
# create text box
product_id = Entry(root, width = 30)
product_id.grid(row=2, column=1, padx=20, pady=(10,0))

product_name = Entry(root, width = 30)
product_name.grid(row=3, column=1, pady=(10,0))

price = Entry(root, width = 30)
price.grid(row=4, column=1, pady=(10,0))

product_type = Entry(root, width = 30)
product_type.grid(row=5, column=1, pady=(10,0))

product_color = Entry(root, width = 30)
product_color.grid(row=6, column=1, pady=(10,0))

delete_box = Entry(root,width=30)
delete_box.grid(row=11, column=1,pady=4)


# create text box labels

product_id_label = Label(root, text = "Product Id")
product_id_label.grid(row=2, column=0, pady=(10,0))

product_name_label = Label(root, text = "Product Name")
product_name_label.grid(row=3, column=0, pady=(10,0))

price_label = Label(root, text = "Price")
price_label.grid(row=4, column=0, pady=(10,0))

product_type_label = Label(root, text = "Product Type")
product_type_label.grid(row=5, column=0, pady=(10,0))

product_color_label = Label(root, text = "Product Color")
product_color_label.grid(row=6, column=0, pady=(10,0))

delete_box_label= Label(root, text="Select ID")
delete_box_label.grid(row=11,column=0,pady=4)

prod_detail_label=Label(root, text = "PRODUCT DETAILS",font=("Times New Roman",20,"bold"), fg="sea green",bg="white")
prod_detail_label.grid(row=0,column=4,pady=4, ipadx=150)


# create submit button
submit_btn = Button(root, text="Add Record To Database",bg = "maroon",fg="white", command= submit)
submit_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=63)

# create a query button
query_btn = Button(root, text="Show Records",bg = "maroon",fg="white", command=query)
query_btn.grid(row=8, column=0, columnspan=2, pady=10, padx= 10, ipadx=90)

#create a delete button
delete_btn = Button(root, text="delete Record",bg = "maroon",fg="white", command=delete)
delete_btn.grid(row=12, column=0, columnspan=2, pady=10, padx= 10, ipadx=91)

# button for closing
exit_btn = Button(root, text="Exit Page",bg = "maroon",fg="white", command=close)
exit_btn.grid(row=12, column=3, columnspan=2,pady=10, padx= 10, ipadx=91)

# button for main page
main_btn = Button(root, text="Main Page",bg = "maroon",fg="white", command=mainpage)
main_btn.grid(row=12, column=6, columnspan=2,pady=10, padx= 10, ipadx=91)

#commit changes
conn.commit()

#close connection
conn.close()

root.mainloop()
