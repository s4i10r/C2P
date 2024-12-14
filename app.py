"""
program to display csv files in a readable pdf
"""

from tkinter import Tk, Label, Button

root = Tk()
root.title("C2P")
root.geometry("700x600")

def convert():
    print("...°°°...°°°...")



title = Label(root, text="CSV to PDF Converter", font=("Arial", 22))

title.pack()



convert_button = Button(root, text="CONVERT TO PDF", command=convert)
convert_button.grid(row=3, column=0)
convert_button.pack()


root.mainloop()
