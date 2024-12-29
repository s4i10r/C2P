"""
program to display csv files in a readable pdf
"""

from tkinter import Tk
from tkinter import Label, Button, Frame, filedialog
import conversion

root = Tk()
root.title("C2P")
root.geometry("700x600")


# class is neccessary to keep the filename without global
class CSV():
    def __init__(self):
        pass



def convert_file(filepath: str):
    # create an instance to an pdf file
    pdf = conversion.PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=8)
    pdf.create_table(filepath)
    return pdf.output("output.pdf", "F")

def select_file():
    file = filedialog.askopenfilename(
            title="Select a file",
            filetypes=(("CSV Files", "*.csv"),("All Files", "*.*")))
    if file:
        file_path_label.config(text=f"Selected file: {file}")
    
    global filepath
    filepath = file

    return None

filepath: str = str()

content_frame = Frame(root, pady=10)
content_frame.pack(anchor="center")


title = Label(content_frame, text="CSV to PDF Converter", font=("Arial", 22))
title.pack()

select_button = Button(content_frame, text="select a file", command=select_file,
                            width=50, height=20)
select_button.pack(pady=20)


file_path_label = Label(content_frame, text="No selected file")

convert_button = Button(content_frame, text="CONVERT TO PDF", command=convert_file(filepath))
convert_button.pack()

root.mainloop()
