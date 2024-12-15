"""
program to display csv files in a readable pdf
"""

from tkinter import Tk
from tkinter import Label, Button, Frame, filedialog

root = Tk()
root.title("C2P")
root.geometry("700x600")

#TODO: convert the csv
def convert_file():
    print("test")


def select_file():
    file = filedialog.askopenfilename(
            title="Select a file",
            filetypes=(("CSV Files", "*.csv"),("All Files", "*.*")))
    if file:
        file_path_label.config(text=f"Selected file: {file}")



content_frame = Frame(root, pady=10)
content_frame.pack(anchor="center")


title = Label(content_frame, text="CSV to PDF Converter", font=("Arial", 22))
title.pack()

select_button = Button(content_frame, text="select a file", command=select_file,
                            width=50, height=20)
select_button.pack(pady=20)


file_path_label = Label(content_frame, text="No selected file")

convert_button = Button(content_frame, text="CONVERT TO PDF", command=convert_file)
convert_button.pack()

root.mainloop()
