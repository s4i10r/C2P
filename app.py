"""
program to display csv files in a readable pdf
"""

from tkinter import Tk
from tkinter import Label, Button, Frame, filedialog
import conversion

root = Tk()
root.title("C2P")
root.geometry("700x600")


# class is neccessary to keep track of the filename without using global
class FileSelector():
    def __init__(self, root):
        self.filepath = None


    
    def select_filepath(self):
        self.filepath = filedialog.askopenfilename(
            title="Select a file",
            filetypes=(("CSV Files", "*.csv"),("All Files", "*,*")))
        if self.filepath:
            file_path_label.config(text=f"Selected file: {self.filepath}")
            file_path_label.pack()
        else:
            raise Exception("File not found")
    

    def convert_file(self):
        pdf = conversion.PDF()
        pdf.add_page()
        pdf.set_font("Arial", size=8)
        pdf.create_table(self.filepath)
        return pdf.output("output.pdf", "F")

selector = FileSelector(root)


content_frame = Frame(root, pady=10)
content_frame.pack(anchor="center")


title = Label(content_frame, text="CSV to PDF Converter", font=("Arial", 22))
title.pack()

select_button = Button(content_frame, text="select a file", command=selector.select_filepath,
                            width=50, height=20)
select_button.pack(pady=20)


file_path_label = Label(content_frame, text="No selected file")

convert_button = Button(content_frame, text="CONVERT TO PDF", command=selector.convert_file)
convert_button.pack()

root.mainloop()
