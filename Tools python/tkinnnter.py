import tkinter as tk
from tkinter import Entry

root = tk.Tk()
def clicked():
    res = ("welcome " + text.get())
    label2 = tk.Label(root, text=res, fg="blue")
    label2.pack()


root.title("hello")
root.geometry("400x200")
label1 = tk.Label(root, text="test")
but1 = tk.Button(root, text="click", fg="red", command=clicked)


text = Entry(root, text="input nama")

text.pack()
but1.pack()
label1.pack()
root.mainloop()