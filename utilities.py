import string
from datetime import datetime, timedelta
from print_sagou import *

def get_columns_for_two(start_column = "", end_column = "", column_to_remove = ""):
    column_names = []
    for letter1 in string.ascii_uppercase:
        if letter1 >= start_column:
            column_names.append(letter1)
    for letter1 in string.ascii_uppercase:
        for letter2 in string.ascii_uppercase:
            ch = letter1 + letter2
            if ch == end_column:
                column_names.append(ch)
                if column_to_remove != "":
                    column_names.remove(column_to_remove)
                return column_names
            else:
                column_names.append(ch)



def get_date_list():
    while True:
        start_date_str = input("Entrer La date de depart (DD-MM-YYYY): ")
        end_date_str = input("Entrer la date finale (DD-MM-YYYY): ")
        start_date = datetime.strptime(start_date_str, '%d-%m-%Y')
        end_date = datetime.strptime(end_date_str, '%d-%m-%Y')
        date_list = []
        current_date = start_date
        while current_date <= end_date:
            date_str = current_date.strftime('%d-%m-%Y')
            date_list.append(date_str)
            current_date += timedelta(days=1)
        if len(date_list) != 6:
            print_error("LES DATE QUI VOUS AVEZ INSERER N'EST PAS VALIDE")
            continue
        else:
            return date_list


