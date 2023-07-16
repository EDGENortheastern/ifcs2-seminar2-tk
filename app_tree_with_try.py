import csv
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import datetime
import re

class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Register App")
        self.configure(bg="#FFC9F3")  # Set the background color
        
        self.name_var = tk.StringVar()
        self.name_label = tk.Label(self, text="Enter your full name:", bg="#FFC9F3")
        self.name_label.pack()
        
        self.name_entry = tk.Entry(self, textvariable=self.name_var)
        self.name_entry.pack()
        
        self.submit_button = tk.Button(self, text="Submit", command=self.validate_and_submit, bg="#FFC9F3", highlightbackground="#FFC9F3", highlightcolor="#FFC9F3")
        self.submit_button.pack()

        self.view_all_button = tk.Button(self, text="View All", command=self.view_all, bg="#FFC9F3", highlightbackground="#FFC9F3", highlightcolor="#FFC9F3")
        self.view_all_button.pack()

        self.treeview = ttk.Treeview(self, columns=("Name", "Timestamp"), show="headings")
        self.treeview.heading("Name", text="Name")
        self.treeview.heading("Timestamp", text="Timestamp")
        self.treeview.pack()
        
    def validate_and_submit(self):
        try:
            name = self.name_var.get()
            if not self.validate_name(name):
                raise ValueError("Invalid name. Please enter a name without numbers.")
            self.save_name(name)
            messagebox.showinfo("Success", "Name saved successfully")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def validate_name(self, name):
        return not bool(re.search(r'\d', name))
        
    def save_name(self, name):
        with open("names.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, datetime.datetime.now()])
            
    def view_all(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)  # Clear the treeview
        with open("names.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                self.treeview.insert("", tk.END, values=row)  # Insert each name and timestamp into the treeview

def capitalize_name(name):
    return name.title()

if __name__ == "__main__":
    app = Application()
    app.mainloop()


