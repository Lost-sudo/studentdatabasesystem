import tkinter as tk
import datetime
from tkinter import messagebox


class RegisterStudent:
    def __init__(self, master1):
        self.master1 = master1
        master1.title("Register Student")

        try:
            with open('../Files/last_student_id.txt', 'r') as id_file:
                self.last_student_id = int(id_file.read().strip())
        except FileNotFoundError:
            self.last_student_id = 0

        self.first_name_label = tk.Label(master1, text="First Name")
        self.first_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.first_name_entry = tk.Entry(master1)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.last_name_label = tk.Label(master1, text="Last Name")
        self.last_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.last_name_entry = tk.Entry(master1)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.age_label = tk.Label(master1, text="Age")
        self.age_label.grid(row=2, column=0, padx=10, pady=10)
        self.age_entry = tk.Entry(master1)
        self.age_entry.grid(row=2, column=1, padx=10, pady=10)

        self.address_label = tk.Label(master1, text="Address")
        self.address_label.grid(row=3, column=0, padx=10, pady=10)
        self.address_entry = tk.Entry(master1)
        self.address_entry.grid(row=3, column=1, padx=10, pady=10)

        self.year_level_label = tk.Label(master1, text="Year level")
        self.year_level_label.grid(row=4, column=0, padx=10, pady=10)
        self.year_level_entry = tk.Entry(master1)
        self.year_level_entry.grid(row=4, column=1, padx=10, pady=10)

        self.course_label = tk.Label(master1, text="Course", bd=0.5, relief="solid")
        self.course_label.grid(row=5, column=0, columnspan=2, padx=10, pady=(10, 0), sticky='we')
        self.courses = ["Bachelor of Science in Computer Engineering",
                        "Bachelor of Science in Information Technology",
                        "Bachelor of Science in Computer Science",
                        "Bachelor of Science in Hotel and Restaurant Management",
                        "Bachelor of Science in Criminology",
                        "Bachelor of Science in Industrial Technology major in Welding and Fabrication",
                        "Bachelor of Science in Industrial Technology major in Mechanical Technology"]
        self.course = tk.Listbox(master1, height=len(self.courses), width=80)
        for course in self.courses:
            self.course.insert(tk.END, course)

        self.course.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='w')

        self.submit_button = tk.Button(master1, text="Submit", command=self.register)
        self.submit_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def register(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        age = self.age_entry.get()
        address = self.address_entry.get()
        year_level = self.year_level_entry.get()
        course_index = self.course.curselection()
        if course_index:
            selected_course = self.courses[course_index[0]]

            current_year = datetime.datetime.now().year
            self.last_student_id += 1
            with open('../Files/last_student_id.txt', 'w') as id_file:
                id_file.write(str(self.last_student_id))

            student_id = f"{current_year}-{self.last_student_id:05}"

            with open('../Files/students.txt', 'a') as file:
                file.write(
                    f"{student_id},{first_name},{last_name},{age},{address},{year_level},{selected_course}\n")
            messagebox.showinfo("Success", "Registration Successful")
            file.close()
            self.master1.destroy()
        else:
            messagebox.showerror("Error", "Please select a course.")
