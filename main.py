import tkinter as tk
import customtkinter
from tkinter import filedialog
import time
import os
from PIL import Image
from validate_email import validate_email
from utilities import C_File, C_Dossier
from dotenv import set_key, load_dotenv

import threading
import logging
import sys


from absence_app import Read_Db
from absence_app import Absence


# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

dirPath = os.path.dirname(os.path.realpath(__file__))

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.tabview_generate_lists = None
        self.tabview_fill_bot= None
        self.generate_list_menu = None
        self.about_us_text = None
        self.fill_absence_menu = None
        self.try_again_generate = False
        self.try_again_fill = False
        self.progressbar_1 = None

        image_path = resource_path("images")


        self.main_logo_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "logo_black.png")),
            dark_image=Image.open(os.path.join(image_path, "logo_white.png")), size=(200,200))
        self.about_us_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "logo_black.png")),
            dark_image=Image.open(os.path.join(image_path, "logo_white.png")), size=(150, 150))
        # self.main_logo_photo = ImageTk.PhotoImage(self.main_logo_image)



        # configure window
        self.title("SagouBot Massar Direction")
        self.iconbitmap(resource_path("icon.ico"))
        self.geometry(f"{1100}x{580}")


        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.sidebar_frame.grid(row=0, column=0)

        self.sideBar_logo = customtkinter.CTkLabel(self.sidebar_frame, text="",
                                                             image=self.main_logo_image)
        self.sideBar_logo.grid(row=5, column=0, padx=20, pady=20)

        self.entry_default_bordercolor = customtkinter.CTkEntry(self).cget("border_color")

        # self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="SagouBot", font=customtkinter.CTkFont(size=40, weight="bold"))
        # self.logo_label.grid(row=1, column=0, padx=20, pady=(20, 10))
        self.generate_list_menu_button_event()
        # Console (Text area)
        self.console_text = customtkinter.CTkTextbox(self, height=200, width=400, fg_color="gray1")
        self.console_text.insert("0.0", "CONSOLE")
        self.console_text.insert(F"{len('CONSOLE')}.0", "--------" * 28)
        self.console_text.configure(state="disabled")
        self.console_text.grid(row=1, column=1, padx=(20, 20), pady=(5, 15), sticky="nsew")
        self.console_text.tag_config("error", foreground="red")
        self.console_text.tag_config("note", foreground="orange")
        self.console_text.tag_config("successes", foreground="blue")

        # self.generate_progress_bar()
        # Progress Bar
        # progress_bar = customtkinter.CTkProgressBar(self, mode='determinate')
        # progress_bar.grid(row=1, column=1, padx=(20, 20), pady=(5, 0), sticky="nsew")

        # # Button to trigger updates
        # update_button = customtkinter.CTkButton(self, text="Start Processing", command=())
        # update_button.grid(row=1, column=1, padx=(20, 20), pady=(5, 0), sticky="nsew")




    def high_school_switch(self):
        state = self.high_school_options.get()
        options = [self.TCS,
        self.TCSF,
        self.TCLSH,
        self.BACSC,
        self.BACSH,
        self.BACSE,
        self.BACSVT,
        self.BACSH2]
        if state:
            for option in options:
                option.configure(state="normal")
        else:
            for option in options:
                option.configure(state="disabled")
        return
    def college_switch(self):
        state = self.college_options.get()
        if state:
            self.college_generale.configure(state="normal")
            self.college_aspeb.configure(state="normal")
            self.college_inter.configure(state="normal")
        else:
            self.college_generale.configure(state="disabled")
            self.college_aspeb.configure(state="disabled")
            self.college_inter.configure(state="disabled")


    def college_label_error(self):
        current_text = self.label_college.cget("text")
        self.label_college.configure(text=current_text.replace("*", "") + "*", text_color="red")
        return
    def high_school_label_eroor(self):
        current_text = self.label_high_school.cget("text")
        self.label_high_school.configure(text=current_text.replace("*", "") + "*", text_color="red")
        return

    def reset_label_high_college(self):
        current_text1 = self.label_college.cget("text")
        current_text = self.label_high_school.cget("text")
        self.label_high_school.configure(text=current_text.replace("*", ""), text_color="gray90")
        self.label_college.configure(text=current_text1.replace("*", ""), text_color="gray90")

    def label_data_file_error(self):
        current_text = self.label_data_file.cget("text")
        self.label_data_file.configure(text=current_text.replace("*", "") + "*", text_color="red")
        return
    def label_template_file_error(self):
        current_text = self.label_template_entry.cget("text")
        self.label_template_entry.configure(text=current_text.replace("*", "") + "*", text_color="red")
        return

    def reset_error1(self):
        current_text = self.label_data_file.cget("text")
        self.label_data_file.configure(text=current_text.replace("*", ""), text_color="gray90")
        return

    def reset_error2(self):
        current_text = self.label_template_entry.cget("text")
        self.label_template_entry.configure(text=current_text.replace("*", ""), text_color="gray90")
        return

    def directory_error(self):
        current_text = self.label_output_folder.cget("text")
        self.label_output_folder.configure(text=current_text + "*", text_color="red")
        return
    def reset_error3(self):
        current_text = self.label_output_folder.cget("text")
        self.label_output_folder.configure(text=current_text.replace("*", ""), text_color="gray90")
        return


    def go_to_review2(self):
        if self.email_entry.get() == "" or self.password_entry.get() == "" or not self.validate_path(self.entry_path_absence) or not self.check_terms_and_condition.get():
            if self.email_entry.get() == "":
                self.error_label(self.label_email_entry)
                self.entry_error(self.email_entry)
            if len(self.password_entry.get()) < 8:
                self.error_label(self.label_password_entry)
                self.entry_error(self.password_entry)
            if not self.validate_path(self.entry_path_absence):
                self.error_label(self.label_absence_data_file)
                self.entry_error(self.entry_path_absence)
            if not self.check_terms_and_condition.get():
                self.check_terms_and_condition.configure(border_color="red", text_color="red")
                self.error_label(self.label_terms)
        else:
            paths = C_File(resource_path("db/paths.txt"))
            L = paths.fichier_to_Liste()
            L[3] = "ABSENCE_FILE" + "=" + self.entry_path_absence.get() +"\n"
            L[4] = "EMAIL" + "=" + self.email_entry.get() +"\n"
            paths.Liste_to_Fichier(L)
            set_key(dotenv_path=os.path.join(dirPath,".env"), key_to_set="EMAIL", value_to_set=self.email_entry.get())
            set_key(dotenv_path=os.path.join(dirPath,".env"), key_to_set="PASSWORD", value_to_set=self.password_entry.get())
            load_dotenv(dotenv_path=os.path.join(dirPath,".env"))
            self.tabview_fill_bot.set("Review & Submit")

            self.label_all_review2 = customtkinter.CTkTextbox(self.tabview_fill_bot.tab("Review & Submit"))
            self.label_all_review2.grid(row=0, column=0, columnspan=6, sticky="nsew")
            # self.label_all_review2.insert("1.0", text)
            text = f"Email:"
            text += " " * (30 - len("Email:"))
            text += str(self.email_entry.get()) + "\n\n"
            self.label_all_review2.insert("end", text)
            text = "Absence Excel File:"
            text += " " * (30 - len("Absence Excel File:"))
            text += str(self.entry_path_absence.get())+ "\n\n"
            self.label_all_review2.insert("end", text)
            text = "Browser:"
            text += " " * (30 - len("Browser:"))
            if self.browser_type.get() == 2:
                text += "FireFox"
            else:
                text += "Chrome"
            self.label_all_review2.insert("end", text)
            self.label_all_review2.configure(state="disabled", text_color="gray70")

        return
    def go_to_output_location(self):
        if self.tabview_generate_lists.grid_info():
            tabview = self.tabview_generate_lists
            tab = tabview.get()
            optionsHighSchool = [self.TCS,
                                 self.TCSF,
                                 self.TCLSH,
                                 self.BACSC,
                                 self.BACSH,
                                 self.BACSE,
                                 self.BACSVT,
                                 self.BACSH2]
            optionsCollege = [
                self.college_inter,
                self.college_aspeb,
                self.college_generale
            ]
            selected_classes = []
            paths = C_File(resource_path("db/paths.txt"))
            if tab == "Setup":
                # path validation
                if self.validate_path(self.entry_path) and self.validate_path(self.entry_path2) and (
                        self.college_options.get() or self.high_school_options.get()):
                    if self.high_school_options.get():
                        for option in optionsHighSchool:
                            if option.get():
                                selected_classes.append((option.cget("text")))
                    if self.college_options.get():
                        for option in optionsCollege:
                            if option.get():
                                selected_classes.append((option.cget("text")))
                    if len(selected_classes) == 0:
                        self.college_label_error()
                        self.high_school_label_eroor()
                    else:
                        self.selected_classes = selected_classes
                        self.tabview_generate_lists.set("Output Location")
                        L = paths.fichier_to_Liste()
                        L[0] = "DATA" + "=" + self.entry_path.get() + "\n"
                        L[1] = "TEMPLATE" + "=" + self.entry_path2.get() + "\n"
                        paths.Liste_to_Fichier(L)
                else:
                    if not self.validate_path(self.entry_path):
                        self.label_data_file_error()
                    if not self.validate_path(self.entry_path2):
                        self.label_template_file_error()
                    if self.high_school_options.get():
                        for option in optionsHighSchool:
                            if option.get():
                                selected_classes.append((option.cget("text")))
                    if self.college_options.get():
                        for option in optionsCollege:
                            if option.get():
                                selected_classes.append((option.cget("text")))
                    if len(selected_classes) == 0:
                        self.college_label_error()
                        self.high_school_label_eroor()
            if tab == "Output Location":
                if self.validate_dir(self.output_path):
                    self.tabview_generate_lists.set("Review & Submit")
                    L = paths.fichier_to_Liste()
                    L[-1] = "DIR" + "=" + self.output_path.get()
                    paths.Liste_to_Fichier(L)

                    self.label_all_review1 = customtkinter.CTkTextbox(self.tabview_generate_lists.tab("Review & Submit"))
                    self.label_all_review1.grid(row=0, column=0, columnspan=6, sticky="nsew")
                    # self.label_all_review2.insert("1.0", text)
                    text = f"Data file path:"
                    text += " " * (30 - len("Data file path:"))
                    text += str(self.entry_path.get()) + "\n\n"
                    self.label_all_review1.insert("end", text)
                    text = "Template file path:"
                    text += " " * (30 - len("Template file path:"))
                    text += str(self.entry_path2.get()) + "\n\n"
                    self.label_all_review1.insert("end", text)
                    text = "Classes:"
                    text += " " * (30 - len("Classes:"))
                    for c in self.selected_classes:
                        text = text + c + ",\t"
                    self.label_all_review1.insert("end", text + "\n\n")
                    text = "Output directory:"
                    text += " " * (30 - len("Output directory:"))
                    text += str(self.output_path.get()) + "\n\n"
                    self.label_all_review1.insert("end", text)
                    self.label_all_review1.configure(state="disabled", text_color="gray70")
                else:
                    self.directory_error()
        return

    def browse_path(self):
        filetypes = (
            ("Text files", "*.xls"),  # Display only .txt files
            ("All files", "*.*")  # Display all files
        )
        path = filedialog.askopenfilename(filetypes=filetypes, initialdir=os.path.dirname(self.path["DATA"]) if self.path["DATA"] != "" else os.path.join(os.path.expanduser('~'), 'Documents'))
        if path == "":
            return
        self.entry_path.delete(0, tk.END)  # Clear the entry
        self.entry_path.insert(0, os.path.abspath(path))
        self.path["DATA"] = path
        file = C_File(file_name=path)
        if file.existe_fichier():
            self.reset_error1()

    def browse_path2(self):
        filetypes = (
            ("Text files", "*.xlsx"),  # Display only .txt files
            ("All files", "*.*")  # Display all files
        )
        path = filedialog.askopenfilename(filetypes=filetypes, initialdir=os.path.dirname(self.path["TEMPLATE"]) if self.path["TEMPLATE"] != "" else os.path.join(os.path.expanduser('~'), 'Documents'))
        if path == "":
            return
        self.entry_path2.delete(0, tk.END)  # Clear the entry
        self.entry_path2.insert(0, os.path.abspath(path))
        self.path["TEMPLATE"] = path
        file = C_File(file_name=path)
        if file.existe_fichier():
            self.reset_error2()
    def browser_path3(self):
        filetypes = (
            ("Text files", "*.xlsx"),  # Display only .txt files
            ("All files", "*.*")  # Display all files
        )
        path = filedialog.askopenfilename(filetypes=filetypes, initialdir=os.path.dirname(self.path["ABSENCE_FILE"]) if self.path["ABSENCE_FILE"] != "" else os.path.join(os.path.expanduser('~'), 'Documents'))
        if path == "":
            return
        self.path["ABSENCE_FILE"] = path
        self.entry_path_absence.delete(0, tk.END)  # Clear the entry
        self.entry_path_absence.insert(0, os.path.abspath(path))
        file = C_File(file_name=path)
        if file.existe_fichier():
            self.reset_label(self.label_absence_data_file)
            self.entry_reset(self.entry_path_absence)


    def browse_folder(self):
        path = filedialog.askdirectory(initialdir=self.path["DIR"] if self.path["DIR"] != "" else os.path.join(os.path.expanduser('~'), 'Documents'))
        if path == "":
            return
        self.output_path.delete(0, tk.END)
        self.output_path.insert(0, os.path.abspath(path))
        self.path["DIR"] = path
        dir = C_Dossier()
        if dir.existe_dossier(Chemin=path):
            self.reset_error3()
        return


    # Function to validate the path entry
    def validate_path(self, path):
        if path.get() == "":
            return False
        file = C_File(file_name=path.get())
        return file.existe_fichier()

    def validate_dir(self, path):
        if path.get() == "":
            return False
        dir = C_Dossier()
        return dir.existe_dossier(Chemin=path.get())

    def back(self):
        if self.tabview_generate_lists.grid_info():
            tab = self.tabview_generate_lists
        else:
            tab = self.tabview_fill_bot

        if tab.get() == "Review & Submit":
            tab.set("Output Location")
        elif tab.get() == "Output Location":
            tab.set("Setup")
        return

    def back2(self):
        self.tabview_fill_bot.set("Setup") if self.tabview_fill_bot.grid_info() else self.tabview_generate_lists.set("Setup")
        return

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.generate_list_menu.configure(fg_color=("gray75", "gray25") if name == "Generate Lists" else "transparent")
        self.fill_absence_menu.configure(fg_color=("gray75", "gray25") if name == "Fill Absence Bot" else "transparent")
        self.about_us_menu.configure(fg_color=("gray75", "gray25") if name == "About us" else "transparent")

    def generate_progress_bar(self, determinate=True):
        if self.progressbar_1 is None:
            self.progressbar_1 = customtkinter.CTkProgressBar(self.sidebar_frame,
                                                              mode="determinate" if determinate == True else "indeterminate")
            state = True
        else:
            self.progressbar_1.configure(mode="determinate" if determinate == True else "indeterminate")
            state = False

        if determinate:
            self.progressbar_1.set(0)
        else:
            self.progressbar_1.start()
        if state:
            self.progressbar_1.grid(row=6, column=0, padx=20, pady=20, sticky="ew")
        else:
            self.progressbar_1.grid()


    def generate_list_menu_button_event(self):
        if self.try_again_generate != False:
            test = self.generate_list_menu.cget("fg_color")
            if test == ("gray75", "gray25"):
                self.tabview_generate_lists.set("Setup")
                return
        if self.try_again_generate == False:
            self.generate_list_menu = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height=40,
                                                              border_spacing=10,
                                                              text="Generate Lists",
                                                              fg_color="transparent", text_color=("gray10", "gray90"),
                                                              hover_color=("gray70", "gray30"), anchor="w",
                                                              command=self.generate_list_menu_button_event)
            self.generate_list_menu.grid(row=1, column=0, sticky="ew", pady=(20, 0))

            self.fill_absence_menu = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height=40,
                                                             border_spacing=10, text="Fill Absence Bot",
                                                             fg_color="transparent", text_color=("gray10", "gray90"),
                                                             hover_color=("gray70", "gray30"), anchor="w",
                                                             command=self.fill_absence_button_event
                                                             )
            self.fill_absence_menu.grid(row=2, column=0, sticky="ew")

            self.about_us_menu = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height=40,
                                                         border_spacing=10, text="About us",
                                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                                         hover_color=("gray70", "gray30"), anchor="w",
                                                         command=self.about_us_button_event
                                                         )
            self.about_us_menu.grid(row=3, column=0, sticky="ew")
            # end of side bar

            # generate lists page
            self.tabview_generate_lists = customtkinter.CTkTabview(self, width=250, state='disabled', text_color_disabled='white',
                                                    height=250)
            self.tabview_generate_lists.grid(row=0, column=1, padx=(20, 20), pady=(5, 0), sticky="nsew")
            self.tabview_generate_lists.add("Setup")
            self.tabview_generate_lists.add("Output Location")
            self.tabview_generate_lists.add("Review & Submit")
            self.tabview_generate_lists.tab("Setup").grid_columnconfigure(0, weight=1)
            # setup tab
            self.tabview_generate_lists.tab("Setup").grid_rowconfigure(0, weight=1)
            self.tabview_generate_lists.tab("Setup").grid_columnconfigure(0, weight=1)

            # data entry
            # check if file exist
            paths = C_File(file_name=resource_path("db/paths.txt"))
            self.path={}
            if paths.existe_fichier():
                self.paths = paths.fichier_to_Liste()
                for path in self.paths:
                    path_splited = path.split("=")
                    self.path[path_splited[0]]=path_splited[-1].strip()

            self.data_entry_frame = customtkinter.CTkFrame(self.tabview_generate_lists.tab("Setup"))
            self.data_entry_frame.grid(sticky='nw', row=0, column=0, padx=5, pady=(0, 0))

            self.label_data_file = customtkinter.CTkLabel(self.data_entry_frame, text="Data File (.xls):",
                                                          text_color="gray90")
            self.label_data_file.grid(row=0, column=0, padx=(0, 5), pady=(15, 0))

            self.entry_path = customtkinter.CTkEntry(self.data_entry_frame, placeholder_text="C:\\", validate='focusout',
                                                     validatecommand=((), '%P'),
                                                     width=250)
            self.entry_path.grid(row=0, column=1, padx=(100, 5), pady=(15, 0))

            self.browse_button = customtkinter.CTkButton(self.data_entry_frame, text="Browse", command=self.browse_path,
                                                         width=50)
            self.browse_button.grid(row=0, column=2, padx=(0, 5), pady=(15, 0))

            self.label_template_entry = customtkinter.CTkLabel(self.data_entry_frame, text="Template file (.xlsx):")
            self.label_template_entry.grid(row=1, column=0, padx=(0, 5), pady=(15, 0))

            self.entry_path2 = customtkinter.CTkEntry(self.data_entry_frame, placeholder_text="C:\\", validate='focusout',
                                                      width=250)
            self.entry_path2.grid(row=1, column=1, padx=(100, 5), pady=(15, 10))

            self.browse_button2 = customtkinter.CTkButton(self.data_entry_frame, text="Browse", command=self.browse_path2,
                                                          width=50)
            self.browse_button2.grid(row=1, column=2, padx=(0, 5), pady=(15, 10))

            if self.path["DATA"] != "":
                self.entry_path.insert(0, self.path["DATA"])
            if self.path["TEMPLATE"] != "":
                self.entry_path2.insert(0, self.path["TEMPLATE"])
            self.class_type_options_frame = customtkinter.CTkFrame(self.tabview_generate_lists.tab("Setup"), fg_color="gray25", height=100)
            self.class_type_options_frame.grid(sticky="nsew", row=2, column=0, columnspan=6, padx=10, pady=(20, 20))
            # self.error_label = customtkinter.CTkLabel(self.class_type_options_frame, text="You have to choose atlease one class", text_color="black")
            # self.error_label.grid(row=0, column=0, padx=(0,0))
            self.label_college = customtkinter.CTkLabel(self.class_type_options_frame, text="College Classes")
            self.label_college.grid(row=0, column=0, padx=(0, 0))
            self.college_options = customtkinter.CTkSwitch(self.class_type_options_frame, text="College", state="switched",
                                                           command=self.college_switch)
            self.college_options.select()
            self.college_options.grid(row=1, column=0, padx=(0, 0))
            self.college_inter = customtkinter.CTkCheckBox(self.class_type_options_frame, text="APIC", state="normal",
                                                           checkbox_width=20, checkbox_height=20,
                                                           command=self.reset_label_high_college)
            self.college_inter.grid(row=2, column=0, padx=(20, 0), pady=(10, 0), sticky="n")

            self.college_generale = customtkinter.CTkCheckBox(self.class_type_options_frame, text="ASCG", state="normal",
                                                              checkbox_width=20, checkbox_height=20,
                                                              command=self.reset_label_high_college)
            self.college_generale.grid(row=2, column=1, padx=(0, 0), pady=(10, 0), sticky="n")
            self.college_aspeb = customtkinter.CTkCheckBox(self.class_type_options_frame, text="ASCPEB", state="normal",
                                                           checkbox_width=20, checkbox_height=20,
                                                           command=self.reset_label_high_college)
            self.college_aspeb.grid(row=3, column=0, padx=(20, 0), pady=(5, 5), sticky="n")

            self.label_high_school = customtkinter.CTkLabel(self.class_type_options_frame, text="High School Classes",
                                                            anchor="e")
            self.label_high_school.grid(row=0, column=2, padx=(100, 0))
            self.high_school_options = customtkinter.CTkSwitch(self.class_type_options_frame, text="High School",
                                                               state="switched",
                                                               command=self.high_school_switch)
            # self.high_school_options.select()
            self.high_school_options.grid(row=1, column=2, padx=(80, 0))
            self.TCS = customtkinter.CTkCheckBox(self.class_type_options_frame, text="TCS", state="disabled",
                                                 checkbox_width=20, checkbox_height=20,
                                                 command=self.reset_label_high_college)
            self.TCS.grid(row=2, column=2, padx=(100, 0), pady=(5, 0), sticky="nsew")

            self.TCSF = customtkinter.CTkCheckBox(self.class_type_options_frame, text="TCSF", state="disabled",
                                                  checkbox_width=20, checkbox_height=20,
                                                  command=self.reset_label_high_college)
            self.TCSF.grid(row=2, column=3, padx=(0, 0), pady=(5, 0), sticky="nsew")

            self.TCLSH = customtkinter.CTkCheckBox(self.class_type_options_frame, text="TCLSH", state="disabled",
                                                   checkbox_width=20, checkbox_height=20,
                                                   command=self.reset_label_high_college)
            self.TCLSH.grid(row=3, column=2, padx=(100, 0), pady=(5, 5), sticky="nsew")

            self.BACSE = customtkinter.CTkCheckBox(self.class_type_options_frame, text="1BACSE", state="disabled",
                                                   checkbox_width=20, checkbox_height=20,
                                                   command=self.reset_label_high_college)
            self.BACSE.grid(row=3, column=3, padx=(0, 0), pady=(5, 5), sticky="nsew")
            self.BACSH = customtkinter.CTkCheckBox(self.class_type_options_frame, text="1BACSH", state="disabled",
                                                   checkbox_width=20, checkbox_height=20,
                                                   command=self.reset_label_high_college)
            self.BACSH.grid(row=3, column=4, padx=(0, 0), pady=(5, 5), sticky="nsew")
            self.BACSC = customtkinter.CTkCheckBox(self.class_type_options_frame, text="2BACSC", state="disabled",
                                                   checkbox_width=20, checkbox_height=20,
                                                   command=self.reset_label_high_college)
            self.BACSC.grid(row=3, column=5, padx=(0, 0), pady=(5, 5), sticky="nsew")
            self.BACSH2 = customtkinter.CTkCheckBox(self.class_type_options_frame, text="2BACSH", state="disabled",
                                                    checkbox_width=20, checkbox_height=20,
                                                    command=self.reset_label_high_college)
            self.BACSH2.grid(row=2, column=4, padx=(0, 0), pady=(5, 0), sticky="nsew")
            self.BACSVT = customtkinter.CTkCheckBox(self.class_type_options_frame, text="2BACSVT", state="disabled",
                                                    checkbox_width=20, checkbox_height=20,
                                                    command=self.reset_label_high_college)
            self.BACSVT.grid(row=2, column=5, padx=(0, 0), pady=(5, 0), sticky="nsew")

            self.submit = customtkinter.CTkButton(self.tabview_generate_lists.tab("Setup"), text="Next",
                                                  command=self.go_to_output_location, width=50)
            self.submit.grid(row=6, column=5, padx=10, pady=(5, 5))
            self.return_btn = customtkinter.CTkButton(self.tabview_generate_lists.tab("Setup"), text="Exit",
                                                      width=50, fg_color="gray30", command=self.exit)
            self.return_btn.grid(row=6, column=4, padx=10, pady=(5, 5))

            # output location tab
            self.tabview_generate_lists.tab("Output Location").grid_rowconfigure(0, weight=1)
            self.tabview_generate_lists.tab("Output Location").grid_columnconfigure((0, 1, 2), weight=1)

            self.output_location_frame = customtkinter.CTkFrame(self.tabview_generate_lists.tab("Output Location"), height=200)
            self.output_location_frame.grid(sticky='nw', row=0, column=0, padx=5, pady=(20, 0))

            self.label_output_folder = customtkinter.CTkLabel(self.output_location_frame, text="Output Folder")
            self.label_output_folder.grid(row=0, column=0, padx=(0, 5), pady=(15, 0))
            self.output_path = customtkinter.CTkEntry(self.output_location_frame,
                                                     placeholder_text=self.path["DIR"] if self.path["DIR"] != "" else os.path.join(os.path.expanduser('~'), 'Documents'),
                                                     validate='focusout',
                                                     width=250)
            self.output_path.insert("0", str(self.path["DIR"] if self.path["DIR"] != "" else os.path.join(os.path.expanduser('~'), 'Documents')))
            self.output_path.grid(row=0, column=1, padx=(100, 5), pady=(15, 0))

            self.browse_button3 = customtkinter.CTkButton(self.output_location_frame, text="Browse",
                                                          command=self.browse_folder, width=50)
            self.browse_button3.grid(row=0, column=2, padx=(0, 5), pady=(15, 0))

            self.submit2 = customtkinter.CTkButton(self.tabview_generate_lists.tab("Output Location"), text="Next",
                                                  command=self.go_to_output_location, width=50)
            self.submit2.grid(row=3, column=5, padx=10, pady=(5, 5))
            self.return_btn2 = customtkinter.CTkButton(self.tabview_generate_lists.tab("Output Location"), text="Back", command=self.back,
                                                      width=50, fg_color="gray30")
            self.return_btn2.grid(row=3, column=4, padx=10, pady=(5, 5))

            # review tab
            self.tabview_generate_lists.tab("Review & Submit").grid_rowconfigure(0, weight=1)
            self.tabview_generate_lists.tab("Review & Submit").grid_columnconfigure((0, 1, 2), weight=1)
            self.submit3 = customtkinter.CTkButton(self.tabview_generate_lists.tab("Review & Submit"), text="Submit",
                                                  command=self.generate_absence_file, width=60)
            self.submit3.grid(row=4, column=5, padx=10, pady=(5, 5))
            self.return_btn3 = customtkinter.CTkButton(self.tabview_generate_lists.tab("Review & Submit"), text="Back", command=self.back,
                                                      width=50, fg_color="gray30")
            self.return_btn3.grid(row=4, column=4, padx=10, pady=(5, 5))
            self.select_frame_by_name("Generate Lists")
            self.try_again_generate = True
        else:
            self.tabview_fill_bot.grid_remove()
            self.tabview_generate_lists.grid()
            if not self.console_text.grid_info():
                self.console_text.grid()
            if self.about_us_text is not None:
                self.about_us_text.grid_remove()
                self.about_us_logo.grid_remove()
            self.select_frame_by_name("Generate Lists")






    def entry_error(self, entry):
        entry.configure(border_color="red")
    def entry_reset(self, entry):
        entry.configure(border_color=self.entry_default_bordercolor)
    def error_label(self, label):
        current_text = label.cget("text")
        label.configure(text=current_text.replace("*", "") + "*", text_color="red")
        return
    def reset_label(self, label):
        current_text = label.cget("text")
        label.configure(text=current_text.replace("*", ""), text_color="gray90")
        return
    def validate_email_entry(self):
        email = self.email_entry.get()
        is_valid = validate_email(email)
        if is_valid:
            self.reset_label(self.label_email_entry)
            self.entry_reset(self.email_entry)
        else:
            self.error_label(self.label_email_entry)
            self.entry_error(self.email_entry)
    def check_terms_box(self):
        if self.check_terms_and_condition.get():
            self.check_terms_and_condition.configure(border_color="gray72", text_color="gray72")
            self.reset_label(self.label_terms)
        else:
            self.check_terms_and_condition.configure(border_color="red", text_color="red")
            self.error_label(self.label_terms)


    def fill_absence_button_event(self):
        test = self.fill_absence_menu.cget("fg_color")
        if test == ("gray75", "gray25"):
            self.tabview_fill_bot.set("Setup")
            return
        if self.try_again_fill == False:
            self.tabview_fill_bot = customtkinter.CTkTabview(self, width=250, state='disabled',
                                                                   text_color_disabled='white',
                                                                   height=250)
            self.tabview_fill_bot.grid(row=0, column=1, padx=(20, 20), pady=(5, 0), sticky="nsew")
            self.tabview_fill_bot.add("Setup")
            self.tabview_fill_bot.add("Review & Submit")
            # setup tab
            self.tabview_fill_bot.tab("Setup").grid_rowconfigure(0, weight=1)
            self.tabview_fill_bot.tab("Setup").grid_columnconfigure(0, weight=1)

            self.tabview_fill_bot.tab("Review & Submit").grid_rowconfigure(0, weight=1)
            self.tabview_fill_bot.tab("Review & Submit").grid_columnconfigure((0, 1, 2), weight=1)
            # self.generate_list_menu_button_event()

            self.tabview_fill_bot.set("Setup")
            # self.submit.destroy()
            # self.return_btn.destroy()
            self.data_entry_frame = customtkinter.CTkFrame(self.tabview_fill_bot.tab("Setup"))
            self.data_entry_frame.grid(sticky='nw', row=0, column=0, padx=5, pady=(0, 0))

            self.label_email_entry = customtkinter.CTkLabel(self.data_entry_frame, text="Email:", text_color="gray90")
            self.label_email_entry.grid(row=0, column=0, padx=(0, 5), pady=(15, 0))

            self.email_entry = customtkinter.CTkEntry(self.data_entry_frame, placeholder_text="email@taalim.ma", width=250)
            self.email_entry.grid(row=0, column=1, padx=(100, 5), pady=(15, 0))

            if self.path["EMAIL"] != "":
                self.email_entry.insert(0, self.path["EMAIL"])


            self.email_entry.bind("<KeyRelease>",  lambda _ : self.validate_email_entry())
            self.label_password_entry = customtkinter.CTkLabel(self.data_entry_frame, text="Password:")
            self.label_password_entry.grid(row=1, column=0, padx=(0, 5), pady=(15, 0))

            self.password_entry = customtkinter.CTkEntry(self.data_entry_frame, show="*" ,placeholder_text="Your Password", width=250)
            self.password_entry.grid(row=1, column=1, padx=(100, 5), pady=(15, 0))

            self.password_entry.bind("<KeyRelease>",  lambda _ : (self.reset_label(self.label_password_entry), self.entry_reset(self.password_entry)) if len(self.password_entry.get()) > 8 else (self.error_label(self.label_password_entry), self.entry_error(self.password_entry)))


            self.label_absence_data_file = customtkinter.CTkLabel(self.data_entry_frame, text="Absence File (.xlsx):",
                                                          text_color="gray90")
            self.label_absence_data_file.grid(row=2, column=0, padx=(0, 5), pady=(15, 0))

            self.entry_path_absence = customtkinter.CTkEntry(self.data_entry_frame, placeholder_text=self.path["ABSENCE_FILE"] if self.path["ABSENCE_FILE"] != "" else "C://", validate='focusout',
                                                     validatecommand=((), '%P'),
                                                     width=250)
            self.entry_path_absence.grid(row=2, column=1, padx=(100, 5), pady=(15, 0))

            if self.path["ABSENCE_FILE"] != "":
                self.entry_path_absence.insert(0, self.path["ABSENCE_FILE"])
            self.browse_button_absence = customtkinter.CTkButton(self.data_entry_frame, text="Browse", command=self.browser_path3,
                                                         width=50)
            self.browse_button_absence.grid(row=2, column=2, padx=(0, 5), pady=(15,0))
            self.label_browser_chrome_firefox = customtkinter.CTkLabel(self.data_entry_frame, text="Browser:", text_color="gray90")
            self.label_browser_chrome_firefox.grid(row=3, column=0, padx=(0, 5), pady=(15, 0))
            self.browser_type = customtkinter.IntVar()
            self.chrome_radio = customtkinter.CTkRadioButton(self.data_entry_frame, text="Chrome", variable=self.browser_type, value=1, state="disabled")
            self.chrome_radio.grid(row=3, column=1, padx=(10, 5), pady=(15, 0))
            self.firefox_radio = customtkinter.CTkRadioButton(self.data_entry_frame, text="Firefox", variable=self.browser_type, value=2)
            self.firefox_radio.grid(row=3, column=2, padx=(10, 5), pady=(15,0))
            self.firefox_radio.select()
            self.label_terms = customtkinter.CTkLabel(self.data_entry_frame, text="Terms and conditions:",
                                                                       text_color="gray90")
            self.label_terms.grid(row=4, column=0, padx=(0, 5), pady=(20, 0))
            self.check_terms_and_condition = customtkinter.CTkCheckBox(self.data_entry_frame, text="I accept the Terms and the Conditions", state="normal",checkbox_width=20, checkbox_height=20, command=self.check_terms_box)
            self.check_terms_and_condition.grid(row=4, column=1, padx=(0, 0), pady=(20,0), sticky="ne")

            self.submit4 = customtkinter.CTkButton(self.tabview_fill_bot.tab("Setup"), text="Next",
                                                  command=self.go_to_review2, width=50)
            self.submit4.grid(row=6, column=5, padx=10, pady=(5, 5))
            self.return_btn4 = customtkinter.CTkButton(self.tabview_fill_bot.tab("Setup"), text="Exit",
                                                      width=50, fg_color="gray30", command=self.exit)
            self.return_btn4.grid(row=6, column=4, padx=10, pady=(5, 5))


            self.run_bot = customtkinter.CTkButton(self.tabview_fill_bot.tab("Review & Submit"), text="Run",
                                                   command=self.run_bot_interaction, width=50)
            self.run_bot.grid(row=6, column=5, padx=10, pady=(5, 5))
            self.return_btn5 = customtkinter.CTkButton(self.tabview_fill_bot.tab("Review & Submit"), text="Back", command=self.back2,
                                                       width=50, fg_color="gray30")
            self.return_btn5.grid(row=6, column=4, padx=10, pady=(5, 5))

            if self.about_us_text is not None:
                self.about_us_text.grid_remove()
                self.about_us_logo.grid_remove()
            self.console_text.grid()
            self.try_again_fill = True

            self.select_frame_by_name("Fill Absence Bot")
        else:
            self.tabview_generate_lists.grid_remove()
            self.tabview_fill_bot.grid()
            self.console_text.grid()
            if self.about_us_text is not None:
                self.about_us_text.grid_remove()
                self.about_us_logo.grid_remove()
            self.select_frame_by_name("Fill Absence Bot")



    def about_us_button_event(self):
        if self.tabview_generate_lists.grid_info():
            self.tabview_generate_lists.grid_remove()
        if self.tabview_fill_bot is not None:
            if self.tabview_fill_bot.grid_info():
                self.tabview_fill_bot.grid_remove()
        if self.about_us_text is not None:
            self.about_us_text.grid()
            self.about_us_logo.grid()
            self.console_text.grid_remove()
            self.select_frame_by_name("About us")
        else:
            self.about_us_logo = customtkinter.CTkLabel(self, text="",
                                                       image=self.about_us_image)
            self.about_us_logo.grid(row=0, column=1, padx=10, pady=10)
            self.about_us_text = customtkinter.CTkTextbox(self, height=200, wrap="word", font=("Arial", 18))
            self.about_us_text.grid(row=1, column=1,rowspan=3, columnspan=6, padx=(20, 20), pady = (15, 20), sticky = "nsew")
            self.console_text.grid_remove()

            self.about_us_text.tag_config("Title", foreground="gray92")
            self.about_us_text.tag_config("subTitle", foreground="gray65")
            self.about_us_text.tag_config("Paragraph", foreground="gray50")
            # Content to be displayed



            # Insert the formatted text into the Text widget
            self.about_us_text.insert("end", "\n About Us", "LargeText")
            self.about_us_text.insert("end", "\n\nMassar Direction Sagoubot is a cutting-edge automation project designed to streamline and simplify the process of managing absence data for multiple classes within a web application. Our solution is meticulously crafted using modern technologies and software tools to optimize efficiency and save valuable time for teachers and administrators.\n", "Paragraph")
            self.about_us_text.insert("end", "\n\n Terms and Privacy", "Title")
            self.about_us_text.insert("end", "\n\nAccount Access", "subTitle")
            self.about_us_text.insert("end",
                                      "\nTo enhance your experience with Massar Direction Sagoubot, the application utilizes your account credentials to securely log in to the Massar website. Your privacy and security are of utmost importance to us. We ensure that your login information is encrypted and used solely for the purpose of automating absence data management.\n", "Paragraph")
            self.about_us_text.insert("end", "\n\nData Handling", "subTitle")
            self.about_us_text.insert("end",
                                      "\nYour data, specifically related to absence records and class information, is processed within the confines of the application to facilitate automation. We do not store or retain any of your personal data beyond the scope of improving application functionality.\n",
                                      "Paragraph")
            self.about_us_text.insert("end", "\n\nSecurity Measures", "subTitle")
            self.about_us_text.insert("end",
                                      "\nWe employ industry-standard security measures to safeguard your account information. This includes encryption protocols and best practices to prevent unauthorized access or misuse of your credentials.\n", "Paragraph")
            self.about_us_text.insert("end", "\n\nUser Consent", "subTitle")
            self.about_us_text.insert("end",
                                      "\nBy using Massar Direction Sagoubot, you consent to the utilization of your Massar account credentials for the sole purpose of automating absence data management. We prioritize transparency and security in handling your login information.\n", "Paragraph")
            self.about_us_text.insert("end", "\n\nQuestions or Concerns", "subTitle")
            self.about_us_text.insert("end",
                                      "\nIf you have any questions, concerns, or require further clarification regarding our terms, privacy practices, or the usage of your account information, please feel free to reach out to us at sakou81833@gmail.com. Your satisfaction and trust are our top priorities.\n", "Paragraph")
            self.about_us_text.configure(state="disabled")
            self.select_frame_by_name("About us")

    def exit(self):
        result = tk.messagebox.askokcancel("Confirmation", "Are you sure you want to exit?")
        if result:  # If the user confirms
            app.quit()
    # backend functions
    def generate_absence_file(self):
        self.generate_progress_bar()
        self.submit3.configure(state="disabled")
        self.return_btn3.configure(state="disabled")
        self.console_text.configure(state="normal")
        self.label_all_review1.configure(text_color="gray35")
        def run_fill_all_class_sheets():
            reader = Read_Db(input_file=self.entry_path.get(),
                             template_file=self.entry_path2.get(),
                             output_file=str(self.output_path.get()) + "\\absence.xlsx",
                             required_classes=self.selected_classes,
                             progress_bar=self.progressbar_1,
                             console=self.console_text)
            reader.fill_all_class_sheets()
            time.sleep(3)
            self.submit3.configure(state="normal")
            self.return_btn3.configure(state="normal")
            self.progressbar_1.grid_remove()
            self.console_text.configure(state="disabled")
            self.label_all_review1.configure(text_color="gray70")

        thread = threading.Thread(target=run_fill_all_class_sheets)
        thread.start()
        return


    def run_bot_interaction(self):
        self.generate_progress_bar(determinate=False)
        self.console_text.configure(state="normal")
        self.run_bot.configure(state="disabled")
        self.return_btn5.configure(state="disabled")

        self.label_all_review2.configure(text_color="gray35")
        def run_fill_absence():

            # loading the class here because of the .env file not getting refreshed
            from Interaction_browser import Massar_Direction_Sagou
            interaction_object = Massar_Direction_Sagou(console=self.console_text)
            driver_test = interaction_object.main_interaction()
            if driver_test:
                interaction_object.get_list_page()
                absence = Absence(driver=interaction_object.driver, console=self.console_text)
                absence.main_absence_loop()
            time.sleep(3)
            self.console_text.configure(state="disabled")
            self.run_bot.configure(state="normal")
            self.return_btn5.configure(state="normal")
            self.label_all_review2.configure(text_color="gray70")
            self.progressbar_1.grid_remove()
        thread = threading.Thread(target=run_fill_absence)
        thread.start()
        return

if __name__ == "__main__":
    app = App()
    app.mainloop()