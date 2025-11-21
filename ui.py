from data2 import database
from tkinter import *
from tkinter import messagebox
root = Tk()

db = database("F:/mydtabase1.db")

root.title("phonebook")
root.geometry("800x1000")
root.configure(bg="gray")
root.resizable(1,0)

#functions



def add():
    fname = ent_fname.get()
    address = ent_address.get()
    lname = ent_lname.get()
    phone = ent_phone.get()
    if  not phone.isdigit():
        messagebox.showerror("error","value of phone is not valid")
    else:
        txtbox.insert("end",f"{fname},{lname},{address},{phone} \n")
        db.insert_rec(fname,lname,address,phone)
    return
    
def delete():
    txtbox.delete("1.0", "end") 
    
    
def cl_all():
    ent_address.delete(0,END)
    ent_fname.delete(0,END)
    ent_phone.delete(0,END)
    ent_lname.delete(0,END) 
    
def search():        
    query = ent_search.get()
    txtbox.delete("1.0",END)
    result = db.search(query)
    if result: 
        for i in result:
            txtbox.insert(END,f"{i}/n")






       
#lables and entrys        
# Search entry + label
lbl_search = Label(text="Search:", font="arial 15", bg='gold')
lbl_search.place(x=400, y=700)
ent_search = Entry(font="arial 15")
ent_search.place(x=480, y=700)

# ID entry + label (برای Update)
lbl_edit = Label(text="edit: ", font="arial 15", bg='gold')
lbl_edit.place(x=30, y=700)
ent_edit = Entry(font="arial 15")
ent_edit.place(x=80, y=700)
lbl_fname = Label(text="Fname:",font="arial 20",bg='gold')
lbl_fname.place(x=30,y=30)
ent_fname = Entry(font="arial 15")
ent_fname.place(x=130,y=35)

lbl_lname = Label(text="lname:",font="arial 20",bg='gold')
lbl_lname.place(x=30,y=100)

ent_lname = Entry(font="arial 15")
ent_lname.place(x=130,y=100)

#x => 300      y=> 70
lbl_phone = Label(text="Phone:",font="arial 20",bg='gold')
lbl_phone.place(x=400,y=30)


ent_phone = Entry(font="arial 15")
ent_phone.place(x=500,y=35)

lbl_address = Label(text="Address:",font="arial 20",bg='gold')
lbl_address.place(x=400,y=100)


ent_address = Entry(font="arial 15")
ent_address.place(x=515,y=105)




#buttons 
btn_add = Button(text="add",command=add,bg='orange')
btn_add.place(x=100,y=190)

btn_delete = Button(text="delete",command=delete,bg="orange")
btn_delete.place(x=200,y=190)

btn_del_ent = Button(text="clear all entrys",command=cl_all,bg="orange")
btn_del_ent.place(x=300,y=190)
btn_search = Button(text="search",command=search)
btn_search.place(x=350, y=700)
#text box 
txtbox = Text(width=50,height=20)
txtbox.place(x=100,y=250)

root.mainloop()























