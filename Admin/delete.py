import tkinter as tk
from tkinter import messagebox
from DisplayStudents.display_students import DisplayStudents


class Delete(DisplayStudents):  # this class inherits a DisplayStudents
    def __init__(self, master6):  # defines a method for the Delete class which takes master6 as an argument
        self.master6 = master6
        super().__init__(master6)  # calls the constructor from DisplayStudents using the super() function
        master6.title("Delete Student Data")

        self.delete_button = tk.Button(master6, text="Delete", command=self.delete_student, font=("Arial", 8),
                                       width=27, height=2)
        self.delete_button.pack(padx=10, pady=10)

    def delete_student(self):  # defines a function method for deleting students data
        selected_index = self.search_results_treeview.focus()  # this retrieves the index of the currently selected item in search result treeview
        if selected_index:  # checks if an item is selected
            selected_student_id = self.search_results_treeview.item(selected_index, "text")  # this retrieves the text(student ID)
            # of the selected item

            # this messagebox asks the user whether to confirm the deletion of data or not
            confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure to delete student{selected_student_id}")
            if confirm:  # check if the user confirms the deletion
                # in this code block, it is the method to attempt to open the data files
                try:
                    with open('../Files/students.txt', 'r') as file:  # opens the students.txt file as read
                        lines = file.readlines()  # this read the data in each line
                    with open('../Files/students.txt', 'w') as file:  # opens the students.txt file as write
                        for line in lines:  # iterate through each line
                            if not line.startswith(selected_student_id):  # this checks
                                # if the data starts in student ID and if yes
                                file.write(line)  # this rewrites the data in the line
                                # meaning it will now delete the student's data
                    self.search_results_treeview.delete(selected_index)  # this deletes the data based on the selected index
                    messagebox.showinfo("Success", "Student deleted successfully")  # if deleted successfully,
                    # this message box will execute
                except FileNotFoundError:  # this catches the error if the student data not found in the file
                    messagebox.showerror("Error", "Student data not found.")
            else:
                messagebox.showerror("Error", "Please select a student to delete")  # this will prompt the user
                # to select the students to delete,
                # if there's no student data has been selected
