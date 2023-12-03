import sys

from utilities.print_sagou import *
# from scan_absence import Scan_Absences
from absence_app import scan_absence
from utilities.other_utilities import get_date_list


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Absence:
    def __init__(self, driver="", console=""):
        self.driver = driver
        self.console = console
        self.data_table_Xpath = "/html/body/div/div[1]/div[2]/div[2]/section[2]/div[2]/div[1]/div/div/div[2]/div/form/div/div/div/div/div/div/div/div[2]/div/table"
        self.data_table_reduced_Xpath = '//*[@id="DataTables-Table-0"]/tbody'
        self.row_Xpath = '//*[@id="DataTables-Table-0"]/tbody/tr['
        self.nome_Xpath = ']/td[3]'
        self.CNE_Xpath = ']/td[2]'
        self.select_Xpath = ']/td[4]/select'
        self.h_Xpath = ']/td['
        self.dates = ""
        self.searchBtn = self.driver.find_element(By.CSS_SELECTOR, "#search > div > div > div > div.box-body > div.blocBtn > button")
        self.saveBtnCssSelector = "#gridFrom > button"

    def get_list_page(self):
        try:
            self.driver.get("https://massar.men.gov.ma/Evaluation/Absence/AbsenceJournaliereParClasse")
        except Exception as e:
            print_error(e, console=self.console)
            print_error("We Can't find the list page! Close the program and try again.", console=self.console)
        else:
            print_info("GETTING TO THE LIST PAGE", console=self.console)

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
            except Exception as e:
                print_error(e, console=self.console)
                print_error("CHECK YOUR INTERNET CONNECTION THEN TRY AGAIN", console=self.console)
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
                                    classe_absence = Scan_Absences(classe=Classe_option.text)
                                    classe_list_absence, start_date, end_date = classe_absence.get_absence_day_per_student2()

                                    if classe_list_absence == False:
                                        print_info(f"THE CLASS {Classe_option.text} NOT IN THE EXCEL FILE", console=self.console)
                                        continue
                                    self.dates = get_date_list(start_date_str=start_date, end_date_str=end_date)
                                    Classe_Select.select_by_value(Classe_option.get_attribute("value"))
                                    for l in range(len(self.dates)):
                                        print_success(f"WORKING ON CLASS {Classe_option.text}, DATE {self.dates[l]}...", console=self.console)
                                        date = self.driver.find_element(By.ID, "Jour")
                                        date.send_keys(Keys.CONTROL + "a")
                                        date.send_keys(Keys.DELETE)
                                        date.send_keys(self.dates[l])
                                        try:
                                            WebDriverWait(self.driver, 15).until(
                                                EC.element_to_be_clickable((By.CSS_SELECTOR, '#search > div > div > div > div.box-body > div.blocBtn > button'))
                                            )
                                        except Exception as e:
                                            print_error(e, console=self.console)
                                            pass
                                        else:
                                            self.searchBtn = self.driver.find_element(By.CSS_SELECTOR, '#search > div > div > div > div.box-body > div.blocBtn > button')
                                            self.searchBtn.click()
                                        try:
                                            WebDriverWait(self.driver, 3).until(
                                                EC.invisibility_of_element_located(
                                                    (
                                                        By.ID, "loadingDiv",
                                                    )
                                                )
                                            )
                                        except Exception as e:
                                            print_error(e, console=self.console)
                                            continue
                                        else:
                                            print_info("FILLING THE ABSENCE...", console=self.console)
                                            self.fill_absence(classe_list_absence=classe_list_absence,class_name=Classe_option.text, day_index = l)
                                            try:
                                                WebDriverWait(self.driver, 30).until(
                                                    EC.presence_of_element_located((By.CSS_SELECTOR,"#gridFrom > button"))
                                                )
                                            except Exception as e:
                                                print_error(e, console=self.console)
                                                print_error('WE COULD NOT FIND THE SAVE BUTTON ', console=self.console)
                                                self.driver.quit()
                                                # sys.exit()
                                            else:
                                                try:
                                                    WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#gridFrom > button")))
                                                except Exception as e:
                                                    print_error(e, console=self.console)
                                                    print_error('WE COULD NOT FIND THE SAVE BUTTON', console=self.console)
                                                else:
                                                    saveBtn = self.driver.find_element(By.CSS_SELECTOR, "#gridFrom > button")
                                                    # saveBtn.click()
                                                    self.driver.execute_script("arguments[0].click();", saveBtn)

                                                    print_info('SAVE BUTTON IS CLICKED', console=self.console)
                                            try:
                                                WebDriverWait(self.driver, 3).until(
                                                    EC.invisibility_of_element_located(
                                                        (
                                                            By.ID, "loadingDiv",
                                                        )
                                                    )
                                                )
                                            except Exception as e:
                                                print_error(e, console=self.console)
                                                pass
                                            try:
                                                WebDriverWait(self.driver, 10).until(
                                                    EC.presence_of_element_located(
                                                        (
                                                            By.ID, "Model_msg_Btn",
                                                        )
                                                    )
                                                )
                                            except Exception as e:
                                                print_error(e, console=self.console)
                                                print_error('WE COULD NOT FIND THE CLOSE BUTTON', console=self.console)
                                            else:
                                                print_info('CLOSE BUTTON IS CLOSED', console=self.console)
                                                close_btn = self.driver.find_element(By.ID, "Model_msg_Btn")
                                                close_btn.click()
                                            try:
                                                WebDriverWait(self.driver, 3).until(
                                                    EC.invisibility_of_element_located(
                                                        (
                                                            By.ID, "loadingDiv",
                                                        )
                                                    )
                                                )
                                            except Exception as e:
                                                print_error(e, console=self.console)
                                                pass

                                            print_success(f"CLASS {Classe_option.text} PASSED, DATE {self.dates[l]}", console=self.console)

        return

    def fill_absence(self, classe_list_absence, class_name, day_index):
        # print(classe_list_absence)
        # print(class_name)
        # print(classe_list_absence)
        mytable = self.driver.find_element(By.XPATH, self.data_table_reduced_Xpath)
        i = 0
        for row in mytable.find_elements(By.CSS_SELECTOR, 'tr'):
            i += 1
            cne = self.driver.find_element(By.XPATH, str(self.row_Xpath) + str(i) + str(self.CNE_Xpath))
            name = self.driver.find_element(By.XPATH, str(self.row_Xpath) + str(i) + str(self.nome_Xpath))

            try:
                week_absence_student = classe_list_absence[cne.text]
                week_days_per_student = self.list_week_to_days(week_absence_student)
            except KeyError as e:
                print_error(e, self.console)
                print_error(f'THIS CNE {cne.text} DOES NOT EXIST, THE NAME IS: {name.text}, CLASS: {class_name}', console=self.console)
            else:
                # print(day_index)
                # print(week_days_per_student)
                self.fill_absence_per_day(i,week_days_per_student[day_index])

        # if classe_name == "1APIC-1":
        #     time.sleep(400)
        return

    def fill_absence_per_day(self,row_i, day):
        j = 0
        # print(day)
        if str(day[0]) == "0":
            # print("FULL DAY")
            select_cause = Select(self.driver.find_element(By.XPATH, str(self.row_Xpath) + str(row_i) + str(self.select_Xpath)))
            select_cause.select_by_value("2")
            checkbox = self.driver.find_element(By.XPATH, str(self.row_Xpath) + str(row_i) + str(self.h_Xpath) + str(5) + "]/input[1]")
            checkbox.click()
            return
        elif "x" in day:
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH, str(self.row_Xpath) + str(row_i) + str(self.select_Xpath)
                        )
                    )
                )
            except Exception as e:
                print_error(e, self.console)
                print_error("AN ERROR IN HTML SELECTION PLEASE TRY AGAIN.", console=self.console)
                self.exit_program()
            select_cause = Select(self.driver.find_element(By.XPATH, str(self.row_Xpath) + str(row_i) + str(self.select_Xpath)))
            select_cause.select_by_value("2")
            for i in range(len(day)):
                if day[i] == None:
                    continue
                if str(day[i]) == "x":
                    # print(day[i])
                    if i < 4:
                        checkbox = self.driver.find_element(By.XPATH, str(self.row_Xpath) + str(row_i) + str(self.h_Xpath) + str(6 + i) + "]/input[1]")
                    else:
                        checkbox = self.driver.find_element(By.XPATH, str(self.row_Xpath) + str(row_i) + str(
                            self.h_Xpath) + str(8 + i) + "]/input[1]")
                    checkbox.click()
                else:
                    print_error('WE CANNOT REGONIZE THE FILL OF THE CELL', console=self.console)

            # j += 1
            # date = self.driver.find_element(By.ID, "Jour")
            # date.send_keys(Keys.CONTROL + "a")
            # date.send_keys(Keys.DELETE)
            # date.send_keys(self.dates[j])
            # self.searchBtn.click()


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
        week.append(day)
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
