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


class List_Reader:
    def __init__(self, driver="",  class_name_to_extract=""):
        self.driver = driver
        self.class_name_to_extract = class_name_to_extract


    def get_list_page(self):
        try:
            self.driver.get("https://massar.men.gov.ma/Evaluation/EspaceEnseignant/ListeEleves")
        except:
            print_error("We Can't find the list page! Close the program and try again.")
        else:
            print_info("GETTING TO THE LIST PAGE")

    def get_classes_from_classes_page(self):
        return

    def list_of_each_class(self):
        searchBtn = self.driver.find_element(By.ID, "btnSearch")

        TypeEnseignement = self.driver.find_element(By.ID, "TypeEnseignement")
        TypeEnseignement_all_options = TypeEnseignement.find_elements(By.TAG_NAME, "option")
        TypeEnseignement_Select = Select(TypeEnseignement)

        for TypeEnseignement_option in TypeEnseignement_all_options:
            TypeEnseignement_Select.select_by_value(TypeEnseignement_option.get_attribute("value"))

            Cycle = self.driver.find_element(By.ID, "Cycle")
            Cycle_all_options = Cycle.find_elements(By.TAG_NAME, "option")

            Cycle_Select = Select(Cycle)

            for Cycle_option in Cycle_all_options:
                Cycle_Select.select_by_value(Cycle_option.get_attribute("value"))

                Niveau = self.driver.find_element(By.ID, "Niveau")
                Niveau_all_options = Niveau.find_elements(By.TAG_NAME, "option")
                Niveau_Select = Select(Niveau)

                for Niveau_option in Niveau_all_options:
                    Niveau_Select.select_by_value(Niveau_option.get_attribute("value"))

                    Classe = self.driver.find_element(By.ID, "Classe")
                    Classe_all_options = Classe.find_elements(By.TAG_NAME, "option")
                    Classe_Select = Select(Classe)

                    for Classe_option in Classe_all_options:
                        if self.class_name_to_extract != "":
                            if self.class_name_to_extract == Classe_option.text:
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
                                   print_error("CHECK YOUR INTERNET CONNECTION THEN TRY AGAIN")
                                else:
                                    self.get_class_list(Classe_option.text)
                                    return
                            else:
                                continue

                        else:
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
                                self.get_class_list(Classe_option.text)
        return

    def get_class_list(self, class_name):
        table_xpath = '/html/body/div/div[1]/div[2]/div[2]/section[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/table'
        try:
            df = pd.read_html(StringIO(self.driver.find_element(By.XPATH, table_xpath).get_attribute('outerHTML')))[0]
        except:
            print_error("WE CANNOT FIND THE DATA TABLE")
        else:
            print_info(f"EXTRACTING THE LIST OF {class_name}")
            df.to_excel(f"db/classes_list/{class_name}.xlsx", index=False)
        return


    def main_list_reader(self):
        self.get_list_page()
        self.list_of_each_class()
        return

