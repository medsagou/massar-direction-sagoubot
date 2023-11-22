import tkinter as tk
import tkinter.messagebox
import customtkinter
from tkinter import filedialog
import time
import os
from PIL import Image, ImageTk
from Class_Files import C_File, C_Dossier
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")


        self.main_logo_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "logo_black.png")),
            dark_image=Image.open(os.path.join(image_path, "logo_white.png")), size=(200,200))
        # self.main_logo_photo = ImageTk.PhotoImage(self.main_logo_image)



        # configure window
        self.title("SagouBot Massar Direction")
        self.iconbitmap("icon.ico")
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

        # self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="SagouBot", font=customtkinter.CTkFont(size=40, weight="bold"))
        # self.logo_label.grid(row=1, column=0, padx=20, pady=(20, 10))





        self.generate_list_menu = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Generate Lists",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"), anchor="w", command=self.generate_list_menu_button_event)
        self.generate_list_menu.grid(row=1, column=0, sticky="ew", pady=(20,0))

        self.fill_absence_menu = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Fill Absence Bot",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),anchor="w", command=self.fill_absence_button_event
                                                      )
        self.fill_absence_menu.grid(row=2, column=0, sticky="ew")

        self.about_us_menu = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="About us",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"), anchor="w", command=self.about_us_button_event
                                                     )
        self.about_us_menu.grid(row=3, column=0, sticky="ew")

        self.select_frame_by_name("Generate Lists")
        # end of side bar


        # generate lists page
        self.tabview = customtkinter.CTkTabview(self, width=250, state='disabled', text_color_disabled='white', height=250)
        self.tabview.grid(row=0, column=1, padx=(20, 20), pady=(5, 0), sticky="nsew")
        self.tabview.add("Setup")
        self.tabview.add("Output Location")
        self.tabview.add("Review & Submit")
        self.tabview.tab("Setup").grid_columnconfigure(0, weight=1)
        # setup tab
        self.tabview.tab("Setup").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Setup").grid_columnconfigure(0, weight=1)


            # data entry
        self.data_entry_frame = customtkinter.CTkFrame(self.tabview.tab("Setup"))
        self.data_entry_frame.grid(sticky='nw',row=0, column=0, padx=5, pady=(0,0))

        self.label_data_file = customtkinter.CTkLabel(self.data_entry_frame, text="Data File (.xls):", text_color="gray90")
        self.label_data_file.grid(row=0, column=0, padx=(0, 5), pady=(15,0))

        self.entry_path = customtkinter.CTkEntry(self.data_entry_frame, placeholder_text="C:\\", validate='focusout', validatecommand=((), '%P'),
                                                 width=250)
        self.entry_path.grid(row=0, column=1, padx=(100, 5), pady=(15,0))

        self.browse_button = customtkinter.CTkButton(self.data_entry_frame, text="Browse", command=self.browse_path,
                                                     width=50)
        self.browse_button.grid(row=0, column=2, padx=(0, 5), pady=(15,0))

        self.label_template_entry = customtkinter.CTkLabel(self.data_entry_frame, text="Template file (.xlsx):")
        self.label_template_entry.grid(row=1, column=0, padx=(0, 5), pady=(15,0))

        self.entry_path2 = customtkinter.CTkEntry(self.data_entry_frame, placeholder_text="C:\\", validate='focusout', width=250)
        self.entry_path2.grid(row=1, column=1, padx=(100, 5), pady=(15,0))

        self.browse_button2 = customtkinter.CTkButton(self.data_entry_frame, text="Browse", command=self.browse_path2,width=50)
        self.browse_button2.grid(row=1, column=2, padx=(0, 5), pady=(15,0))


        self.class_type_options_frame = customtkinter.CTkFrame(self.tabview.tab("Setup"), fg_color="gray25", height=100)
        self.class_type_options_frame.grid(sticky="nsew", row=5, column=0, padx=10, pady=(20,20))
        # self.error_label = customtkinter.CTkLabel(self.class_type_options_frame, text="You have to choose atlease one class", text_color="black")
        # self.error_label.grid(row=0, column=0, padx=(0,0))
        self.label_college = customtkinter.CTkLabel(self.class_type_options_frame, text="College Classes")
        self.label_college.grid(row=0, column=0, padx=(0,0))
        self.college_options = customtkinter.CTkSwitch(self.class_type_options_frame, text="College", state="switched", command=self.college_switch)
        self.college_options.select()
        self.college_options.grid(row=1, column=0, padx=(0,0))
        self.college_inter = customtkinter.CTkCheckBox(self.class_type_options_frame, text="APIC", state="normal", checkbox_width=20, checkbox_height=20, command=self.reset_label_high_college)
        self.college_inter.grid(row=2, column=0, padx=(20,0), pady=(10,0), sticky="n")

        self.college_generale = customtkinter.CTkCheckBox(self.class_type_options_frame, text="ASCG", state="normal",
                                                          checkbox_width=20, checkbox_height=20, command=self.reset_label_high_college)
        self.college_generale.grid(row=3, column=0, padx=(20, 0), pady=(5,0), sticky="n")
        self.college_aspeb = customtkinter.CTkCheckBox(self.class_type_options_frame, text="ASCPEB", state="normal",
                                                          checkbox_width=20, checkbox_height=20, command=self.reset_label_high_college)
        self.college_aspeb.grid(row=4, column=0, padx=(20, 0), pady=(5,5), sticky="n")


        self.label_high_school = customtkinter.CTkLabel(self.class_type_options_frame, text="High School Classes", anchor="e")
        self.label_high_school.grid(row=0, column=2, padx=(100,0))
        self.high_school_options = customtkinter.CTkSwitch(self.class_type_options_frame, text="High School", state="switched",
                                                       command=self.high_school_switch)
        # self.high_school_options.select()
        self.high_school_options.grid(row=1, column=2, padx=(80, 0))
        self.TCS = customtkinter.CTkCheckBox(self.class_type_options_frame, text="TCS", state="disabled",
                                                       checkbox_width=20, checkbox_height=20, command=self.reset_label_high_college)
        self.TCS.grid(row=2, column=2, padx=(100, 0), pady=(5, 0), sticky="nsew")

        self.TCSF = customtkinter.CTkCheckBox(self.class_type_options_frame, text="TCSF", state="disabled",
                                             checkbox_width=20, checkbox_height=20, command=self.reset_label_high_college)
        self.TCSF.grid(row=2, column=3, padx=(0, 0), pady=(5, 0), sticky="nsew")

        self.TCLSH = customtkinter.CTkCheckBox(self.class_type_options_frame, text="TCLSH", state="disabled",
                                                          checkbox_width=20, checkbox_height=20, command=self.reset_label_high_college)
        self.TCLSH.grid(row=3, column=2, padx=(100, 0), pady=(5, 0), sticky="nsew")

        self.BACSE = customtkinter.CTkCheckBox(self.class_type_options_frame, text="1BACSE", state="disabled",
                                               checkbox_width=20, checkbox_height=20, command=self.reset_label_high_college)
        self.BACSE.grid(row=3, column=3, padx=(0, 0), pady=(5, 0), sticky="nsew")
        self.BACSH = customtkinter.CTkCheckBox(self.class_type_options_frame, text="1BACSH", state="disabled",
                                               checkbox_width=20, checkbox_height=20, command=self.reset_label_high_college)
        self.BACSH.grid(row=3, column=4, padx=(0, 0), pady=(5, 0), sticky="nsew")
        self.BACSC = customtkinter.CTkCheckBox(self.class_type_options_frame, text="2BACSC", state="disabled",
                                               checkbox_width=20, checkbox_height=20, command=self.reset_label_high_college)
        self.BACSC.grid(row=3, column=5, padx=(0, 0), pady=(5, 0), sticky="nsew")
        self.BACSH2 = customtkinter.CTkCheckBox(self.class_type_options_frame, text="2BACSH", state="disabled",
                                               checkbox_width=20, checkbox_height=20, command=self.reset_label_high_college)
        self.BACSH2.grid(row=2, column=4, padx=(0, 0), pady=(5, 0), sticky="nsew")
        self.BACSVT = customtkinter.CTkCheckBox(self.class_type_options_frame, text="2BACSVT", state="disabled",
                                                checkbox_width=20, checkbox_height=20, command=self.reset_label_high_college)
        self.BACSVT.grid(row=2, column=5, padx=(0, 0), pady=(5, 0), sticky="nsew")





        self.submit = customtkinter.CTkButton(self.tabview.tab("Setup"), text="Next",
                                              command=self.go_to_output_location, width=50)
        self.submit.grid(row=6, column=5, padx=10, pady=(5, 5))
        self.return_btn = customtkinter.CTkButton(self.tabview.tab("Setup"), text="Exit", command=self.back,
                                                  width=50, fg_color="gray30")
        self.return_btn.grid(row=6, column=4, padx=10, pady=(5, 5))





        # output location tab
        self.tabview.tab("Output Location").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Output Location").grid_columnconfigure((0, 1, 2), weight=1)

        self.output_location_frame = customtkinter.CTkFrame(self.tabview.tab("Output Location"), height=200)
        self.output_location_frame.grid(sticky='nw', row=0, column=0, padx=5, pady=(20, 0))

        self.label_ouput_folder = customtkinter.CTkLabel(self.output_location_frame, text="Output Folder")
        self.label_ouput_folder.grid(row=0, column=0, padx=(0, 5), pady=(15, 0))

        self.ouput_path = customtkinter.CTkEntry(self.output_location_frame, placeholder_text=os.path.join(os.path.expanduser('~'), 'Documents'),
                                                 validate='focusout',
                                                 width=250)
        self.ouput_path.insert("0",str(os.path.join(os.path.expanduser('~'), 'Documents')))
        self.ouput_path.grid(row=0, column=1, padx=(100, 5), pady=(15, 0))

        self.browse_button = customtkinter.CTkButton(self.output_location_frame, text="Browse", command=self.browse_folder, width=50)
        self.browse_button.grid(row=0, column=2, padx=(0, 5), pady=(15, 0))


        self.submit = customtkinter.CTkButton(self.tabview.tab("Output Location"), text="Next",
                                              command=self.go_to_output_location, width=50)
        self.submit.grid(row=4, column=5, padx=10, pady=(5, 5))
        self.return_btn = customtkinter.CTkButton(self.tabview.tab("Output Location"), text="Back", command=self.back,
                                                  width=50, fg_color="gray30")
        self.return_btn.grid(row=4, column=4, padx=10, pady=(5, 5))


        # review tab
        self.tabview.tab("Review & Submit").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Review & Submit").grid_columnconfigure((0, 1, 2), weight=1)
        self.submit = customtkinter.CTkButton(self.tabview.tab("Review & Submit"), text="Submit",command=self.go_to_output_location, width=50)
        self.submit.grid(row=4, column=5, padx=10, pady=(5, 5))
        self.return_btn = customtkinter.CTkButton(self.tabview.tab("Review & Submit"), text="Back", command=self.back, width=50, fg_color="gray30")
        self.return_btn.grid(row=4, column=4 ,padx=10, pady=(5, 5))

        # Console (Text area)
        self.console_text = customtkinter.CTkTextbox(self, height=200, width=400)
        self.console_text.insert("0.0", "CONSOLE")
        self.console_text.insert(F"{len('CONSOLE')}.0", "--------" * 28)
        self.console_text.configure(state="disabled")
        self.console_text.grid(row=1, column=1, padx=(20, 20), pady=(5, 0), sticky="nsew")

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
        current_text = self.label_ouput_folder.cget("text")
        self.label_ouput_folder.configure(text=current_text + "*", text_color="red")
        return
    def reset_error3(self):
        current_text = self.label_ouput_folder.cget("text")
        self.label_ouput_folder.configure(text=current_text.replace("*", ""), text_color="gray90")
        return


    def go_to_output_location(self):
        tab = self.tabview.get()
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
        if tab == "Setup":
            # path validation
            if self.validate_path(self.entry_path) and self.validate_path(self.entry_path2) and (self.college_options.get() or self.high_school_options.get()):
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
                    print(selected_classes) # pass the selected_classes to back-end program
                    self.tabview.set("Output Location")
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
            # checkboxes validation
            # if self.college_options.get() or self.high_school_options.get():
            #     if self.high_school_options.get():
            #         for option in optionsHighSchool:
            #             if option.get():
            #                 selected_classes.append((option.cget("text")))
            #     if self.college_options.get():
            #         for option in optionsCollege:
            #             if option.get():
            #                 selected_classes.append((option.cget("text")))

        if tab == "Output Location":
            if self.validate_dir(self.ouput_path):
                self.tabview.set("Review & Submit")
            else:
                self.directory_error()
        return

    def browse_path(self):
        filetypes = (
            ("Text files", "*.xls"),  # Display only .txt files
            ("All files", "*.*")  # Display all files
        )
        path = filedialog.askopenfilename(filetypes=filetypes, initialdir=os.path.join(os.path.expanduser('~'), 'Documents'))
        if path == "":
            return
        self.entry_path.delete(0, tk.END)  # Clear the entry
        self.entry_path.insert(0, path)
        file = C_File(file_name=path)
        if file.existe_fichier():
            self.reset_error1()

    def browse_path2(self):
        filetypes = (
            ("Text files", "*.xlsx"),  # Display only .txt files
            ("All files", "*.*")  # Display all files
        )
        path = filedialog.askopenfilename(filetypes=filetypes, initialdir=os.path.join(os.path.expanduser('~'), 'Documents'))
        if path == "":
            return
        self.entry_path2.delete(0, tk.END)  # Clear the entry
        self.entry_path2.insert(0, path)
        file = C_File(file_name=path)
        if file.existe_fichier():
            self.reset_error2()

    def browse_folder(self):
        path = filedialog.askdirectory(initialdir=os.path.join(os.path.expanduser('~'), 'Documents'))
        if path == "":
            return
        self.ouput_path.delete(0, tk.END)
        self.ouput_path.insert(0, path)
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
        tab = self.tabview.get()
        if tab == "Review & Submit":
            self.tabview.set("Output Location")
        if tab == "Output Location":
            self.tabview.set("Setup")
        return

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.generate_list_menu.configure(fg_color=("gray75", "gray25") if name == "Generate Lists" else "transparent")
        self.fill_absence_menu.configure(fg_color=("gray75", "gray25") if name == "Fill Absence Bot" else "transparent")
        self.about_us_menu.configure(fg_color=("gray75", "gray25") if name == "About us" else "transparent")

        # show selected frame
        # if name == "home":
        #     self.home_frame.grid(row=0, column=1, sticky="nsew")
        # else:
        #     self.home_frame.grid_forget()
        # if name == "frame_2":
        #     self.second_frame.grid(row=0, column=1, sticky="nsew")
        # else:
        #     self.second_frame.grid_forget()
        # if name == "frame_3":
        #     self.third_frame.grid(row=0, column=1, sticky="nsew")
        # else:
        #     self.third_frame.grid_forget()

    def generate_list_menu_button_event(self):
        self.select_frame_by_name("Generate Lists")

    def fill_absence_button_event(self):
        self.select_frame_by_name("Fill Absence Bot")

    def about_us_button_event(self):
        self.select_frame_by_name("About us")



if __name__ == "__main__":
    app = App()
    app.mainloop()