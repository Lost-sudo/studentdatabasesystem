# Mag import tag libraries diring dapita, pati tong mga module nato na toas laen files
import tkinter as tk  # Libraries ni tkinter
# kaning upat mga modules na ni gi import lang gets?
from Admin.admin import Admin
from Admin.admininterface import AdminInterface
from DisplayStudents.display_students import DisplayStudents
from Registration.registration import RegisterStudent


# Main Window or Main Interface mao ni pinasugod nimong makita pag run sa code madapaker
class Select:
    def __init__(self, select):
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

        left_frame = tk.Frame(select)
        left_frame.grid(row=0, column=0, sticky='nsew')
        select.grid_rowconfigure(0, weight=1)
        select.grid_columnconfigure(0, weight=1)

        right_frame = tk.Frame(select, bg='#eddece')
        right_frame.grid(row=0, column=1, sticky='nsew')
        select.grid_rowconfigure(0, weight=1)
        select.grid_columnconfigure(0, weight=1)

        self.add_left_widgets(left_frame)
        self.add_right_widgets(right_frame)

    def add_left_widgets(self, frame):
        self.photo = tk.PhotoImage(file="../Pictures/logo1.png")
        self.school_label = tk.Label(frame, text="Welcome to Student Database System", font=("Arial", 11, 'bold'),
                                     image=self.photo, compound=tk.BOTTOM)
        self.school_label.grid(row=0, column=0, padx=80, pady=(150, 10))
        self.school_label2 = tk.Label(frame, text="North Eastern Mindanao State University", font=("Arial", 11, 'bold'))
        self.school_label2.grid(row=1, column=0, padx=10, pady=10, sticky='n')

    def add_right_widgets(self, frame):
        self.button_width = 27
        self.button_height = 2
        self.register_button = tk.Button(frame, text="Register Student", font=("Arial", 8, "bold"),
                                             width=self.button_width, height=self.button_height,
                                             command=self.register_student)
        self.register_button.grid(row=1, column=0, padx=80, pady=(200, 10), sticky='ew')

        self.display_button = tk.Button(frame, text="Search and Display", font=("Arial", 8, "bold"),
                                            width=self.button_width, height=self.button_height,
                                            command=self.display_students)
        self.display_button.grid(row=2, column=0, padx=80, pady=10, sticky='ew')

        self.login_button = tk.Button(frame, text="Admin", font=("Arial", 8, "bold"),
                                          width=self.button_width, height=self.button_height, command=self.admin)
        self.login_button.grid(row=3, column=0, padx=80, pady=10, sticky='ew')

    def register_student(self):
        # self.select.withdraw()
        register_root = tk.Tk()
        register_root.geometry("500x500")
        register_root.protocol("WM_DELETE_WINDOW", lambda: self.on_close(register_root))
        RegisterStudent(register_root)

    # function ni para sa pag search or display sa mga student na na register na
    def display_students(self):
        # self.select.withdraw()
        display_root = tk.Tk()
        display_root.protocol("WM_DELETE_WINDOW", lambda: self.on_close(display_root))
        DisplayStudents(display_root)

    # para ma open and admin section mga madapaker
    def admin(self):
        # self.select.withdraw()
        admin_root = tk.Tk()
        admin_root.protocol("WM_DELETE_WINDOW", lambda: self.on_close(admin_root))
        Admin(admin_root, lambda: self.open_admininterface(admin_root))

    # Function ni aron pag exit nimog admin interface mobalik kag saakoa, djk para mo balik kag main interface
    def open_admininterface(self, master):
        admininterface_root = tk.Toplevel(master)
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
        self.select.deiconify()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = Select(root)
    root.mainloop()
