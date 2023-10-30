import string

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




