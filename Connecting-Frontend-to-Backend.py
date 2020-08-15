from tkinter import *
import Backend

def get_selected_row(event):
    try:
        global selected_tuple
        index = listbox1.curselection()[0]
        selected_tuple = listbox1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass    #Do nothing

def view_command():
    listbox1.delete(0,END)
    for row in Backend.view():
        listbox1.insert(END,row)

def search_command():
    listbox1.delete(0,END)        
    for row in Backend.search(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()):
        listbox1.insert(END,row)

def add_command():
    Backend.insert(title_value.get(),author_value.get(),year_value.get(),isbn_value.get())
    listbox1.delete(0,END)
    listbox1.insert(END,(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()))         

def delete_command():
    Backend.delete(selected_tuple[0])
    

def update_command():
    Backend.update(selected_tuple[0], title_value.get(),author_value.get(),year_value.get(),isbn_value.get() )

window = Tk()

window.wm_title("BookStore")

l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "Author")
l2.grid(row = 0, column = 2)

l3 = Label(window, text = "Year")
l3.grid(row = 1, column = 0)

l4 = Label(window, text = "ISBN")
l4.grid(row = 1, column = 2)

title_value = StringVar()
e1 = Entry(window, textvariable = title_value)
e1.grid(row = 0, column = 1)

author_value = StringVar()
e2 = Entry(window, textvariable = author_value)
e2.grid(row = 0, column = 3)

year_value = StringVar()
e3 = Entry(window, textvariable = year_value)
e3.grid(row = 1, column = 1)

isbn_value = StringVar()
e4 = Entry(window, textvariable = isbn_value)
e4.grid(row = 1, column = 3)

listbox1 = Listbox(window, height = 6, width = 35)
listbox1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)

listbox1.configure(yscrollcommand = sb1.set)  #To attach scrollbar with the listbox
sb1.configure(command = listbox1.yview)

listbox1.bind('<<ListboxSelect>>', get_selected_row)  #Used to bind function with a widget

b1 = Button(window, text = "View All", width = 12,command=view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Search Entry", width = 12,command=search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add Entry", width = 12,command=add_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Delete Entry", width = 12,command=delete_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Update Entry", width = 12,command=update_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", width = 12,command=window.destroy)
b6.grid(row = 7, column = 3)


window.mainloop()
