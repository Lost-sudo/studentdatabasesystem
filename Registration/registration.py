import tkinter as tk  # for GUI
import datetime  # for working dates and times
from tkinter import messagebox  # for displaying message boxes


class RegisterStudent:  # defines a class for registration window
    def __init__(self, master1):  # initializes the instance of a class
        self.master1 = master1
        master1.title("Register Student")
        self.master1.configure(bg="#eddece")

        # tries to open the last_student_id.txt to read the last student id
        try:
            with open('../Files/last_student_id.txt', 'r') as id_file:
                self.last_student_id = int(id_file.read().strip())
        except FileNotFoundError:
            self.last_student_id = 0

        self.label = tk.Label(master1, text="Student Registration Interface", font=("Arial", 15, 'bold'), bg="#eddece")
        self.label.pack(fill="both")

        # Label and Entry for the first name
        self.first_name_label = tk.Label(master1, text="First Name", font=("Arial", 10, 'bold'), bg="#eddece")
        self.first_name_label.pack(pady=2, padx=(10, 10))
        self.first_name_entry = tk.Entry(master1, width=30)
        self.first_name_entry.pack(pady=0, padx=0)

        # Label and Entry for the last name
        self.last_name_label = tk.Label(master1, text="Last Name", font=("Arial", 10, 'bold'), bg="#eddece")
        self.last_name_label.pack(pady=2, padx=(10, 10))
        self.last_name_entry = tk.Entry(master1, width=30)
        self.last_name_entry.pack(pady=0, padx=0)

        # Label and Entry for the age
        self.age_label = tk.Label(master1, text="Age", font=("Arial", 10, 'bold'), bg="#eddece")
        self.age_label.pack(pady=2, padx=(10, 10))
        self.age_entry = tk.Entry(master1, width=30)
        self.age_entry.pack(pady=0, padx=0)

        # Label and Entry for the address
        self.address_label = tk.Label(master1, text="Address", font=("Arial", 10, 'bold'), bg="#eddece")
        self.address_label.pack(pady=2, padx=(10, 10))
        self.address_entry = tk.Entry(master1, width=30)
        self.address_entry.pack(pady=0, padx=0)

        # Label and Entry for the Year Level
        self.year_level_label = tk.Label(master1, text="Year level", font=("Arial", 10, 'bold'), bg="#eddece")
        self.year_level_label.pack(pady=2, padx=(10, 10))
        self.year_level_entry = tk.Entry(master1, width=30)
        self.year_level_entry.pack(pady=0, padx=0)

        # Label and a Listbox of courses available
        self.course_label = tk.Label(master1, text="Course List", font=("Arial", 15, 'bold'), bg="#eddece")
        self.course_label.pack(pady=2, padx=2, fill='both')
        self.courses = ["Bachelor of Science in Computer Engineering",
                        "Bachelor of Science in Information Technology",
                        "Bachelor of Science in Computer Science",
                        "Bachelor of Science in Hotel and Restaurant Management",
                        "Bachelor of Science in Criminology",
                        "Bachelor of Science in Industrial Technology major in Welding and Fabrication",
                        "Bachelor of Science in Industrial Technology major in Mechanical Technology"]
        self.course = tk.Listbox(master1, height=len(self.courses), font=("Arial", 10, 'bold'), width=100)   # set height and width for the listbox
        for course in self.courses:  # this loops iterates over each courses in the list self.courses
            self.course.insert(tk.END, course)  # this inserts each course in the list box

        self.course.pack(pady=2, padx=2, fill='both')

        # button for submitting and associate it with the register method
        self.submit_button = tk.Button(master1, text="Submit", command=self.register, font=("Arial", 10, 'bold'))
        self.submit_button.pack(pady=2, padx=2)

    # definition for register method called from the submitted button
    def register(self):
        # retrieves the input values
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        age = self.age_entry.get()
        address = self.address_entry.get()
        year_level = self.year_level_entry.get()
        course_index = self.course.curselection()
        if course_index:  # this checks if the user has selected a course
            selected_course = self.courses[course_index[0]]  # retrieves the selected course

            current_year = datetime.datetime.now().year  # retrieves the current year which has been used in the student id
            self.last_student_id += 1  # this increments the last student id by 1
            with open('../Files/last_student_id.txt', 'w') as id_file:  # this opens the last_student_id.txt in written mode
                id_file.write(str(self.last_student_id))  # this writes the updated value of the last_student_id.txt

            student_id = f"{current_year}-{self.last_student_id:05}"  # this generates a unique student ID

            with open('../Files/students.txt', 'a') as file:  # this opens the students.txt in appended mode
                # this writes the student's information to the file
                file.write(
                    f"{student_id},{first_name},{last_name},{age},{address},{year_level},{selected_course}\n")
            messagebox.showinfo("Success", "Registration Successful")  # displays a message box indicating
            # registration successful
            file.close()  # closes the file after writing the student's information
        else:
            messagebox.showerror("Error", "Please select a course.")  # if no course is selected this
            # displays an error message
