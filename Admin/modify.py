import tkinter as tk
from tkinter import messagebox
from DisplayStudents.display_students import DisplayStudents


class Modify(DisplayStudents):  # this class inherits from DisplayStudents,
    # so we can use the display function in searching the data
    def __init__(self, master5):  # overrides methods to add modification functionality
        self.master5 = master5
        super().__init__(master5)  # this is the one that calls the display function from the DisplayStudents class
        # __init__(master5) calling constructor that allows to perform the display function
        master5.title("Modify Student")

        self.modify_button = tk.Button(master5, text="Modify", command=self.modify_student)
        self.modify_button.grid(row=2, column=3, padx=(0, 5), pady=(0, 5), sticky="w")

    def modify_student(self):  # called when the modified button is clicked
        selected_student = self.search_results_treeview.focus()  # checks if a student is selected
        if selected_student:  # if selected, this block of code will be performed
            student_id = self.search_results_treeview.item(selected_student, "text")  # retrieve the student ID and current info from the treeview

            modify_window = tk.Toplevel(self.master5)  # creates a new window for modifying data
            modify_window.title("Modify Student")

            current_first_name = self.search_results_treeview.item(selected_student, "value")[0]  # retrieves the first value index,which corresponds to the first name
            current_last_name = self.search_results_treeview.item(selected_student, "value")[1]  # retrieves the first value index,which corresponds to the last name
            current_age = self.search_results_treeview.item(selected_student, "value")[2]  # retrieves the first value index,which corresponds to the age
            current_address = self.search_results_treeview.item(selected_student, "value")[3]  # retrieves the first value index,which corresponds to the address
            current_year_level = self.search_results_treeview.item(selected_student, "value")[4]  # retrieves the first value index,which corresponds to the year_level
            current_course = self.search_results_treeview.item(selected_student, "value")[5]  # retrieves the first value index,which corresponds to the course selected

            tk.Label(modify_window, text="Enter First Name: ").grid(row=0, column=0, padx=10, pady=10)
            new_first_name_entry = tk.Entry(modify_window)
            new_first_name_entry.grid(row=0, column=1, padx=10, pady=10)
            new_first_name_entry.insert(0, current_first_name)

            tk.Label(modify_window, text="Enter Last Name: ").grid(row=2, column=0, padx=10, pady=10)
            new_last_name_entry = tk.Entry(modify_window)
            new_last_name_entry.grid(row=2, column=1, padx=10, pady=10)
            new_last_name_entry.insert(1, current_last_name)

            tk.Label(modify_window, text="Enter Age: ").grid(row=3, column=0, padx=10, pady=10)
            new_age_entry = tk.Entry(modify_window)
            new_age_entry.grid(row=3, column=1, padx=10, pady=10)
            new_age_entry.insert(2, current_age)

            tk.Label(modify_window, text="Enter Address: ").grid(row=4, column=0, padx=10, pady=10)
            new_address_entry = tk.Entry(modify_window)
            new_address_entry.grid(row=4, column=1, padx=10, pady=10)
            new_address_entry.insert(3, current_address)

            tk.Label(modify_window, text="Enter Year Level: ").grid(row=5, column=0, padx=10, pady=10)
            new_year_level_entry = tk.Entry(modify_window)
            new_year_level_entry.grid(row=5, column=1, padx=10, pady=10)
            new_year_level_entry.insert(4, current_year_level)

            tk.Label(modify_window, text="Enter New Course: ").grid(row=6, column=0, padx=10, pady=10)
            new_course_entry = tk.Entry(modify_window)
            new_course_entry.grid(row=6, column=1, padx=10, pady=10)
            new_course_entry.insert(5, current_course)

            # when the save button is clicked, it retrieves all the data that is modified
            save_button = tk.Button(modify_window, text="Save", command=lambda:
                                                                self.save_modifications(student_id,
                                                                                        new_first_name_entry.get(),
                                                                                        new_last_name_entry.get(),
                                                                                        new_age_entry.get(),
                                                                                        new_address_entry.get(),
                                                                                        new_course_entry.get()))
            save_button.grid(row=7, column=0, columnspan=2, pady=10)

        else:
            messagebox.showerror("Error", "Please select student to modify")  # this will be executed if there is no student selected

    @staticmethod
    # function definition for saving the modification with a parameter of the new data
    def save_modifications(student_id, new_first_name, new_last_name, new_age, new_address, new_course):
        with open('../Files/students.txt', 'r') as file:  # opens the file in read mode
            lines = file.readlines()  # reads the data in each line that stores them as a list

        for i, line in enumerate(lines):  # iterates through each line list
            # using the enumerating to get the indexes of each data in a line
            if line.startswith(student_id):  # this checks if the data in a line starts with a student id
                student_data = line.strip().split(',')  # if student id matches, it removes the whitespaces and splits tem using comma
                # this updates the data based on the indexes where the data is located, and then joins them using comma
                student_data[1] = new_first_name
                student_data[2] = new_last_name
                student_data[3] = new_age
                student_data[4] = new_address
                student_data[6] = new_course
                lines[i] = ','.join(student_data) + '\n'

        with open('../Files/students.txt', 'w') as file:  # this opens the students.txt file as written mode
            file.writelines(lines)  # this writes the new data based on the line the data located

        messagebox.showinfo("Success", "Modifications saved successfully")  # this shows
        # that the modifications are successful
        file.close()  # this close the file
