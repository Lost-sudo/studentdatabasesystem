import tkinter as tk
from tkinter import ttk  # for treeview
from tkinter import messagebox


class DisplayStudents:
    def __init__(self, master2):  # initializes the instance of a class
        self.master2 = master2  # the parent of a window
        master2.title("Search and Display Student")

        # GUI elements
        self.search_label = tk.Label(master2, text="Enter search keyword", font=("Arial", 10, 'bold'))
        self.search_label.grid(row=0, column=0, padx=10, pady=10)
        self.search_entry = tk.Entry(master2)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10)

        self.search_button = tk.Button(master2, text="Search", font=("Arial", 10, 'bold'), command=lambda: self.search_students(self.search_entry.get()))
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

    # Definition for search_students from the search_button
    def search_students(self, keyword):
        for item in self.search_results_treeview.get_children():  # retrieves the search keyword entered by the user
            self.search_results_treeview.delete(item)  # clears any existing data in the treeview

        try:
            with open('../Files/students.txt', 'r') as file:  # opens the students.txt file in read mode
                data_found = False  # a flag used to indicate whether any matching data is found,
                # set to false before attempting to search data in a file
                for line in file:  # loops through each line in a file
                    if keyword.lower() in line.lower():  # checks if the lowercase version of the keyword exists
                        student_data = line.strip().split(',')  # line.strip() removes any leading or trailing whitespaces
                        # split() splits the line into a list of strings using comma as delimiter
                        student_id = student_data.pop(0)  # removes and returns the first element of the student data list which is the student id
                        # inserts a new item into the Treeview
                        # "" this indicates the item will be inserted at the root level of the tree
                        # tk.END specifies that the new item will be inserted at the end of the tree
                        self.search_results_treeview.insert("", tk.END, text=student_id, values=student_data)
                        data_found = True  # if matching data is found, data_found flag sets to true
                if not data_found:  # if no matching data found, this block of code will be executed indicating that there's not data found
                    messagebox.showinfo("No Data", f"No Data found for {keyword}")
        except FileNotFoundError:  # if there's no file containing the data of students found, this will be executed
            messagebox.showerror("Error", "Student Data Not Found")
