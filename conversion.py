from fpdf import FPDF
import csv


class PDF(FPDF):
    def header(self):
        self.set_font("Arial")

    def footer(self):
        self.set_y(-20)
        self.set_font("Arial", "I", 0)
        self.cell(0, 10, f"Seite {self.page_no()}", 0, 0, "C")
    

    def create_table(self, filepath):
        with open(filepath, "r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            reader = list(reader)
            num_rows = len(reader)
            num_columns = len(reader[0])

            # get max width of each column for better formatting
            column_list = [[] for i in range(num_columns)]

            # for every row
            for i in range(num_rows):
                # check every entry
                for j in range(num_columns):
                    # first entry in first list, second in second, ...
                    column_list[j].append(reader[i][j])

            # create table
            for row in reader:
                runner = 0
                for entry in row:
                    # calculate cell width based on longest string + padding
                    self.cell(self.get_string_width(max(column_list[runner], key=len) + "10"), 10, entry, 1)
                    runner += 1
                # linebreak every row
                self.ln(10)


