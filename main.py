import tkinter as tk

root = tk.Tk()

root.title("Text Editor")

def save_file():
    with open("text.txt", "w") as file:
        file.write(messagebox.get("1.0", "end-1c"))


messagebox = tk.Text(root, height=10, width=50)
messagebox.pack()


Save_button = tk.Button(root, text="Save", command= save_file())
