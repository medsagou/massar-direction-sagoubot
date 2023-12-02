# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 22:49:39 2023

@author: Pr. Sagou
"""
import os
import sys
from dotenv import load_dotenv
from print_sagou import *
from Class_Files import C_File

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()  # loading the environment variables from the .env file





class Massar_Direction_Sagou:
    def __init__(self, driver = "", console=""):
        self.driver = console
        self.console = console
        return

    def get_driver(self):
        opt = webdriver.FirefoxOptions()
        opt.add_argument("--start-maximized")
        # chromedriver_autoinstaller.install()
        # self.driver = webdriver.Firefox(options=opt)
        try:
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
        except:
            print_error("BROWSER OPENING ERROR, TRY TO DOWNLOAD AND INSTALL FIREFOX", console=self.console)
            return False
        else:
            print_success("DRIVER CONNECTED", console=self.console)
            return True

    def get_site(self):
        try:
            self.driver.get(os.getenv("OFFICIAL_SITE"))
        except:
            print_error("WE CAN't OPEN THE BROWSER", console=self.console)
            self.exit_program()
        else:
            print_info("SITE OPENED", console=self.console)
            return True

    def get_list_page(self):
        try:
            self.driver.get("https://massar.men.gov.ma/Evaluation/Absence/AbsenceJournaliereParClasse")
        except:
            print_error("We Can't find the list page! Close the program and try again.", console=self.console)
        else:
            print_info("GETTING TO THE LIST PAGE", console=self.console)


    def fill_username(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (
                        By.ID,"UserName",
                    )
                )
            )
        finally:
            username = self.driver.find_element(By.ID, "UserName")
            username.send_keys(os.getenv("EMAIL"))
            print_info("USERNAME FIELD DONE", console=self.console)
        return

    def fill_password(self):
        password = self.driver.find_element(By.ID, "Password")
        password.send_keys(os.getenv("PASSWORD"))
        print_info("PASSWORD FIELD DONE", console=self.console)
        return

    def submit_form(self):
        # submit the form
        sumbit_button = self.driver.find_element(By.ID, "btnSubmit")
        sumbit_button.click()
        print_info("BUTTON CLICKED", console=self.console)

        # checking if we've getting any error while submiting the form
        if not self.check_error_login():
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.ID, "sidebar-menu",
                        )
                    )
                )
            except:
                print_error("PLEASE CHECK YOUR LOGIN INFORMATION AND TRY AGAIN.", console=self.console)
                self.exit_program()
            else:
                print_success("WE HAVE SUCCESSFULLY LOGGED INTO YOUR ACCOUNT", console=self.console)
            return
        else:
            print_error("ERROR: PLEASE CHECK YOUR LOGIN INFORMATION AND TRY AGAIN.", console=self.console)
            self.exit_program()


    def check_error_login(self):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(
                    (
                        By.ID, "MsgError",
                    )
                )
            )
        except:
            return False
        else:
            return True




    def close_tab(self):
        self.driver.quit()
        return

    def exit_program(self):
        print_info("EXITING THE PROGRAM -- GOODBYE --", console=self.console)
        self.driver.close()
        self.driver.quit()
        # sys.exit()

    def main_interaction(self):

        if self.get_driver():
            self.get_site()
            self.fill_username()
            self.fill_password()
            self.submit_form()
        else:
            return False
        #_____________________________





# end of Massar_Sagou class
