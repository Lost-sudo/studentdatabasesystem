import tkinter as tk
from tkinter import messagebox
from DisplayStudents.display_students import DisplayStudents


class Delete(DisplayStudents):
    def __init__(self, master6):
        self.master6 = master6
        super().__init__(master6)
        master6.title("Delete Student Data")

        self.delete_button = tk.Button(master6, text="Delete", command=self.delete_student)
        self.delete_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def delete_student(self):
        selected_index = self.search_results_treeview.focus()
        if selected_index:
            selected_student_id = self.search_results_treeview.item(selected_index, "text")
            confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure to delete student{selected_student_id}")
            if confirm:
                try:
                    with open('../Files/students.txt', 'r') as file:
                        lines = file.readlines()
                    with open('../Files/students.txt', 'w') as file:
                        for line in lines:
                            if not line.startswith(selected_student_id):
                                file.write(line)
                    self.search_results_treeview.delete(selected_index)
                    messagebox.showinfo("Success", "Student deleted successfully")
                except FileNotFoundError:
                    messagebox.showerror("Error", "Student data not found.")
            else:
                messagebox.showerror("Error", "Please select a student to delete")
