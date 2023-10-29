import pandas as pd
import openpyxl
from print_sagou import *


class Read_Db:
    def __init__(self, input_file = "db/file_data.xlsb", output = "db/Book1.xlsx", df = ""):
        self.index = {0: "CLASS_StudentIndex",
                      1: "Niveau",
                      2: "class_name",
                      3: "student_index",
                      4: "CNE",
                      5: "nom",
                      6: "prenom"}
        self.input_file = input_file
        self.output_file = output
        self.df = df
        self.init_cell = ["A"]
        self.start_col = 'A'
        self.end_col = 'C'

    def get_key(self, val):

        for key, value in self.index.items():
            if val == value:
                return key
        return "key doesn't exist"

    def get_data_from_xlsb(self):

        xlsb_file = pd.ExcelFile(self.input_file)
        df = xlsb_file.parse('Feuil3', header=None)  #
        # pd.set_option('display.max_rows', None)
        # pd.set_option('display.max_columns', None)
        # print(df)
        # pd.reset_option('display.max_rows')
        # pd.reset_option('display.max_columns')
        self.df = df
        return df

    def get_workbook(self):
        workbook = openpyxl.load_workbook(self.output_file)
        return workbook

    def get_workbook_sheet(self, workbook ,sheet):
        return workbook[sheet]

    def add_value_to_sheet(self, workbook, cell, value):
        worksheet = self.get_workbook_sheet(workbook=workbook, sheet="Sheet4")
        cell_to_update = worksheet[cell]
        cell_to_update.value = value
        workbook.save(self.output_file)
        return


    def create_copy_sheet(self, class_name = "", workbook = "", source_sheet = ""):
        new_sheet = workbook.copy_worksheet(source_sheet)
        new_sheet.title = class_name
        return


    def get_column_list_from_df(self, column_key):
        if self.df == "":
            self.get_data_from_xlsb()

        L = list(set(self.df.values[:, column_key].tolist()))
        try:
            L.remove("0")
        except ValueError:
            pass
        try:
            L.remove(0)
        except ValueError:
            pass
        return L

    def create_all_class_sheet(self):
        classes_list = self.get_column_list_from_df(column_key=self.get_key("class_name"))
        workbook = openpyxl.load_workbook(self.output_file)
        source_sheet = workbook["BaseSheet"]
        for classe in classes_list:
            print_info(f"CREATE A SHEET FOR {classe} CLASS")
            if classe != "":
                self.create_copy_sheet(class_name=classe, workbook=workbook, source_sheet = source_sheet)

        workbook.save(self.output_file)
        workbook.close()
        return

    def fill_all_class_sheets(self):
        self.create_all_class_sheet()
        if str(self.df) == "":
            self.get_data_from_xlsb()

        for row in self.df.values:
            for col in range(ord(self.start_col), ord(self.end_col) + 1):
                print(row, chr(col))

        return
# db = Read_Db()
# db.get_data_from_xlsb()
# print(db.get_classes_list_from_df())
# db.fill_all_class_sheets()


