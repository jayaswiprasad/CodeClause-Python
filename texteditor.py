import tkinter as tk

# root = tk.Tk()
# root.title("Text Editor")

# # Create the text widget
# text_widget = tk.Text(root)
# text_widget.pack(fill=tk.BOTH, expand=1)

# # Run the main loop
# root.mainloop()

# Create the window
root = tk.Tk()
root.title("Text Editor")

# Create the text widget
text_widget = tk.Text(root)
text_widget.pack(fill=tk.BOTH, expand=1)

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create the file menu
file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add the "Open" command to the file menu
def open_file():
    file_path = tk.filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as f:
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, f.read())
file_menu.add_command(label="Open", command=open_file)

# Add the "Save" command to the file menu
def save_file():
    file_path = tk.filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as f:
            f.write(text_widget.get(1.0, tk.END))
file_menu.add_command(label="Save", command=save_file)

# Add a separator to the file menu
file_menu.add_separator()

# Add the "Exit" command to the file menu
def exit_editor():
    root.destroy()
file_menu.add_command(label="Exit", command=exit_editor)

# Run the main loop
root.mainloop()
