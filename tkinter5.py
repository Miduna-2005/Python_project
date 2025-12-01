import tkinter as tk
from tkinter import messagebox

def on_click():
    messagebox.showinfo("Information", "Button Clicked!")

root = tk.Tk()
root.title("Python Tkinter App")
root.geometry("600x400")

label = tk.Label(root, text="Hello World! This is Tkinter App")
label.grid(row=0, column=0, columnspan=4, pady=10)

rd1 = tk.Radiobutton(root, text="Option 1", value=1)
rd2 = tk.Radiobutton(root, text="Option 2", value=2)
rd1.grid(row=1, column=0)
rd2.grid(row=1, column=1)

btn = tk.Button(root, background="red", foreground="white", text="Click Me", command=on_click)
btn.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
