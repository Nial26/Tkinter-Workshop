import tkinter as tk

root = tk.Tk()
root.title("Buttons Example")
root.geometry("400x300")

b1 = tk.Button(root, text = "Button 1")
b2 = tk.Button(root, text = "Button 2")

b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)

root.mainloop()