from Read_XLSB_File import Read_Db
# import openpyxl
from utilities import get_columns_for_two

class Scan_Absences(Read_Db):

    def __init__(self, classe = "",  starter_col="B", ending_col="B", starter_row=10, ending_row=""):
        super().__init__()
        self.starter_col = starter_col
        self.ending_col = ending_col
        self.starter_row = starter_row
        self.ending_row = ending_row
        self.workbook = self.get_workbook(self.output_file)
        self.classe = classe
        self.worksheet_class = ""
        self.classe_numbers = "AO6"
        self.scaned_area = ["B", "AZ"]

    def get_absence_day_per_student(self):
        sheet_names = self.workbook.sheetnames
        if self.classe in sheet_names:
            sheet = self.workbook[self.classe]
            start_row = 10
            end_row = int(sheet[self.classe_numbers].value) + start_row
            # print(end_row)
            area_values = {}
            start_date = sheet["T6"].value
            end_date = sheet["AE6"].value
            for row in range(start_row, end_row + 1):
                row_values = []
                for col in get_columns_for_two(start_column = self.scaned_area[0], end_column = self.scaned_area[-1], column_to_remove = "AB"):
                    cell_value = sheet[str(col) + str(row)].value
                    row_values.append(cell_value)
                area_values[row_values[0]] = row_values
            # print(area_values)
            return area_values, start_date, end_date
        return False, False, False

    def get_absence_day_per_student2(self):
        sheet_names = self.workbook.sheetnames
        if self.classe in sheet_names:
            sheet = self.workbook[self.classe]
            sheet_date = self.workbook['BaseSheet']
            start_row = 10
            end_row = int(sheet[self.classe_numbers].value) + start_row
            # print(end_row)
            area_values = {}
            start_date = sheet_date["T6"].value
            end_date = sheet_date["AE6"].value
            for row in range(start_row, end_row + 1):
                row_values = []
                for col in get_columns_for_two(start_column = self.scaned_area[0], end_column = self.scaned_area[-1], column_to_remove = "AB"):
                    cell_value = sheet[str(col) + str(row)].value
                    row_values.append(cell_value)
                area_values[row_values[0]] = row_values
            # print(area_values)
            return area_values, start_date, end_date
        return False, False, False


