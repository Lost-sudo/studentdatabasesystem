import tkinter as tk
from tkinter import messagebox


class Admin:
    # Initializes a new instance of the class
    # open_admininterface is a callback, so when the admin logged in successfully, admin interface will open
    def __init__(self, master3, open_admininterface):
        self.master3 = master3
        master3.title("Admin")
        self.open_admininterface = open_admininterface  # callback function to the instance variable self.open_admininterface
        self.master3.configure(bg="#eddece")

        self.admin_label = tk.Label(master3, text="Enter Admin Username and Password", font=("Arial", 10, "bold"), bg="#eddece")
        self.admin_label.pack(padx=(10, 10), pady=(200, 50))

        # GUI
        self.username_label = tk.Label(master3, text="Enter Username", bg="#eddece", font=("Arial", 10, "bold"))
        self.username_label.pack(padx=(10, 10), pady=2)
        self.username_entry = tk.Entry(master3, width=30, font=("Arial", 10))
        self.username_entry.pack(padx=0, pady=0)

        self.password_label = tk.Label(master3, text="Enter password", bg="#eddece", font=("Arial", 10, "bold"))
        self.password_label.pack(padx=(10, 10), pady=2)
        self.password_entry = tk.Entry(master3, show="*", width=30, font=("Arial", 10))
        self.password_entry.pack(padx=0, pady=0)

        self.submit_button = tk.Button(master3, text="Login", command=self.login, font=("Arial", 8),
                                       width=20, height=2)
        self.submit_button.pack(padx=2, pady=5)

    # login definition
    def login(self):
        # this retrieves the text entered on the entry widgets
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":  # checks if the username is admin
            # and password, password can also be change
            # if you want
            self.master3.withdraw()  # if the username and password are correct, the login interface will be close
            self.open_admininterface()  # if the username and password is correct the admin interface will be open
        else:
            messagebox.showerror("Error", "Invalid Username or Password")  # if the username and password are not correct,
            # this message box will be executed

    # definition to open to the admin interface
    def open_admininterface(self):
        admin_root = tk.Tk()  # creates a new window
        self.master3.destroy()  # after the open of the admin interface,
        # the login section will be destroyed to prevent it from using again
        admin_root.protocol("WM_DELETE_WINDOW", lambda: self.on_close(admin_root))

    def on_close(self, admin_root):  # This line defines the on_close method within the Admin class
        admin_root.destroy()  # This line destroys the admin root window when it is closed
        self.master3.deiconify()  # This line restores the visibility of the master3 window if the admin interface is closed
