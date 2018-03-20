import tkinter as tk
import time

root = tk.Tk()
root.title("Mutable Variables V2")
root.geometry("400x300")

text_data = tk.StringVar()
text_data.set("Hello There") #All the variable wrappers provide set and get methods to mutate and access the data
hello_label = tk.Label(root, textvariable = text_data) #Notice that text_data is assigned to textvariable not text
hello_label.pack()
tk.Button(root, text = "Change Text", command = text_data.set("Text Changed")) #don't really care of the command is set to None here

root.mainloop()