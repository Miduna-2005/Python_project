import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


entry_name = None
entry_password = None
combo_department = None


def submit_form():
    name = entry_name.get()
    password = entry_password.get()
    dept = combo_department.get()

    if name == "":
        messagebox.showerror("Error", "Name cannot be empty!")
    elif password == "":
        messagebox.showerror("Error", "Password cannot be empty!")
    elif dept == "Select Department":
        messagebox.showerror("Error", "Please choose a department!")
    else:
        messagebox.showinfo("Success",
                            f"Name: {name}\nDepartment: {dept}\nForm Submitted Successfully!")


# ---------- UI Window ----------
root = tk.Tk()
root.title(" Tkinter Form")
root.geometry("500x400")
root.configure(bg="#F0F4FF")   # Light blue background

# ---------- Heading ----------
title_label = Label(root,
                    text="User Registration Form",
                    font=("Arial", 18, "bold"),
                    bg="#F0F4FF",
                    fg="#003366")
title_label.pack(pady=15)

# ---------- Form Frame ----------
form_frame = Frame(root, bg="#F0F4FF")
form_frame.pack(pady=10)

# ---------- Name Entry ----------
Label(form_frame, text="Name :", font=("Arial", 12), bg="#F0F4FF").grid(row=0, column=0, padx=10, pady=10)
entry_name = Entry(form_frame, width=25, font=("Arial", 12), bg="#FFFFFF")
entry_name.grid(row=0, column=1, padx=10, pady=10)

# ---------- Password Entry ----------
Label(form_frame, text="Password :", font=("Arial", 12), bg="#F0F4FF").grid(row=1, column=0, padx=10, pady=10)
entry_password = Entry(form_frame, width=25, font=("Arial", 12), show="*", bg="#FFFFFF")
entry_password.grid(row=1, column=1, padx=10, pady=10)

# ---------- Combo Box ----------
Label(form_frame, text="Department :", font=("Arial", 12), bg="#F0F4FF").grid(row=2, column=0, padx=10, pady=10)

combo_department = ttk.Combobox(form_frame,
                                values=["Select Department", "CSE", "IT", "ECE", "EEE", "AIML", "Civil", "Mechanical"],
                                state="readonly",
                                width=22,
                                font=("Arial", 11))
combo_department.current(0)
combo_department.grid(row=2, column=1, padx=10, pady=10)

# ---------- Submit Button ----------
submit_btn = Button(root,
                    text="Submit",
                    font=("Arial", 12, "bold"),
                    bg="#4CAF50",      # Green
                    fg="white",
                    width=12,
                    command=submit_form)
submit_btn.pack(pady=20)

root.mainloop()
