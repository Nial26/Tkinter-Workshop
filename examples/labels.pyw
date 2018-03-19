import tkinter

root = tkinter.Tk() 
root.title("Labels Example") #Set the title of the Window
root.geometry("400x300") #Set the default geometry of the Window
label = tkinter.Label(root, text="Hello World!") 
label.pack()

root.mainloop()