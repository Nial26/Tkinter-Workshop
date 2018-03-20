import tkinter as tk

def create_window(parent = None):
    window = tk.Toplevel(parent)
    window.title("New Window")
    window.geometry("400x300")
    tk.Button(window, text = "New Window!", command = lambda: create_window(window)).pack() #Experminet out with passing and not passing the window as a parent paramter here to understand the significance of it.            
    tk.Button(window, text = "Destroy this window", command = lambda: destroy_window(window)).pack()

def destroy_window(window):
    window.destroy()


root = tk.Tk() #The Root window
root.title("Root Window")
root.geometry("400x300")
tk.Button(root, text = "New Window!", command = lambda: create_window()).pack()
tk.Button(root, text = "Destroy this window", command = lambda: destroy_window(root)).pack()
root.mainloop()