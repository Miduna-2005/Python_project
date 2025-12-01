#import tkinter
import tkinter as tk
from tkinter import *
#from tkinter import ttk #represents manually
root=tk.Tk()
root.title("Python Tkinter App")
root.geometry("600x400")
label=tk.Label(root,text="Hello World! This is Tkinter App").pack()
#dont create extra variables for grid just use
#label.grid(column=0,row=0)
root.mainloop()
#should no name as tkinter.py it will show attribute error so save other than tkinter.py