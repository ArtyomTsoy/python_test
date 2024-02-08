import tkinter as tk
from tkinter import messagebox
import requests
import json
import os

class JsonApp:
    def __init__(self, master):
        self.master = master
        master.title('Requester')

        self.id_label = tk.Label(master, text="ID:")
        self.id_label.grid(row=0, column=0, padx=5, pady=5)

        self.id_entry = tk.Entry(master)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.send_button = tk.Button(master, text="Send request", command=self.send_request)
        self.send_button.grid(row=0, column=2, padx=5, pady=5)

        self.result = tk.Text(master, width=60, height=20)
        self.result.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.save_button = tk.Button(master, text="Save", command=self.save_data)
        self.save_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    def send_request(self):
        try:
            user_id = int(self.id_entry.get())
            url = requests.get('f"https://jsonplaceholder.typicode.com/users/{user_id}"')
            data = url.json()
            self.result.delete(1.0, tk.END)
            self.result.insert(tk.END, json.dumps(data, indent=4))
        except ValueError:
            messagebox.showerror("ID должен быть целым числом.")
        except requests.RequestException as e:
            messagebox.showerror(f"Ошибка запроса: {str(e)}")

    def save_data(self):
        try:
            data = self.result.get(1.0, tk.END)
            foldername = "saved_data"
            if not os.path.exists(foldername):
                os.makedirs(foldername)
            with open(os.path.join(foldername, "data.json"), "w") as file:
                file.write(data)
                messagebox.showinfo("Ура", "Данные успешно сохранены.")
        except Exception as e:
            messagebox.showerror("О нет", f"Ошибка сохранения данных: {str(e)}")

def main():
    bimbom = tk.Tk()
    app = JsonApp(bimbom)
    bimbom.mainloop()

if __name__ == "__main__":
    main()
