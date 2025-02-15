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
    
def exit_app():
    root.quit()


file_menu = tk.Menu(root)
root.config(menu=file_menu)
file_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)


messagebox = tk.Text(root, height=10, width=50)
messagebox.pack()

# add the buttons after this part, dont touvh the code above
#for the command= part of all buttons, name them accordingly,
# new_file, open_file, save_file, exit_app

button_new = tk.Button(root, text="New", command=new_file)

button_open = tk.Button(root, text="Open", command=open_file)

button_save = tk.Button(root, text="Save", command=save_file)

button_exit = tk.Button(root, text="Exit", command=exit)


root.mainloop()
