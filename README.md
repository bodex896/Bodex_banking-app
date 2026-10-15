Python Banking App

A simple banking application built with Python and Tkinter. It allows users to simulate basic banking transactions through a graphical user interface.

Features

- Check account balance
- Deposit money
- Withdraw money
- Simulate money transfers
- Generate transaction receipts
- Save transaction receipts to text files
- Print transaction receipts

Project Structure

python-banking-app/
├── README.md
├── .gitignore
└── src/
    ├── main.py
    ├── banking_app.py
    └── bank_account.py

File Descriptions

- "README.md" — Explains the project, its features, and how to run it.
- ".gitignore" — Prevents unnecessary files, such as Python cache files and local receipt files, from being uploaded to GitHub.
- "main.py" — Starts the application and opens the main window.
- "banking_app.py" — Contains the Tkinter graphical interface, transaction forms, receipt generation, and printing functions.
- "bank_account.py" — Handles account operations, including deposits, withdrawals, balance updates, and simulated transfers.

Technologies Used

- Python
- Tkinter
- Object-Oriented Programming
- Git and GitHub

How to Run

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the command:

python src/main.py

If your system uses "python3", run:

python3 src/main.py

Important Notes

This is an educational project created to practise Python programming and GUI development. Transactions are simulated; the application does not connect to a real bank or transfer actual money.

The account balance resets when the application restarts because database storage has not yet been implemented.

Future Improvements

- Add SQLite database storage.
- Add user registration and login.
- Save account balances between sessions.
- Improve input validation and error handling.

Author

Olabode

Aspiring Software Engineer | Python Developer
