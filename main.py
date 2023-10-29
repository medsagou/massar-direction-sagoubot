from interaction import Massar_Sagou
from list_reader import List_Reader
from Absences import Absence
from ui import User_Interface
import os

def main():
    interaction_object = Massar_Sagou()
    interaction_object.main_interaction()

    ui = User_Interface()
    # ui.main_page(interaction_object.get_classes_from_main_page())

    # main menu
    while True:
        # ui.clear_screen()
        list_reader_by_class = Absence()
        list_reader_by_class.driver = interaction_object.driver
        list_reader_by_class.main_list_reader()

        main_choice_1, main_choice_1_value = ui.main_menu()

        if str(main_choice_1) == "1":
            while True:
                ui.clear_screen()
                choice01, choice01_value = ui.menu01()
                if str(choice01) == "1":
                    ui.clear_screen()
                    choice001, classe_name = ui.classes_menu()
                    if str(classe_name) == "Retour":
                        ui.clear_screen()
                        break
                    elif str(classe_name) == "Quitter":
                        ui.clear_screen()
                        interaction_object.exit_program()
                    else:
                        list_reader_by_class = List_Reader(class_name_to_extract=classe_name)
                        list_reader_by_class.driver = interaction_object.driver
                        list_reader_by_class.main_list_reader()

                elif str(choice01) == "2":
                    ui.clear_screen()
                    list_reader = List_Reader()
                    list_reader.driver = interaction_object.driver
                    list_reader.main_list_reader()
                    break
                elif str(choice01_value) == "Retour":
                    ui.clear_screen()
                    break
                elif str(choice01_value) == "Quitter":
                    ui.clear_screen()
                    interaction_object.exit_program()

        elif str(main_choice_1_value) == "Retour":
            ui.clear_screen()
            break
        elif str(main_choice_1_value) == "Quitter":
            ui.clear_screen()
            interaction_object.exit_program()

if __name__ == "__main__":
    main()