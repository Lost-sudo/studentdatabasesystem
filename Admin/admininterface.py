import tkinter as tk
from Admin.modify import Modify
from Admin.delete import Delete


class AdminInterface:
    # This class initializes the admin interface with the given master4
    # window and a callback function open_main to go back to the main interface.
    def __init__(self, master4, open_main):
        self.master4 = master4
        master4.title("Admin")
        self.open_main = open_main
        self.master4.configure(bg="#eddece")

        # set the width and height of the buttons in the interface.
        self.button_width = 27
        self.button_height = 2

        # GUI for buttons associated with each command
        self.modify_label = tk.Label(master4, text="What would you like to do?", font=("Arial", 10, 'bold'),
                                     bg="#eddece")
        self.modify_label.pack(padx=10, pady=(250, 2))

        self.modify_button = tk.Button(master4, text="Modify Student", font=("Arial", 9, "bold"),
                                       width=self.button_width, height=self.button_height, command=self.open_modify)
        self.modify_button.pack(padx=(10, 10), pady=2)

        self.delete_button = tk.Button(master4, text="Delete Student", font=("Arial", 9, "bold"),
                                       width=self.button_width, height=self.button_height, command=self.open_delete)
        self.delete_button.pack(padx=(10, 10), pady=2)

        # self.main_button = tk.Button(master4, text="Go Back", font=("Arial", 9, "bold"),
        #                              width=self.button_width,
        #                              height=self.button_height, command=self.open_main)

    def open_modify(self):  # called when the "Modify Student" button is clicked.
        self.master4.withdraw()  # hides the current admin interface (master4 window) using the withdrawal method
        modify_root = tk.Toplevel(
            self.master4)  # it creates a new top-level window (Toplevel) for the modification interface
        modify_root.geometry("900x400")
        modify_root.protocol("WM_DELETE_WINDOW", lambda: self.on_close(
            modify_root))  # protocol is set for the new window to call the on_close method when it is closed.
        Modify(modify_root)  # the Modify class is instantiated with the new window.

    def open_delete(self):
        self.master4.withdraw()
        delete_root = tk.Toplevel(self.master4)
        delete_root.geometry("900x400")
        delete_root.protocol("WM_DELETE_WINDOW", lambda: self.on_close(delete_root))
        Delete(delete_root)

    def on_close(self, close_root):  # This method is called when a child window
        # (modification or deletion interface) is closed
        close_root.destroy()  # destroys the child window
        self.master4.deiconify()  # restores the visibility of the main admin interface
