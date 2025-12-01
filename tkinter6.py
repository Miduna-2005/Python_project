import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import re   # for email validation

def on_click():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    selected = choice.get()
    department = combo_dept.get()

    # ----- Validation -----

    # Empty field check
    if name == "" or email == "" or password == "":
        messagebox.showwarning("Warning", "All fields are required!")
        return

    # Email validation using regex
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address!")
        return

    # Password validation
    if len(password) < 6:
        messagebox.showerror("Weak Password", "Password must be at least 6 characters!")
        return

    # Radio selection validation
    if selected == 0:
        messagebox.showwarning("Warning", "Please select an option!")
        return

    # Combobox validation
    if department == "Select Department":
        messagebox.showwarning("Warning", "Please choose your department!")
        return

    # Success message
    messagebox.showinfo(
        "Form Submitted",
        f"Name: {name}\nEmail: {email}\nDepartment: {department}\nOption: {selected}"
    )


# --------- MAIN WINDOW ----------
root = tk.Tk()
root.title("Tkinter Form")
root.geometry("550x600")
root.configure(bg="#F3F4F6")

# --------- Heading ----------
title_label = tk.Label(
    root,
    text="Tkinter Form",
    font=("Arial", 20, "bold"),
    bg="#F3F4F6",
    fg="#333333"
)
title_label.pack(pady=20)

# --------- Main Frame ----------
frame = tk.Frame(root, bg="white", bd=2, relief="solid")
frame.pack(pady=10, padx=20)

# --------- Name Entry ----------
name_label = tk.Label(frame, text="Enter Name:", font=("Arial", 12), bg="white")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

name_entry = tk.Entry(frame, font=("Arial", 12), width=25)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# --------- Email Entry ----------
email_label = tk.Label(frame, text="Enter Email:", font=("Arial", 12), bg="white")
email_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

email_entry = tk.Entry(frame, font=("Arial", 12), width=25)
email_entry.grid(row=1, column=1, padx=10, pady=10)

# --------- Password Entry ----------
password_label = tk.Label(frame, text="Password:", font=("Arial", 12), bg="white")
password_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

password_entry = tk.Entry(frame, font=("Arial", 12), width=25, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

# --------- ComboBox (Department) ----------
dept_label = tk.Label(frame, text="Department:", font=("Arial", 12), bg="white")
dept_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

combo_dept = ttk.Combobox(
    frame,
    values=["CSE", "IT", "ECE", "EEE", "MECH", "CIVIL", "AI&DS", "AI&ML"],
    font=("Arial", 12),
    state="readonly",
    width=22
)
combo_dept.set("Select Department")
combo_dept.grid(row=3, column=1, padx=10, pady=10)

# --------- Radio Buttons ----------
choice = tk.IntVar(value=0)

rb1 = tk.Radiobutton(frame, text="Option 1", value=1, variable=choice,
                     font=("Arial", 12), bg="white")
rb2 = tk.Radiobutton(frame, text="Option 2", value=2, variable=choice,
                     font=("Arial", 12), bg="white")

rb1.grid(row=4, column=0, padx=10, pady=10)
rb2.grid(row=4, column=1, padx=10, pady=10)

# --------- Submit Button ----------
btn = tk.Button(
    root,
    text="Submit",
    font=("Arial", 14, "bold"),
    bg="#2563EB",
    fg="white",
    width=12,
    height=1,
    command=on_click
)
btn.pack(pady=20)

root.mainloop()
