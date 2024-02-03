import tkinter as tk
from tkinter import messagebox
import requests
import json
import os

def send_request():
    try:
        user_id = int(id_entry.get())
        url = requests.get('f"https://jsonplaceholder.typicode.com/users/{user_id}"')
        data = url.json()
        result.delete(1.0, tk.END)
        result.insert(tk.END, json.dumps(data, indent=4))
    except ValueError:
        messagebox.showerror("ID должен быть целым числом.")
    except requests.RequestException as e:
        messagebox.showerror(f"Ошибка запроса: {str(e)}")

def save_data():
    try:
        data = result.get(1.0, tk.END)
        foldername = 'saved_data'
        if not os.path.exists(foldername):
            os.makedirs(foldername)
        with open(os.path.join(foldername, 'data.json'), 'w') as file:
            file.write(data)
            messagebox.showinfo("Данные успешно сохранены.")
    except Exception as e:
        messagebox.showerror(f"Ошибка сохранения данных: {str(e)}")

bimbom = tk.Tk()
bimbom.title('request to jsonplaceholder')

id_label = tk.Label(bimbom, text='ID:')
id_label.grid(row=0, column=0, padx=5, pady=5)

id_entry = tk.Entry(bimbom)
id_label.grid(row=0, column=1, padx=5, pady=5)

send_button = tk.Button(bimbom, text='send request', command=send_request)
send_button.grid(row=0, column=2, padx=5, pady=5)

result = tk.Text(bimbom, width=60, height=20)
result.grid(row=1, column=0,columnspan=3, padx=5, pady=5)

save_buttn = tk.Button(bimbom, text='save', command=save_data)
save_buttn.grid(row=2, column=0,columnspan=3, padx=5, pady=5)

bimbom.mainloop()