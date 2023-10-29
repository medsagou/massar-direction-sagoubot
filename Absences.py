import sys
import time
from print_sagou import *
import pandas as pd
from io import StringIO
from Menu import Menu

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Absence:
    def __init__(self, driver="",  class_name_to_extract="", date = ""):
        self.driver = driver
        self.class_name_to_extract = class_name_to_extract
        self.date = date

    def get_list_page(self):
        try:
            self.driver.get("https://massar.men.gov.ma/Evaluation/Absence/AbsenceJournaliereParClasse")
        except:
            print_error("We Can't find the list page! Close the program and try again.")
        else:
            print_info("GETTING TO THE LIST PAGE")

    def get_classes_from_classes_page(self):
        return

    def list_of_each_class(self):
        searchBtn = self.driver.find_element(By.CSS_SELECTOR, "#search > div > div > div > div.box-body > div.blocBtn > button")

        TypeEnseignement = self.driver.find_element(By.ID, "TypeEnseignement")
        TypeEnseignement_all_options = TypeEnseignement.find_elements(By.TAG_NAME, "option")
        TypeEnseignement_Select = Select(TypeEnseignement)

        for TypeEnseignement_option in TypeEnseignement_all_options:
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.invisibility_of_element_located(
                        (
                            By.ID, "loadingDiv",
                        )
                    )
                )
            except:
                print_error("CHECK YOUR INTERNET CONNECTION THEN TRY AGAIN")
            TypeEnseignement_Select.select_by_value(TypeEnseignement_option.get_attribute("value"))

            Cycle = self.driver.find_element(By.ID, "Cycle")
            Cycle_all_options = Cycle.find_elements(By.TAG_NAME, "option")

            Cycle_Select = Select(Cycle)

            for Cycle_option in Cycle_all_options:
                if Cycle_option.text != "":
                    Cycle_Select.select_by_value(Cycle_option.get_attribute("value"))
                    Niveau = self.driver.find_element(By.ID, "Niveau")
                    Niveau_all_options = Niveau.find_elements(By.TAG_NAME, "option")
                    Niveau_Select = Select(Niveau)

                    for Niveau_option in Niveau_all_options:
                        if Niveau_option.text != "":
                            Niveau_Select.select_by_value(Niveau_option.get_attribute("value"))

                            Classe = self.driver.find_element(By.ID, "Classe")
                            Classe_all_options = Classe.find_elements(By.TAG_NAME, "option")
                            Classe_Select = Select(Classe)

                            for Classe_option in Classe_all_options:
                                if Classe_option.text != "":
                                    date = self.driver.find_element(By.ID, "Jour")
                                    date.send_keys(Keys.CONTROL + "a")
                                    date.send_keys(Keys.DELETE)
                                    date.send_keys("23-10-2023")
                                    Classe_Select.select_by_value(Classe_option.get_attribute("value"))
                                    searchBtn.click()
                                    try:
                                        WebDriverWait(self.driver, 3).until(
                                            EC.invisibility_of_element_located(
                                                (
                                                    By.ID, "loadingDiv",
                                                )
                                            )
                                        )
                                    except:
                                        continue
                                    else:
                                        print_info("A CLASS PASSED")



        return



    def main_list_reader(self):
        self.get_list_page()
        self.list_of_each_class()
        return

