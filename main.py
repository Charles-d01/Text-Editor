import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

root.title("Text Editor")
root.wm_iconbitmap("Icon.ico")

def new_file():
    messagebox.delete("1.0", "end")

def open_file():
    file_name = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")], title = "Open File")
    if file_name:
        with open(file_name, "r") as file:
            messagebox.delete("1.0", "end")
            messagebox.insert("1.0", file.read())


def save_file():
    save_as_file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")], title = "Save File as")
    if save_as_file_name:
        with open(save_as_file_name, "w") as file:
            file.write(messagebox.get("1.0", "end-1c"))
    
def exit():
    root.quit()


messagebox = tk.Text(root, height=50, width=150)
messagebox.pack()

# add the buttons after this part, dont touvh the code above
#for the command= part of all buttons, name them accordingly,
# new_file, open_file, save_file, exit_app

root.mainloop()
