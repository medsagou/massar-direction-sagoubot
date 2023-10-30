import sys
import time
from print_sagou import *
import pandas as pd
from io import StringIO
from Menu import Menu
import datetime
from scan_absence import Scan_Absences
from Read_XLSB_File import Read_Db
from utilities import get_date_list


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Absence:
    def __init__(self, driver=""):
        self.driver = driver
        self.data_table_Xpath = "/html/body/div/div[1]/div[2]/div[2]/section[2]/div[2]/div[1]/div/div/div[2]/div/form/div/div/div/div/div/div/div/div[2]/div/table"
        self.data_table_reduced_Xpath = '//*[@id="DataTables-Table-0"]/tbody'
        self.row_Xpath = '//*[@id="DataTables-Table-0"]/tbody/tr['
        self.nome_Xpath = ']/td[3]'
        self.CNE_Xpath = ']/td[2]'
        self.select_Xpath = ']/td[4]/select'
        self.h_Xpath = ']/td['
        self.dates = get_date_list()
        self.searchBtn = self.driver.find_element(By.CSS_SELECTOR, "#search > div > div > div > div.box-body > div.blocBtn > button")

    def get_list_page(self):
        try:
            self.driver.get("https://massar.men.gov.ma/Evaluation/Absence/AbsenceJournaliereParClasse")
        except:
            print_error("We Can't find the list page! Close the program and try again.")
        else:
            print_info("GETTING TO THE LIST PAGE")

    def get_classes_from_classes_page(self):
        return

    def main_absence_loop(self):
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
                                    Classe_Select.select_by_value(Classe_option.get_attribute("value"))
                                    date = self.driver.find_element(By.ID, "Jour")
                                    date.send_keys(Keys.CONTROL + "a")
                                    date.send_keys(Keys.DELETE)
                                    date.send_keys(self.dates[0])
                                    self.searchBtn.click()
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
                                        self.fill_absence(classe_name=Classe_option.text)
                                        print_info("A CLASS PASSED")
        return

    def fill_absence(self, classe_name):
        classe_absence = Scan_Absences(classe = classe_name)
        classe_list_absence = classe_absence.get_absence_day_per_student()
        mytable = self.driver.find_element(By.XPATH, self.data_table_reduced_Xpath)
        i = 0
        for row in mytable.find_elements(By.CSS_SELECTOR, 'tr'):
            i += 1
            cne = self.driver.find_element(By.XPATH, str(self.row_Xpath) + str(i) + str(self.CNE_Xpath))
            name = self.driver.find_element(By.XPATH, str(self.row_Xpath) + str(i) + str(self.nome_Xpath))

            try:
                week_absence_student = classe_list_absence[cne.text]
                week_days_per_student = self.list_week_to_days(week_absence_student)
            except KeyError:
                print_error(f'THIS CNE {cne.text} DOES NOT EXIST, THE NAME IS: {name.text}, CLASS: {classe_name}')
            else:

                self.fill_absence_per_day(i,week_days_per_student)

        if classe_name == "1APIC-1":
            time.sleep(400)
        return

    def fill_absence_per_day(self,row_i, week_days_per_student):
        j = 0
        for day in week_days_per_student:
            if str(day[0]) == "0":
                print("full day")
                select_cause = Select(self.driver.find_element(By.XPATH, str(self.row_Xpath) + str(row_i) + str(self.select_Xpath)))
                select_cause.select_by_value("2")
                checkbox = self.driver.find_element(By.XPATH, str(self.row_Xpath) + str(row_i) + str(self.h_Xpath) + str(5) + "]/input[1]")
                checkbox.click()
                print("checkbox clicked")
                return
            elif "x" in day:
                select_cause = Select(self.driver.find_element(By.XPATH, str(self.row_Xpath) + str(row_i) + str(self.select_Xpath)))
                select_cause.select_by_value("2")
                for i in range(len(day)):
                    if day[i] == None:
                        continue
                    if str(day[i]) == "x":
                        print(day[i])
                        if i < 4:
                            checkbox = self.driver.find_element(By.XPATH, str(self.row_Xpath) + str(row_i) + str(self.h_Xpath) + str(6 + i) + "]/input[1]")
                        else:
                            checkbox = self.driver.find_element(By.XPATH, str(self.row_Xpath) + str(row_i) + str(
                                self.h_Xpath) + str(8 + i) + "]/input[1]")
                        checkbox.click()
                    else:
                        print_error('WE CANNOT REGONIZE THE FILL OF THE CELL')

            j += 1
            date = self.driver.find_element(By.ID, "Jour")
            date.send_keys(Keys.CONTROL + "a")
            date.send_keys(Keys.DELETE)
            date.send_keys(self.dates[j])
            self.searchBtn.click()


    def list_week_to_days(self, list_week):
        index = 0
        week = []
        day = []
        for i in range(2,len(list_week)):
            if index == 8:
                week.append(day)
                day = []
                index = 0
            day.append(list_week[i])
            index += 1
        return week


    def main_list_reader(self):
        self.get_list_page()
        self.list_of_each_class()
        return

#
# test = Absence()
# # read = Read_Db()
# # read.fill_all_class_sheets()
#
# classe_absence = Scan_Absences(classe='1APIC-1')
# class_dict_absence = classe_absence.get_absence_day_per_student()
# test.fill_absence()
