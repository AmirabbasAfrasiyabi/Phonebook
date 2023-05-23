
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

window =tk. Tk()

window.title("Phonebook" )
window.geometry("520x420")
window.config(bg = "#C7E3EF")
window.resizable(width=False ,height= False)

#frame

Frame_up = Frame(window , width= 520 , height= 50 ,  bg="#DFB2F4")
Frame_up.grid (row=0 , column= 0 ,padx= 1 , pady= 1)

Frame_down = Frame(window , width= 520 , height= 180 ,  bg="#C7E3EF")
Frame_down.grid (row=1 , column= 0 ,padx= 1 , pady= 1)

Frame_table = Frame(window , width= 520 , height= 100 ,  bg="#C7E3EF" , relief= FLAT)
Frame_table.grid (row=2 , column= 0 , columnspan=2, padx= 1 , pady= 1  , sticky= NW)

listbox = tk.Listbox (  Frame_table  , height= 10 , width= 60  )
listbox. pack (side= LEFT , fill= BOTH , expand= 1 , padx= 5 , pady= 10)
  
# Function to add a new contact to the listbox

phonebook = {}

def Addcontact():

    # Get the user input values
    Firstname = E_Firstname.get()
    Lastname = E_Lastname.get()
    Gender= C_Gender.get()
    Telephone = E_Telephone.get()
    Email = E_Email.get()

    # Check if the contact already exists
    if (Firstname == "" or Lastname == ""  or Telephone == "" ):
        messagebox.showerror("Error", " please Please fill all the labels.")
    elif (Firstname  , Lastname , Telephone  ) in phonebook:
        messagebox.showerror("Error", "Phonenumber already exists.")
    else:
        # display a success message
        messagebox.showinfo("congurilation", " Your operation has been successfully completed .")

        # Add the new contact to the listbox
        phonebook[(Firstname , Lastname ,Telephone)] =  Gender , Email
        listbox.insert(END, f"{Firstname} {Lastname} : {Telephone}")

    # Clear the input fields
    
    E_Firstname.delete(0, tk.END)
    E_Lastname.delete(0, tk.END)
    C_Gender.delete(0, tk.END)
    E_Telephone.delete(0,tk.END)
    E_Email.delete(0,tk.END)
  
def Deletecontact ():
    selection = listbox.curselection()
    if selection:
        listbox.delete(selection)
        messagebox.showinfo("congurilation", " Your operation has been successfully completed.")
    else:
        messagebox.showwarning("Error", "Please select an Phonenumber to delete.")

def Resecontact():
    E_Firstname.delete(0, tk.END)
    E_Lastname.delete(0, tk.END)
    C_Gender.delete(0, tk.END)
    E_Telephone.delete(0,tk.END)
    E_Email.delete(0,tk.END)
    messagebox.showinfo("congurilation", " Your operation has been successfully completed.")

def Clearcontact():
    # clear the dictionary
    phonebook.clear()

    # clear the listbox
    listbox.delete(0, END)

# Define the search function
def Searchcontact():
    query = E_search.get().lower()
    if query:
        matches = [item for item in listbox.get(0, tk.END) if query in item.lower()]
        if matches:
            listbox.delete(0, tk.END)
            for match in matches:
                listbox.insert(tk.END, match)
            messagebox.showinfo("Success", f"{len(matches)} matches found")
        else:
            messagebox.showinfo("No matches found")  

# Define a function to handle the "Edit" button click
def Editcontact ():
    selected_item = listbox.curselection()
    if selected_item:
        index = selected_item[0]
        item = listbox.get(index)
        Fullname, Telephone = item.split(":")
        Firstname, Lastname = Fullname.split()
        E_Firstname.insert(0, Firstname)
        E_Lastname.insert(0, Lastname)
        E_Telephone.insert(0, Telephone)
        listbox.delete(index)
        with open("phonebook.txt", "r") as f:
            lines = f.readlines()
        with open("phonebook.txt", "w") as f:
            for line in lines:
                if line.strip() != f"{Fullname}:{Telephone}":
                    f.write(line)
        messagebox.showinfo("Success", "Phonebook entry edited successfully")
    else:
        messagebox.showerror("Error", "Please select an item to edit")

    
def Loadcontact():
    listbox.delete(0, tk.END)
    try:
        with open("phonebook.txt", "r") as f:
            for line in f:
                Fullname, Telephone = line.strip().split(":")
                listbox.insert(tk.END, f"{Fullname} : {Telephone}")
                listbox.insert(tk.END, line.strip())
        messagebox.showinfo("congurilation", "Your operation has been successfully completed.")
    except FileNotFoundError:
        messagebox.showerror("Error", "Phonebook file not found")

