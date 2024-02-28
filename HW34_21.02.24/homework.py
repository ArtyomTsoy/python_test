from tkinter import *
from db_con import *

def re_render_list(listbox):
    values = show_contacts(mycursor)
    listbox['listvariable'] = Variable(value=values)

window = Tk()
window.title("Контакты")
window.geometry("720x480")
window.resizable(False, False)

left_frame = Frame()

Label(left_frame, text='Список').pack()
user_list = Listbox(left_frame)
re_render_list(user_list)

user_list.pack(side=LEFT, fill=BOTH, expand=True)

left_frame.pack(fill=BOTH, side=LEFT, expand=True)

right_frame = Frame(bg="#eee")
Label(right_frame, text='Добавить/обновить/удалить контакт').pack()

username_text = Text(right_frame, height=1, width=30)
username_text.pack()

def create_contact_handler():
    create_contact(username_text.get(1.0, END))
    re_render_list(user_list)

def update_contact_handler():
    selected_index = user_list.curselection()
    contact_id = user_list.get(selected_index)
    update_contact(contact_id, username_text.get(1.0, END))
    re_render_list(user_list)

def delete_contact_handler():
    selected_index = user_list.curselection()
    contact_id = user_list.get(selected_index)
    delete_contact(contact_id)
    re_render_list(user_list)

Button(right_frame, text="Сохранить", command=create_contact_handler).pack()
Button(right_frame, text="Обновить", command=update_contact_handler).pack()
Button(right_frame, text="Удалить", command=delete_contact_handler).pack()

right_frame.pack(fill=BOTH, side=RIGHT, expand=True)

window.mainloop()