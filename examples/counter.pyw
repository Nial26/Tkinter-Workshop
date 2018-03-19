import tkinter as tk

root = tk.Tk()
root.title("Clicker Counter")
root.geometry("400x300")

data = tk.StringVar()
data.set("0")

def count_up():
    global var
    num = int(data.get())
    data.set(str(num + 1))
    

def count_down():
    global var
    num = int(data.get())
    data.set(str(num - 1))

up = tk.Button(root, text = "+", command=count_up).grid(row = 0, column = 0)
point_label = tk.Label(root, textvariable = data).grid(row = 0, column = 1)
down = tk.Button(root, text = "-", command = count_down).grid(row = 0, column = 2)

root.mainloop()
