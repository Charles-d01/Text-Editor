import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

root.title("Text Editor")
root.wm_iconbitmap("Icon.ico")

def new_file():
    text_area.delete("1.0", "end")

def open_file():
    file_name = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")], title = "Open File")
    if file_name:
        with open(file_name, "r") as file:
            text_area.delete("1.0", "end")
            text_area.insert("1.0", file.read())


def save_file():
    save_as_file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")], title = "Save File as")
    if save_as_file_name:
        with open(save_as_file_name, "w") as file:
            file.write(text_area.get("1.0", "end-1c"))
    
def exit_app():
    root.quit()

menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
root.config(menu=menubar)

main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill='both', padx=5, pady=5)


text_area = tk.Text(main_frame, height=10, width=50)
text_area.pack()

# add the buttons after this part, dont touvh the code above
#for the command= part of all buttons, name them accordingly,
# new_file, open_file, save_file, exit_app

button_new = tk.Button(main_frame, text="New", command=new_file)
button_new.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
button_open = tk.Button(main_frame, text="Open", command=open_file)
button_open.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
button_save = tk.Button(main_frame, text="Save", command=save_file)
button_save.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
button_exit = tk.Button(main_frame, text="Exit", command=exit_app)
button_exit.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

main_frame.grid_rowconfigure(0, weight=1)
for i in range(4):
    main_frame.grid_columnconfigure(i, weight=1) 

root.mainloop()
