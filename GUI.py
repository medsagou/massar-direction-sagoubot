import tkinter
import tkinter.messagebox
import customtkinter
import time

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("SagouBot Massar Direction")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="SagouBot", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.tabview = customtkinter.CTkTabview(self, width=250, state='disabled', text_color_disabled='white')
        self.tabview.grid(row=0, column=1, padx=(20, 20), pady=(5, 0), sticky="nsew")
        self.tabview.add("Setup")
        self.tabview.add("Output Location")
        self.tabview.add("Review & Submit")
        self.tabview.tab("Setup").grid_columnconfigure(0, weight=1)
        # setup tab
        self.tabview.tab("Setup").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Setup").grid_columnconfigure((0, 1, 2), weight=1)
        self.submit = customtkinter.CTkButton(self.tabview.tab("Setup"), text="Submit",
                                              command=self.go_to_output_location, width=50)
        self.submit.grid(row=0, column=5, padx=10, pady=(5, 5))
        self.return_btn = customtkinter.CTkButton(self.tabview.tab("Setup"), text="Back", command=self.back,
                                                  width=50, fg_color="gray30")
        self.return_btn.grid(row=0, column=4, padx=10, pady=(5, 5))

        # output location tab
        self.tabview.tab("Output Location").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Output Location").grid_columnconfigure((0, 1, 2), weight=1)
        self.submit = customtkinter.CTkButton(self.tabview.tab("Output Location"), text="Submit",
                                              command=self.go_to_output_location, width=50)
        self.submit.grid(row=0, column=5, padx=10, pady=(5, 5))
        self.return_btn = customtkinter.CTkButton(self.tabview.tab("Output Location"), text="Back", command=self.back,
                                                  width=50, fg_color="gray30")
        self.return_btn.grid(row=0, column=4, padx=10, pady=(5, 5))


        # review tab
        self.tabview.tab("Review & Submit").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Review & Submit").grid_columnconfigure((0, 1, 2), weight=1)
        self.submit = customtkinter.CTkButton(self.tabview.tab("Review & Submit"), text="Submit",command=self.go_to_output_location, width=50)
        self.submit.grid(row=0, column=5, padx=10, pady=(5, 5))
        self.return_btn = customtkinter.CTkButton(self.tabview.tab("Review & Submit"), text="Back", command=self.back, width=50, fg_color="gray30")
        self.return_btn.grid(row=0, column=4 ,padx=10, pady=(5, 5))



    def go_to_output_location(self):
        tab = self.tabview.get()
        if tab == "Setup":
            self.tabview.set("Output Location")
        if tab == "Output Location":
            self.tabview.set("Review & Submit")
        return

    def back(self):
        tab = self.tabview.get()
        if tab == "Review & Submit":
            self.tabview.set("Output Location")
        if tab == "Output Location":
            self.tabview.set("Setup")
        return


if __name__ == "__main__":
    app = App()
    app.mainloop()