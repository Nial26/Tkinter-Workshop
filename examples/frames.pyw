import tkinter as tk

root = tk.Tk()
root.title("Frame Example")
root.geometry("400x300")
f = tk.Frame(root) #The frame's parent is the root
hello_label = tk.Label(f, text = "Hello!") #The Parent of this label is not the root window, but frame f
bye_label = tk.Label(f, text = "Bye!") #As above

hello_label.pack()
bye_label.pack()
f.pack()

root.mainloop()