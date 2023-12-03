<div align="center">
<h1 align="center">
<img src="./images/logo_white.png" width="300" />
<br>MASSAR-DIRECTION-SAGOUBOT</h1>
<h3>◦ Simplify navigating with Massar Direction Sagoubot!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/.ENV-ECD53F.svg?style=flat-square&logo=dotenv&logoColor=black" alt=".ENV" />
<img src="https://img.shields.io/badge/Selenium-43B02A.svg?style=flat-square&logo=Selenium&logoColor=white" alt="Selenium" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat-square&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat-square&logo=Pytest&logoColor=white" alt="Pytest" />
</p>
<img src="https://img.shields.io/github/license/medsagou/massar-direction-sagoubot?style=flat-square&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/medsagou/massar-direction-sagoubot?style=flat-square&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/medsagou/massar-direction-sagoubot?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/medsagou/massar-direction-sagoubot?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents

- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
  - [🔧 Installation](#-installation)
  - [🤖 Running massar-direction-sagoubot](#-running-massar-direction-sagoubot)
  - [🧪 Tests](#-tests)
- [🛣 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The repository "massar-direction-sagoubot" is a project that automates the process of filling absence data for multiple classes in a web application. It includes modules for absences, class files, GUI, interaction, reading and scanning files, menu, class list modules, printing, and UI. The project offers a user-friendly interface and relies on web scraping techniques with the Selenium library to interact with a web page. Its value proposition lies in saving time and effort by automating the manual task of filling absence data, enhancing the efficiency of teachers and administrators.

---

## 📦 Features

|     | Feature             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ⚙️  | **Architecture**    | The codebase follows a modular architecture, with separate classes for absences, class files, GUI, interaction, reading and scanning files, menu, and more. It also includes a database and images folder. The codebase utilizes web scraping techniques with Selenium library to interact with web pages. Overall, it follows a structured approach with clear separation of concerns.                                                                     |
| 📄  | **Documentation**   | The codebase lacks comprehensive documentation. Without detailed comments or documentation, it becomes challenging for developers to understand the codebase and its functionalities.                                                                                                                                                                                                                                                                       |
| 🔗  | **Dependencies**    | The codebase relies on several external libraries and systems such as Selenium, pandas, openpyxl, and pytest. These dependencies enhance the codebase's functionality and enable web scraping, file reading, data manipulation, and testing capabilities. Care should be taken to keep these dependencies up to date to ensure compatibility and security.                                                                                                  |
| 🧩  | **Modularity**      | The codebase demonstrates good modularity through the organization into separate classes and modules. Each file is responsible for a specific functionality, making it easier to understand, maintain, and test different components of the system. It can benefit from further separating concerns and applying design patterns to achieve even higher modularity.                                                                                         |
| 🧪  | **Testing**         | The codebase utilizes the pytest library for testing. It includes a test file, "test_massar_app.py," which contains tests for a web application. The tests validate the page title and perform a search on the website. Having tests in place ensures the correctness of the code and facilitates future modifications and enhancements. However, additional testing strategies like integration and unit tests would enhance the overall testing coverage. |
| ⚡️ | **Performance**     | The codebase performance depends on the specific functionalities implemented within each module. Since web scraping is involved, it is crucial to optimize the web interactions to minimize resource usage and achieve better speed and efficiency. Regular performance testing, optimization, and utilizing caching mechanisms can further improve the system's performance.                                                                               |
| 🔐  | **Security**        | The codebase does not include explicit security measures. When dealing with web scraping, it is essential to ensure secure interactions with websites and handle user credentials with care. Implementing security best practices such as secure storage of sensitive data and strong encryption can enhance the security of the system.                                                                                                                    |
| 🔀  | **Version Control** | The codebase relies on version control using Git for managing source code changes. However, the analysis does not provide information on specific version control strategies and tools used within the project. Proper usage of Git for branching, merging, and code reviews can streamline collaboration and code management.                                                                                                                              |
| 🔌  | **Integrations**    | The system interacts with external systems and services through web scraping and file reading capabilities. It integrates with websites, external databases, and Excel files to extract, modify, and save data. The codebase needs to handle these integrations carefully to ensure data integrity and validate the interactions with external systems.                                                                                                     |
| 📶  | **Scalability**     | The codebase's ability to handle growth largely depends on the specific functionalities implemented                                                                                                                                                                                                                                                                                                                                                         |

---

## 📂 Repository Structure

```sh
└── massar-direction-sagoubot/
    ├── .env
    ├── Absences.py
    ├── Class_Files.py
    ├── db/
    │   └── menu.txt
    ├── GUI.py
    ├── images/
    ├── interaction.py
    ├── main.py
    ├── Menu.py
    ├── Module_Classe_Liste.py
    ├── print_sagou.py
    ├── Read_XLSB_File.py
    ├── requirements.txt
    ├── scan_absence.py
    ├── test_massar_app.py
    ├── ui.py
    └── other_utilities.py

```

---

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [.env](https://github.com/medsagou/massar-direction-sagoubot/blob/main/.env)                                     | This code includes files related to a Massar Direction Sagoubot application. It consists of modules for absences, class files, GUI, interaction, reading and scanning files, menu, class list modules, printing, and UI. It also includes a database folder, images folder, and various test files. The.env file contains variables for email, password, and official site URL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Absences.py](https://github.com/medsagou/massar-direction-sagoubot/blob/main/Absences.py)                       | The code is a class called "Absence" that contains methods for filling the absence data for each student in a specific class. It uses web scraping techniques with the Selenium library to interact with a web page. The class has methods for navigating to the page, selecting different options for the type of teaching, cycle, level, and class, and then filling the absence data for each student on a given date. The data is retrieved from an external file using the "Scan_Absences" class. Overall, the code automates the process of filling absence data for multiple classes in a web application.                                                                                                                                                                                                                                                         |
| [Class_Files.py](https://github.com/medsagou/massar-direction-sagoubot/blob/main/Class_Files.py)                 | The code defines two classes: `C_Dossier` and `C_File`. `C_Dossier` contains methods for working with directories, such as getting the current directory, checking if a directory exists, changing the current directory, and creating a new directory.`C_File` contains methods for working with files, including checking if a file exists and specifying the name of a file. The class also has a constructor that allows for setting the file name and separators for the file's elements.                                                                                                                                                                                                                                                                                                                                                                            |
| [GUI.py](https://github.com/medsagou/massar-direction-sagoubot/blob/main/GUI.py)                                 | Exception:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [interaction.py](https://github.com/medsagou/massar-direction-sagoubot/blob/main/interaction.py)                 | The code is a part of a directory tree for a project called "massar-direction-sagoubot." The specific file is "interaction.py." The code defines a class called "Massar_Direction_Sagou," which serves as the main interaction point for the program. It imports necessary modules like "os," "sys," and "dotenv." The class contains methods that facilitate actions like getting the driver, opening the site, filling username and password fields, submitting the form, checking for errors, closing the tab, and ending the program.The "main_interaction" method executes a sequence of actions, such as getting the driver, opening the site, filling login credentials, and submitting the form.                                                                                                                                                                  |
| [main.py](https://github.com/medsagou/massar-direction-sagoubot/blob/main/main.py)                               | The code is the main script for a directory tree called "massar-direction-sagoubot". It imports several modules and starts a user interface. It then presents a main menu to the user, allowing them to choose from different options. Depending on the option chosen, the code executes different functionalities such as reading data from a database, interacting with a web page, or handling absences. The code loops back to the main menu after each action, giving the user the ability to perform multiple tasks. The script can be executed by running the main() function.                                                                                                                                                                                                                                                                                     |
| [Menu.py](https://github.com/medsagou/massar-direction-sagoubot/blob/main/Menu.py)                               | The code defines a class called "Menu" that manages menus. It has methods to print a menu, prompt for user choice, and retrieve menu options from a file. The class takes a list of options as input, and each option is associated with a number. The user can select an option by entering the corresponding number. The code also includes a method to read menu options from a text file and populate the menu with them.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Module_Classe_Liste.py](https://github.com/medsagou/massar-direction-sagoubot/blob/main/Module_Classe_Liste.py) | The code in Module_Classe_Liste.py defines a class called C_Liste that inherits from the list class. It provides methods for displaying the contents of the list, converting a string to a list using a specified separator, converting a list to a string using the same separator, and changing an element in the list. The class can be used to manipulate and work with lists of elements.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [print_sagou.py](https://github.com/medsagou/massar-direction-sagoubot/blob/main/print_sagou.py)                 | The code in "print_sagou.py" provides functions for printing different types of messages and data structures.-"print_error" prints an error message with red formatting-"print_success" prints a success message with green formatting-"print_info" prints an info message with blue formatting-"print_dict" prints the key-value pairs of a dictionary in a formatted manner-"print_full_df" prints a pandas dataframe with all rows and columns displayed                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Read_XLSB_File.py](https://github.com/medsagou/massar-direction-sagoubot/blob/main/Read_XLSB_File.py)           | The code provided is a class called `Read_Db` that is responsible for reading and manipulating data from an Excel file. The core functionalities of the class include:-Obtaining data from an Excel file (`input_file`) in various formats such as xlsb and xls.-Extracting and parsing specific data from the Excel file based on specified column keys.-Creating new Excel sheets based on the extracted data.-Writing data to specific cells in the created sheets.-Saving the modified Excel file.The class utilizes various libraries such as pandas, openpyxl, and xlrd to perform these operations.                                                                                                                                                                                                                                                                |
| [requirements.txt](https://github.com/medsagou/massar-direction-sagoubot/blob/main/requirements.txt)             | The code represents a directory tree with various files and folders. The main functionalities include processing absences, interacting with a GUI, reading XLSB files, scanning for absences, and managing modules and classes. Additionally, there are utilities for printing and validating email addresses. The code also includes dependencies specified in the requirements.txt file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [scan_absence.py](https://github.com/medsagou/massar-direction-sagoubot/blob/main/scan_absence.py)               | The code in scan_absence.py defines a class called Scan_Absences. This class is a subclass of the Read_Db class and inherits its attributes and methods. The Scan_Absences class has several instance variables such as starter_col, ending_col, starter_row, ending_row, workbook, classe, worksheet_class, classe_numbers, and scaned_area.The class also has two methods: get_absence_day_per_student and get_absence_day_per_student2. These methods process data from an Excel workbook to retrieve absence data for each student in a specific class. The methods extract the absence data from the workbook based on the provided class name and scaned area and return the absence data as well as the start and end dates.The code also imports the Read_Db class from the Read_XLSB_File module and the get_columns_for_two function from the utilities module. |
| [test_massar_app.py](https://github.com/medsagou/massar-direction-sagoubot/blob/main/test_massar_app.py)         | This code is a test class for running Selenium tests on a web application. It uses the pytest library and the Selenium WebDriver. The setup fixture initializes the web driver before each test and makes it available to the test class. The test_title method opens a website and asserts that the page title contains "Example Domain". The test_search method performs a search on the website and asserts that the search term is present in the page title.                                                                                                                                                                                                                                                                                                                                                                                                         |
| [ui.py](https://github.com/medsagou/massar-direction-sagoubot/blob/main/ui.py)                                   | The code defines a class called "User_Interface" with several methods that handle the main menu and submenus for a user interface. The "clear_screen" method clears the terminal screen. The "main_page" method displays a list of classes and the number of students in each class. The "main_menu", "menu01", "classes_menu", and "menu_valider" methods print different menus and return the user's choice and returned value from each menu. The code also imports modules and libraries for additional functionalities.                                                                                                                                                                                                                                                                                                                                              |
| [utilities.py](https://github.com/medsagou/massar-direction-sagoubot/blob/main/utilities.py)                     | Exception:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [menu.txt](https://github.com/medsagou/massar-direction-sagoubot/blob/main/db\menu.txt)                          | The code is a directory tree that contains various files related to a Massar direction SagouBot application. The specific code snippet is a path to a "menu.txt" file located in the "db" directory. The file seems to contain menu options for absence tracking related to different classes. The code snippet shows three menu options: "Absence par class," "La liste a remplir;Absence par class," and "Valider.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

</details>

---

## 🚀 Getting Started

**_Dependencies_**

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Dependency 1`

`- ℹ️ Dependency 2`

`- ℹ️ ...`

### 🔧 Installation

1. Clone the massar-direction-sagoubot repository:

```sh
git clone https://github.com/medsagou/massar-direction-sagoubot
```

2. Change to the project directory:

```sh
cd massar-direction-sagoubot
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

### 🤖 Running massar-direction-sagoubot

```sh
python main.py
```

### 🧪 Tests

```sh
pytest
```

---

## 🛣 Project Roadmap

> - [x] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Implement Y`
> - [ ] `ℹ️ ...`

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/medsagou/massar-direction-sagoubot/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/medsagou/massar-direction-sagoubot/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/medsagou/massar-direction-sagoubot/issues)**: Submit bugs found or log feature requests for MEDSAGOU.

#### _Contributing Guidelines_

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

## 📄 License

This project is protected under the [GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/) License. For more details, refer to the [LICENSE](./LICENSE) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---
