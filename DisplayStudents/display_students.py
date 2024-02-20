import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class DisplayStudents:
    def __init__(self, master2):
        self.master2 = master2
        master2.title("Search and Display Student")

        self.search_label = tk.Label(master2, text="Enter search keyword")
        self.search_label.grid(row=0, column=0, padx=10, pady=10)
        self.search_entry = tk.Entry(master2)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10)

        self.search_button = tk.Button(master2, text="Search", command=lambda: self.search_students(self.search_entry.get()))
        self.search_button.grid(row=0, column=2, padx=10, pady=10)

        self.search_results_treeview = ttk.Treeview(master2, height=10, columns=("First Name", "Last Name", "Age",
                                                                                 "Address", "Year Level", "Course"))
        self.search_results_treeview.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Format column headings
        self.search_results_treeview.heading("#0", text="Student ID")
        self.search_results_treeview.heading("First Name", text="First Name")
        self.search_results_treeview.heading("Last Name", text="Last Name")
        self.search_results_treeview.heading("Age", text="Age")
        self.search_results_treeview.heading("Address", text="Address")
        self.search_results_treeview.heading("Year Level", text="Year Level")
        self.search_results_treeview.heading("Course", text="Course")

        column_widths = {"#0": 100, "First Name": 100, "Last Name": 100, "Age": 30, "Address": 250, "Year Level": 60,
                         "Course": 250}
        for column, width in column_widths.items():
            self.search_results_treeview.column(column, width=width)

    def search_students(self, keyword):
        for item in self.search_results_treeview.get_children():
            self.search_results_treeview.delete(item)

        try:
            with open('../Files/students.txt') as file:
                data_found = False
                for line in file:
                    if keyword.lower() in line.lower():
                        student_data = line.strip().split(',')
                        student_id = student_data.pop(0)
                        self.search_results_treeview.insert("", tk.END, text=student_id, values=student_data)
                        data_found = True
                if not data_found:
                    messagebox.showinfo("No Data", f"No Data found for {keyword}")
        except FileNotFoundError:
            messagebox.showerror("Error", "Student Data Not Found")
