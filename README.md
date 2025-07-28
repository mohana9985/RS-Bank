# RS-Bank: A Simple Banking Application

RS-Bank is a desktop banking application built with Python's `tkinter` library for the graphical user interface (GUI) and `pymysql` for database interaction. It provides basic banking functionalities for users to manage their accounts.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Database Setup](#database-setup)
- [Installation and Usage](#installation-and-usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Features

*   **User Authentication:**
    *   User registration with name, date of birth, phone number, email, and password.
    *   Secure login for existing users.
*   **Account Management:**
    *   Open a new bank account.
    *   View detailed account information (name, DOB, balance).
    *   Deposit funds into an account.
    *   Withdraw funds from an account.
    *   Remove/close an existing account.
*   **Account Overview:**
    *   View a summary of all accounts, including the total number of accounts, active accounts, and closed accounts.

## Prerequisites

Before you begin, ensure you have met the following requirements:

*   **Python 3.x:** You have Python 3 installed on your system.
*   **MySQL Server:** You have a running instance of MySQL server.
*   **Python Libraries:** You need to install the following Python libraries:
    *   `tkinter` (usually comes with Python)
    *   `pymysql`
    *   `python-dateutil`
    *   `cryptography`

## Database Setup

You need to set up a MySQL database to store the application's data.

1.  **Create a Database:**
    Create a new database named `bank`.

    ```sql
    CREATE DATABASE bank;
    ```

2.  **Create Tables:**
    Create the `login` and `accounts` tables within the `bank` database.

    *   **`login` table:** Stores user registration and login credentials.

        ```sql
        CREATE TABLE login (
            fullname VARCHAR(255) PRIMARY KEY,
            password VARCHAR(255),
            dob DATE,
            nickname VARCHAR(255),
            phone VARCHAR(20),
            email VARCHAR(255)
        );
        ```

    *   **`accounts` table:** Stores bank account details.

        ```sql
        CREATE TABLE accounts (
            name VARCHAR(255),
            address VARCHAR(255),
            dob DATE,
            bal INT,
            an INT PRIMARY KEY,
            alive VARCHAR(3) DEFAULT 'yes'
        );
        ```

## Installation and Usage

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd RS-Bank
    ```

2.  **Install dependencies:**

    ```bash
    pip install pymysql python-dateutil cryptography
    ```

3.  **Configure Database Connection:**
    Open the `bank.menu.py` file and update the database connection details in all `pymysql.connect()` calls to match your MySQL setup (host, user, password, db).

    ```python
    con = pymysql.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        db="bank"
    )
    ```

4.  **Run the application:**

    ```bash
    python bank.menu.py
    ```

## Screenshots

The repository includes the following screenshots of the application's user interface:

*   `acc_open.png`: Account opening page.
*   `acc_summary.png`: Account summary view.
*   `accinfo.png`: Account information display.
*   `account_page.png`: Main account features page.
*   `bank1.png`: Login screen.
*   `deposit.png`: Deposit page.
*   `logout.png`: Logout confirmation.
*   `remacc.png`: Remove account page.
*   `withdraw.png`: Withdraw page.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
