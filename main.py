# Mag import tag libraries diring dapita, pati tong mga module nato na toas laen files
import tkinter as tk  # Libraries ni tkinter

from PIL import ImageTk

from tkinter import messagebox

# kaning upat mga modules na ni gi import lang gets?
from Admin.admin import Admin
from Admin.admininterface import AdminInterface
from DisplayStudents.display_students import DisplayStudents
from Registration.registration import RegisterStudent


# Main Window or Main Interface mao ni pinasugod nimong makita pag run sa code madapaker
class Select:
    def __init__(self, select):
        self.school_logo = None
        self.canvas = None
        self.school_label2 = None
        self.login_button = None
        self.display_button = None
        self.register_button = None
        self.button_height = None
        self.button_width = None
        self.photo = None
        self.school_label = None
        self.select = select
        select.title("Student Database System")

        select.grid_rowconfigure(0, weight=1)
        select.grid_columnconfigure(0, weight=1)
        select.grid_columnconfigure(1, weight=1)

        left_frame = tk.Frame(select)
        left_frame.grid(row=0, column=0, sticky="nsew")

        right_frame = tk.Frame(select, bg='#eddece')
        right_frame.grid(row=0, column=1, sticky="nsew")

        self.add_left_widgets(left_frame)
        self.add_right_widgets(right_frame)

    def add_left_widgets(self, frame):
        self.photo = ImageTk.PhotoImage(file="../Pictures/logo1.png")
        self.school_label = tk.Label(frame, text="Welcome to Student Database System", font=("Arial", 11, 'bold'))
        self.school_label.pack(pady=(150, 10))
        self.school_logo = tk.Label(frame, image=self.photo)
        self.school_logo.pack(pady=(10, 10))
        self.school_label2 = tk.Label(frame, text="North Eastern Mindanao State University", font=("Arial", 11, 'bold'))
        self.school_label2.pack(pady=10)

    def add_right_widgets(self, frame):
        self.button_width = 27
        self.button_height = 2
        self.register_button = tk.Button(frame, text="Register Student", font=("Arial", 8, "bold"),
                                             width=self.button_width, height=self.button_height,
                                             command=self.register_student)
        self.register_button.pack(pady=(200, 10), padx=10)

        self.display_button = tk.Button(frame, text="Search and Display", font=("Arial", 8, "bold"),
                                            width=self.button_width, height=self.button_height,
                                            command=self.display_students)
        self.display_button.pack(pady=10, padx=10)

        self.login_button = tk.Button(frame, text="Admin", font=("Arial", 8, "bold"),
                                          width=self.button_width, height=self.button_height, command=self.admin)
        self.login_button.pack(pady=10, padx=10)

    def register_student(self):
        self.select.withdraw()
        register_root = tk.Tk()
        register_root.geometry("800x600")
        register_root.protocol("WM_DELETE_WINDOW", lambda: self.on_close(register_root))
        RegisterStudent(register_root)

    # function ni para sa pag search or display sa mga student na na register na
    def display_students(self):
        self.select.withdraw()
        display_root = tk.Tk()
        display_root.geometry("800x600")
        display_root.protocol("WM_DELETE_WINDOW", lambda: self.on_close(display_root))
        DisplayStudents(display_root)

    # para ma open and admin section mga madapaker
    def admin(self):
        self.select.withdraw()
        admin_root = tk.Tk()
        admin_root.geometry("800x600")
        admin_root.protocol("WM_DELETE_WINDOW", lambda: self.on_close(admin_root))
        Admin(admin_root, lambda: self.open_admininterface(admin_root))

    # Function ni aron pag exit nimog admin interface mobalik kag saakoa, djk para mo balik kag main interface
    def open_admininterface(self, master):
        admininterface_root = tk.Toplevel(master)
        admininterface_root.geometry("800x600")
        admininterface_root.protocol("WM_DELETE_WINDOW", lambda: self.on_close(admininterface_root))
        AdminInterface(admininterface_root, lambda: self.open_main())

    # Function ni arong ma open jd and main interface ig balik nimo sa iya, marupok kang yawaa ka, jk para mobalik jd ka
    # sa main interface
    def open_main(self):
        self.select.withdraw()
        admin_root = tk.Tk()
        admin_root.protocol("WM_DELETE_WINDOW", lambda: self.on_close(admin_root))
        Admin(admin_root, lambda: self.open_admininterface(admin_root))
        self.select.deiconify()

    # function ni aron ma destroy imong kinabuhi, char para ma destroy tong mga naka close na window tas ibalik ra niya
    # kay marupok man ka, djk ibalik lang niya and window na na destroy, idk kinawat lang ni nako online na code
    def on_close(self, close_root):
        close_root.destroy()
        if close_root == self.select:
            self.select = None
        else:
            self.select.deiconify()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = Select(root)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        messagebox.showerror("Error", "Keyboard Interruption")
