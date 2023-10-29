# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 14:20:34 2023

@author: sagou
"""

from Class_Files import C_File
from print_sagou import *
import os

class Menu:
    " classe générique de gestion de menu"

    def __init__(self, L=[], menu_index = 0):
        self.list = L
        self.menu_index = menu_index
        self.ch = None
        self.returned_value = ""

    def print_menu(self):
        print('')
        if self.list != []:
            for i in range(len(self.list)):
                print(i + 1, " : ", self.list[i], "\n")
            return self.choice()
        else:
            if self.get_menu_db(self.menu_index):
                self.print_menu()

    def choice(self):
        while True:
            try:
                i = int(input("Selon votre choix taper un nombre entre 1 et " + str(len(self.list)) + " -->  "))
                assert i >= 1 and i <= len(self.list)
            except ValueError:
                print("! Veuillez saisir un nombre entier.\n")
            except AssertionError:
                print("! Le nombre saisi doit être supérieur ou égal à 1 et inférieur ou égal à " + str(
                    len(self.list)) + ".\n")
            else:
                self.ch = i
                self.returned_value = self.list[i-1]
                return i


    def get_menu_db(self, menu_id):
        menuFichier = C_File('db/menu.txt', sep=";")
        menu = menuFichier.existe_element_fichier3(str(menu_id))
        if menu[0]:
            L = menuFichier.str_to_liste(menu[1].replace('\n', ''))
            self.list = L[1:] + ['Retour', 'Quitter']
            return True
        else:
            print_error("WE CANNOT FIND THE MENU")
            return False


