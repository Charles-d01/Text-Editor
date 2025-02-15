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
openbutton = tk.Button(root, text="Open", comand= open_file())
openbutton.pack()

Save_button = tk.Button(root, text="Save", command= save_file())
Save_button.pack()
exitbutton = tk.Button(root, text="Exit", command=root.quit)
exitbutton.pack()

root.mainloop()
