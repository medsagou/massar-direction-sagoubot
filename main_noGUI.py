import sys

from Interaction_browser import Massar_Direction_Sagou
from absence_app import Absence
from utilities import User_Interface
from absence_app import Read_Db


def main():
    ui = User_Interface()

    # main menu
    while True:
        # ui.clear_screen()
        main_choice_1, main_choice_1_value = ui.main_menu()
        if str(main_choice_1) == "1":
            while True:
                ui.clear_screen()
                choice01, choice01_value = ui.menu01()
                if str(choice01) == "1":
                    reader = Read_Db()
                    reader.fill_all_class_sheets()

                elif str(choice01) == "2":
                    choice02, choice02_value = ui.menu_valider()
                    if str(choice02) == "1":
                        interaction_object = Massar_Direction_Sagou()
                        interaction_object.main_interaction()
                        interaction_object.get_list_page()
                        absence = Absence(driver=interaction_object.driver)
                        absence.main_absence_loop()

                    elif str(choice02_value) == "Retour":
                        ui.clear_screen()
                        break
                    elif str(choice02_value) == "Quitter":
                        ui.clear_screen()
                        sys.exit()

                elif str(choice01_value) == "Retour":
                    ui.clear_screen()
                    break
                elif str(choice01_value) == "Quitter":
                    ui.clear_screen()
                    sys.exit()

        elif str(main_choice_1_value) == "Retour":
            ui.clear_screen()
            break
        elif str(main_choice_1_value) == "Quitter":
            ui.clear_screen()
            sys.exit()

if __name__ == "__main__":
    main()