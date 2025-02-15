import tkinter as tk

root = tk.Tk()

root.title("Text Editor")
root.wm_iconbitmap("Icon.ico")

def save_file():
    with open("text.txt", "w") as file:
        file.write(messagebox.get("1.0", "end-1c"))

def open_file():
    with open("text.txt", "r") as file:
        messagebox.insert("1.0", file.read())


messagebox = tk.Text(root, height=50, width=150)
messagebox.pack()

# add the buttons after this part, dont touvh the code above
#for the command= part of all buttons, name them accordingly,
# new_file, open_file, save_file, exit_app

button_new = tk.Button(root, text="New", command=new_file)

button_open = tk.Button(root, text="Open", command=open_file)

button_save = tk.Button(root, text="Save", command=save_file)

button_exit = tk.Button(root, text="Exit", command=exit_app)
root.mainloop()