def Exitcontact():
    window.destroy()


#frame_up widght

App_name = tk.Label(Frame_up , text=" Add contact " , height= 1, font=("vardana 17 bold") , bg ="#DFB2F4" , fg ="#27353B" )
App_name.place(x = 5 ,y = 5 )

L_Firstname = tk.Label(Frame_down , text= "Firstname:" , height= 1 , width= 10  , font= ("Arial 10") , background="#FADAD6" , foreground= "#27353B" )
L_Firstname.place(x=10 , y=20)
E_Firstname = tk.Entry(Frame_down , width= 25 , justify= "left" , highlightthickness=1 , relief="solid")
E_Firstname.place( x=110 ,y = 20)

L_Lastname = tk.Label(Frame_down , text= "Lastname:" , height= 1  , width= 10,  font= ("Arial 10") , background="#FADAD6" , foreground= "#27353B" )
L_Lastname.place(x=10 , y=50)
E_Lastname = tk.Entry(Frame_down , width= 25 , justify= "left" , highlightthickness=1 , relief="solid")
E_Lastname.place( x=110 ,y = 50)

L_Gender = tk.Label(Frame_down , text= "Gender:" , height= 1 ,width= 10  , font= ("Arial 10") , background="#FADAD6" , foreground= "#27353B" )
L_Gender.place(x=10 , y=80)
C_Gender = ttk.Combobox(Frame_down , width= 22)
C_Gender  ['values'] = [ "" , "Male" , "Female"]
C_Gender.place( x=110 ,y = 80)

L_Telephone = tk.Label(Frame_down , text= "Phone number:" , height= 1  , width= 11,  font= ("Arial 10") , background="#FADAD6" , foreground= "#27353B" )
L_Telephone.place(x=10 , y=110)
E_Telephone = tk.Entry(Frame_down , width= 25 , justify= "left" , highlightthickness=1 , relief="solid")
E_Telephone.place( x=110 ,y = 110)

L_Email =tk. Label(Frame_down , text= "Email:" , height= 1  , width= 10,  font= ("Arial 10") , background="#FADAD6" , foreground= "#27353B" )
L_Email.place(x=10 , y=140)
E_Email = tk.Entry(Frame_down , width= 25 , justify= "left" , highlightthickness=1 , relief="solid")
E_Email.place( x=110 ,y = 140)

b_search =tk. Button(Frame_down , text= "search:" , command= Searchcontact, height= 1  ,  font= ("Arial 10") , background="#F4845F" , foreground="#27353B"  )
b_search.place(x= 290 , y= 20)
E_search = tk.Entry(Frame_down , width= 20 , justify= "left" , font= ("Arial 10") , highlightthickness=1 , relief="solid")
E_search.place( x= 360 ,y = 20)

b_Addcontact = tk.Button(Frame_down , text= "Add:" , command= Addcontact , height= 1  ,width=10,  font= ("Arial 10") , background="#F95738" , foreground="#27353B"  )
b_Addcontact.place(x= 290 , y= 50)

b_Deletecontact = Button(Frame_down , text= "Delete:" ,command= Deletecontact, height= 1  ,width=10,  font= ("Arial 10") , background="#84DCC6" , foreground="#27353B"  )
b_Deletecontact.place(x= 410 , y= 50)

b_Clearcontact = Button(Frame_down , text= "Clear:" , command = Clearcontact ,  height= 1  ,width=10,  font= ("Arial 10") , background="#F4845F" , foreground="#27353B"  )
b_Clearcontact.place(x= 410 , y= 80)

b_Resetcontact = Button(Frame_down , text= "Reset:" , command= Resecontact,  height= 1  ,width=10,  font= ("Arial 10") , background="#F4845F" , foreground="#27353B"  )
b_Resetcontact.place(x= 290 , y= 80)

b_Editcontact = Button(Frame_down , text= "Edit:"  , command=Editcontact ,height= 1  ,width=10,  font= ("Arial 10") , background="#F4845F" , foreground="#27353B"  )
b_Editcontact.place(x= 410 , y= 110)

b_Loadcontact = Button(Frame_down , text= "Load:"  ,command = Loadcontact, height= 1  ,width=10,  font= ("Arial 10") , background="#F4845F" , foreground="#27353B"  )
b_Loadcontact.place(x= 290, y= 110)

b_Exitcontact = Button(Frame_down , text= "Exit:"  ,command = Exitcontact , height= 1  ,width=25,  font= ("Arial 10") , background="#F4845F" , foreground="#27353B"  )
b_Exitcontact.place(x= 290, y= 144)

window.mainloop()






