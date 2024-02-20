import tkinter as tk
from Admin.modify import Modify
from Admin.delete import Delete


class AdminInterface:
    def __init__(self, master4, open_main):
        self.master4 = master4
        master4.title("Admin")
        self.open_main = open_main

        self.button_width = 25
        self.button_height = 2

        self.modify_button = tk.Button(master4, text="Modify Student", font=("Arial", 9, "bold"),
                                       width=self.button_width, height=self.button_height, command=self.open_modify)
        self.modify_button.grid(row=0, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(master4, text="Delete Student", font=("Arial", 9, "bold"),
                                       width=self.button_width, height=self.button_height, command=self.open_delete)
        self.delete_button.grid(row=1, column=0, padx=10, pady=10)

        self.main_button = tk.Button(master4, text="Go Back", font=("Arial", 9, "bold"),
                                     width=self.button_width, height=self.button_height, command=self.open_main)

    def open_modify(self):
        self.master4.withdraw()
        modify_root = tk.Toplevel(self.master4)
        modify_root.protocol("WM_DELETE_WINDOW", lambda: self.on_close(modify_root))
        Modify(modify_root)

    def open_delete(self):
        self.master4.withdraw()
        delete_root = tk.Toplevel(self.master4)
        delete_root.protocol("WM_DELETE_WINDOW", lambda: self.on_close(delete_root))
        Delete(delete_root)

    def on_close(self, close_root):
        close_root.destroy()
        self.master4.deiconify()
