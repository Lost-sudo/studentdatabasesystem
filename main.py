# Mag import tag libraries diring dapita, pati tong mga module nato na toas laen files
import tkinter as tk  # Libraries ni tkinter
# kaning upat mga modules na ni gi import lang gets?
from Admin.admin import Admin
from Admin.admininterface import AdminInterface
from DisplayStudents.display_students import DisplayStudents
from Registration.registration import RegisterStudent


# Main Window or Main Interface mao ni pinasugod nimong makita pag run sa code madapaker
class Select:
    def __init__(self, select):  # nag initialized ni sa main window mga madapaker
        self.select = select
        select.title("Student Database Management System")  # title ni siya

        self.photo = tk.PhotoImage(file="../Pictures/logo1.png")  # oh logo ni siya sa nemsu mga baddy

        # kwan ni gi set lang nako and width og height sa akong button aron di sila mag kimpang
        self.button_width = 27
        self.button_height = 2

        # Mao ning imong makita sa taas ng picture pag run nimo sa code
        self.school_label = tk.Label(select, text="North Eastern Mindanao State University", font=("Arial", 8, "bold"),
                                     image=self.photo, compound=tk.BOTTOM)
        self.school_label.grid(row=0, column=0, padx=(150, 10), pady=10)

        # Mga Buttons ni mga madapaker
        self.register_button = tk.Button(select, text="Register Student", font=("Arial", 8, "bold"),
                                         width=self.button_width, height=self.button_height,
                                         command=self.register_student)
        self.register_button.grid(row=1, column=0, padx=(150, 10), pady=10)

        self.display_button = tk.Button(select, text="Search and Display", font=("Arial", 8, "bold"),
                                        width=self.button_width, height=self.button_height,
                                        command=self.display_students)
        self.display_button.grid(row=2, column=0, padx=(150, 10), pady=10)

        self.login_button = tk.Button(select, text="Admin", font=("Arial", 8, "bold"),
                                      width=self.button_width, height=self.button_height, command=self.admin)
        self.login_button.grid(row=3, column=0, padx=(150, 10), pady=10)

    # function ni aron pag pindot nimog register student sa main interface maka adto kag laen planeta, char para ma open
    # and registration interface
    def register_student(self):
        self.select.withdraw()
        register_root = tk.Tk()
        register_root.geometry("500x500")
        register_root.protocol("WM_DELETE_WINDOW", lambda: self.on_close(register_root))
        RegisterStudent(register_root)

    # function ni para sa pag search or display sa mga student na na register na
    def display_students(self):
        self.select.withdraw()
        display_root = tk.Tk()
        display_root.protocol("WM_DELETE_WINDOW", lambda: self.on_close(display_root))
        DisplayStudents(display_root)

    # para ma open and admin section mga madapaker
    def admin(self):
        self.select.withdraw()
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
    root.geometry("500x500")
    app = Select(root)
    root.mainloop()
