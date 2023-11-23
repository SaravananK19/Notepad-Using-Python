import tkinter as tk
from tkinter import filedialog #provide dialog boxes for file related operation

class Notepad(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)#setting up initial configuration for the notepad window

        # Set the title for the notepad
        self.title("Notepad")

        # Create a text widget
        self.text = tk.Text(self, wrap="word")
        self.text.pack(side="top", fill="both", expand=True)

        # Create a menu bar
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        # Create a file menu
        file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=file_menu) #cascade- use to add a sub-menu. "File"  is submenu of menu cls.
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        # Create an edit menu
        edit_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)

    def new_file(self): #when new is selected it clear the text widgets and set title to Nodepad
        self.text.delete("1.0", "end")
        self.title("Notepad")

    def open_file(self):
        file = filedialog.askopenfile(parent=self, mode="rb", title="Open a file")
        if file:
            contents = file.read()
            self.text.delete("1.0", "end")
            self.text.insert("1.0", contents)
            file.close()
            self.title(file.name + " - Notepad")

    def save_file(self):
        file = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file:
            contents = self.text.get("1.0", "end")
            file.write(contents)
            file.close()
            self.title(file.name + " - Notepad")

    def cut(self):
        self.text.event_generate("<<Cut>>")

    def copy(self):
        self.text.event_generate("<<Copy>>")

    def paste(self):
        self.text.event_generate("<<Paste>>")

if __name__ == "__main__":
    notepad = Notepad()
    notepad.mainloop() #starts the tkinter main loop using mainloop() method
