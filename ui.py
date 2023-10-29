from print_sagou import *
from Menu import  Menu

import os


class User_Interface:

    def clear_screen(slef):
        os.system('cls' if os.name == 'nt' else 'clear')


    def main_page(self, Class_Dict):
        print("Votre Classes :")
        print("{:<12} {:<12}".format("Class", "Nombre des etudiants"))
        print_dict(Class_Dict)
        return

    def main_menu(self):
        start_menu = Menu(menu_index = "0")
        start_menu.print_menu()
        return (start_menu.ch, start_menu.returned_value)

    def menu01(self):
        menu01 = Menu(menu_index = "01")
        menu01.print_menu()
        return (menu01.ch, menu01.returned_value)

    def classes_menu(self):
        class_menu = Menu(menu_index="001")
        class_menu.print_menu()
        return (class_menu.ch, class_menu.returned_value)
