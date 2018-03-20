import tkinter as tk
import time

root = tk.Tk()
root.title("Mutable Variables V1")
root.geometry("400x300")

hello_label = tk.Label(root, text = "Hello!")
hello_label.pack()
tk.Button(root, text = "Change Text", command = lambda: hello_label.config(text = "Text Changed!")).pack()

root.mainloop()