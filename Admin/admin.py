import tkinter as tk
from tkinter import messagebox


class Admin:
    def __init__(self, master3, open_admininterface):
        self.master3 = master3
        master3.title("Admin")
        self.open_admininterface = open_admininterface

        self.username_label = tk.Label(master3, text="Enter Username")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(master3)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_label = tk.Label(master3, text="Enter password")
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(master3, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.submit_button = tk.Button(master3, text="Login", command=self.login)
        self.submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            self.master3.withdraw()
            self.open_admininterface()
        else:
            messagebox.showerror("Invalid Username or Password")

    def open_admininterface(self):
        admin_root = tk.Tk()
        self.master3.destroy()
        admin_root.protocol("WM_DELETE_WINDOW", lambda: self.on_close(admin_root))

    def on_close(self, admin_root):
        admin_root.destroy()
        self.master3.deiconify()
