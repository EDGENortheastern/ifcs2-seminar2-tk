import csv
import tkinter as tk
from tkinter import messagebox
import datetime
import re
import unittest

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Name Collector")
        self.name_var = tk.StringVar()
        
        self.name_label = tk.Label(self, text="Enter Name:")
        self.name_label.pack()
        
        self.name_entry = tk.Entry(self, textvariable=self.name_var)
        self.name_entry.pack()
        
        self.submit_button = tk.Button(self, text="Submit", command=self.validate_and_submit)
        self.submit_button.pack()

        self.view_all_button = tk.Button(self, text="View All", command=self.view_all)
        self.view_all_button.pack()
        
    def validate_and_submit(self):
        name = self.name_var.get()
        if self.validate_name(name):
            self.save_name(name)
            messagebox.showinfo("Success", "Name saved successfully")
        else:
            messagebox.showerror("Error", "Invalid name. Please enter a name without numbers.")
            
    def validate_name(self, name):
        return not bool(re.search(r'\d', name))
        
    def save_name(self, name):
        with open("names.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, datetime.datetime.now()])
            
    def view_all(self):
        with open("names.csv", "r") as file:
            reader = csv.reader(file)
            names = [", ".join(row) for row in reader]
            names_string = "\n".join(names)
            messagebox.showinfo("Names", names_string)

def capitalize_name(name):
    return name.title()

class TestValidateName(unittest.TestCase):
    def test_validate_name(self):
        app = Application()
        
        self.assertTrue(app.validate_name("John Doe"))
        self.assertFalse(app.validate_name("John Doe2"))

if __name__ == "__main__":
    unittest.main(exit=False)
    app = Application()
    app.mainloop()

