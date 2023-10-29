<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>MASSAR-SAGOUBOT</h1>
<h3>◦ By: MedSagou</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python" />
</p>
<img src="https://img.shields.io/github/license/medsagou/massar-sagoubot?style=flat-square&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/medsagou/massar-sagoubot?style=flat-square&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/medsagou/massar-sagoubot?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/medsagou/massar-sagoubot?style=flat-square&color=5D6D7E" alt="GitHub top language" />
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
    - [🤖 Running massar-sagoubot](#-running-massar-sagoubot)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The "massar-sagoubot" repository is a Python project that provides automation capabilities for interacting with a Massar website. It includes functionality for automating the extraction and saving of class lists from the website. The codebase consists of several modules, each responsible for specific tasks, such as interacting with directories, working with files, automating website interaction, and extracting and saving class lists. This project is valuable for anyone who needs to automate the process of extracting and saving class lists from a Massar website.

---

## 📦 Features

**Key Features:**

- **Effortless Class List Extraction**: Massar Sagoubot automates the process of retrieving class lists, allowing teachers to focus on what truly matters – teaching.

- **Customization**: Teachers have the flexibility to customize the bot's settings to match their unique needs and preferences.

- **User-Friendly Interface**: The bot is designed with an intuitive and accessible interface, ensuring that both tech-savvy and non-technical educators can harness its power.

- **Time-Saving Automation**: With repetitive administrative tasks handled by the bot, teachers can invest more time in the classroom.

---


## 📂 Repository Structure

```sh
└── massar-sagoubot/
    ├── Class_Files.py
    ├── interaction.py
    ├── list_reader.py
    ├── main.py
    ├── Menu.py
    ├── Module_Classe_Liste.py
    ├── print_sagou.py
    └── ui.py

```

---


## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                    |-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Class_Files.py](https://github.com/medsagou/massar-sagoubot/blob/main/Class_Files.py)                 | The code consists of two class definitions: C_Dossier and C_File. The C_Dossier class includes methods to interact with directories, such as getting the current directory, checking if a directory exists, changing the current directory, and creating a new directory. It utilizes the os and os.path modules.The C_File class is used to work with files. It includes methods to check if a file exists, specify the name of a file, and instantiate a new file object. The class also allows for specifying a separator for file elements. |
| [interaction.py](https://github.com/medsagou/massar-sagoubot/blob/main/interaction.py)                 | The code defines a class called "Massar_Sagou" that contains methods for automating the interaction with a website. The class has methods for initializing the web driver, opening the website, filling in the username and password fields, submitting the login form, checking for login errors, extracting class information from the main page, and exporting data. The class also has methods for closing the web driver and exiting the program.                                                                                          |
| [list_reader.py](https://github.com/medsagou/massar-sagoubot/blob/main/list_reader.py)                 | The code above implements a class called `List_Reader`, which is responsible for extracting and saving class lists from a Massar website. It uses the Selenium library to automate the web scraping process. The `List_Reader` class has methods for navigating to the list page, selecting different class options, and extracting the data from the table. The `main_list_reader` method calls the other methods in the correct order to perform the desired functionality.                                                                   |
| [main.py](https://github.com/medsagou/massar-sagoubot/blob/main/main.py)                               | The main file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Menu.py](https://github.com/medsagou/massar-sagoubot/blob/main/Menu.py)                               | Menu management                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Module_Classe_Liste.py](https://github.com/medsagou/massar-sagoubot/blob/main/Module_Classe_Liste.py) | List management                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [print_sagou.py](https://github.com/medsagou/massar-sagoubot/blob/main/print_sagou.py)                 | Custom printing Functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [ui.py](https://github.com/medsagou/massar-sagoubot/blob/main/ui.py)                                   | User interface                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

</details>

---

## 🚀 Getting Started

### 🔧 Installation

1. Clone the massar-sagoubot repository:
```sh
git clone https://github.com/medsagou/massar-sagoubot
```

2. Change to the project directory:
```sh
cd massar-sagoubot
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Running massar-sagoubot

```sh
python main.py
```






---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/medsagou/massar-sagoubot/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/medsagou/massar-sagoubot/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/medsagou/massar-sagoubot/issues)**: Submit bugs found or log feature requests for medsagou.

#### *Contributing Guidelines*

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


This project is protected under the [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/) License.

---

## 👏 Acknowledgments

- **Previous Work:** If your project builds upon or is inspired by previous work, give credit to the original authors or researchers.

 - **Self-Acknowledgment:** Don't forget to acknowledge your own efforts and commitment to the project. It's an opportunity to reflect on your own growth and learning throughout the project.

[**Return**](#Top)

---

