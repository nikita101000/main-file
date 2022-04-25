from tkinter import *

main = Tk()
main.geometry('600x300')
main.title('MAIN PAGE')
main['bg']='#98AFC7'

def productpage():
    main.destroy()
    import newfile

def studentpage():
    main.destroy()
    import studentfile
    
# LABELS

name_a = Label(main, text="Project by NIKITA SINGH AND HARSHITA KASHYAP", font=("Times new roman", 15))
name_a.pack()

Label(main, text="NETAJI SUBHAS UNIVERSITY OF TECHNOLOGY", padx=30,pady=30,bg='#78C7C7',font=("RALEWAY", 20)).pack(expand=True, fill=BOTH)

Label(main, text="Student's Project Details", padx=20,pady=20,bg='#78C7C7',font=("Times new roman", 20)).pack(expand=True, fill=BOTH)

#BUTTONS
Button(main,text="Student Details", font=("Times new roman", 15),bg= "dark grey", fg= "white", command=studentpage).pack(fill=X, expand=TRUE, side=LEFT)

Button(main,text="PRODUCT Details", font=("Times new roman", 15),bg= "dark grey", fg= "white", command=productpage).pack(fill=X, expand=TRUE, side=LEFT)

main.mainloop()
