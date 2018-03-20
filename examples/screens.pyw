import tkinter as tk

root = tk.Tk()
root.title("Screens")
root.geometry("400x300")

main_frame = tk.Frame(root) #Create a main Frame

tk.Label(main_frame, text = "Main Frame").pack()

second_frame = tk.Frame(root) # Create a Secondary Frame
tk.Label(second_frame, text = "Second Frame").pack()
tk.Button(second_frame, text = "Go Back", command = main_frame.tkraise).pack() #Raise the main frame on button click

tk.Button(main_frame, text = "Go to 2nd Frame", command = second_frame.lift).pack() #Raise the second frame on button click

second_frame.grid(row = 0, column = 0, padx = 150, pady = 120,  sticky = "NSEW")
main_frame.grid(row = 0, column = 0, padx = 150, pady = 120,  sticky = "NSEW")

main_frame.lift()

root.mainloop()