
import tkinter as tk
from tkinter import messagebox
import datetime
import os
import platform
import random
import subprocess

from bank_account import BankAccount


class BankApp:
    def __init__(self, root):
        self.root = root
        self.account = BankAccount()
        self.account_bal = self.account.balance
        self.account_number = self.account.account_number

        self.root.title("Bank of BODEX")
        self.create_widgets()

    def create_widgets(self):
        self.balance_label = tk.Label(
            self.root,
            text=f"Account Balance: ${self.account_bal}"
        )
        self.balance_label.pack(pady=10)

        self.task_label = tk.Label(
            self.root,
            text="Select a task:"
        )
        self.task_label.pack()

        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(pady=10)

        tk.Button(
            self.task_frame,
            text="Check Balance",
            command=self.check_balance
        ).pack(side=tk.LEFT, padx=3)

        tk.Button(
            self.task_frame,
            text="Deposit",
            command=self.deposit
        ).pack(side=tk.LEFT, padx=3)

        tk.Button(
            self.task_frame,
            text="Withdraw",
            command=self.withdraw
        ).pack(side=tk.LEFT, padx=3)

        tk.Button(
            self.task_frame,
            text="Transfer",
            command=self.transfer
        ).pack(side=tk.LEFT, padx=3)

    def update_balance(self):
        self.account_bal = self.account.balance
        self.balance_label.config(
            text=f"Account Balance: ${self.account_bal}"
        )

    def print_receipt_file(self, file_path):
        """Send the receipt to the system printer."""
        try:
            system = platform.system()

            if system == "Windows":
                os.startfile(os.path.abspath(file_path), "print")
            elif system == "Darwin":
                subprocess.run(["lp", file_path], check=True)
            else:
                subprocess.run(["lpr", file_path], check=True)

            messagebox.showinfo(
                "Print",
                "Receipt sent to printer."
            )

        except (OSError, subprocess.SubprocessError) as error:
            messagebox.showerror(
                "Print Error",
                f"Could not print receipt: {error}"
            )

    def generate_receipt(self, transaction_type, amount=0, recipient=None):
        """Create, display, and save a transaction receipt."""
        time_now = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        ref_no = random.randint(100000, 999999)

        receipt_text = f"""
=======================================
       BANK OF BODEX - RECEIPT
=======================================
Branch       : Main Branch
Account No.  : {self.account_number}
Ref Number   : {ref_no}
Date & Time  : {time_now}
---------------------------------------
Transaction  : {transaction_type}
Amount       : ${amount}
"""

        if recipient:
            receipt_text += f"Recipient    : {recipient}\n"

        receipt_text += f"""Closing Bal  : ${self.account_bal}
---------------------------------------
Thank you for banking with BODEX
=======================================
"""

        file_path = os.path.abspath("last_receipt.txt")

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(receipt_text)

        with open(
            "transaction_receipts.txt", "a", encoding="utf-8"
        ) as file:
            file.write(receipt_text + "\n\n")

        receipt_window = tk.Toplevel(self.root)
        receipt_window.title("Transaction Receipt")

        receipt_box = tk.Text(
            receipt_window,
            width=50,
            height=20,
            font=("Courier", 9)
        )
        receipt_box.pack(padx=10, pady=10)
        receipt_box.insert(tk.END, receipt_text)
        receipt_box.config(state="disabled")

        tk.Button(
            receipt_window,
            text="Print Receipt",
            command=lambda: self.print_receipt_file(file_path)
        ).pack(pady=5)

        print(receipt_text)

    def check_balance(self):
        messagebox.showinfo(
            "Account Balance",
            f"Your account balance is: ${self.account_bal}"
        )
        self.generate_receipt("Balance Check")

    def deposit(self):
        self.deposit_window = tk.Toplevel(self.root)
        self.deposit_window.title("Deposit")

        tk.Label(
            self.deposit_window,
            text="Enter amount to deposit:"
        ).pack(pady=5)

        self.deposit_entry = tk.Entry(self.deposit_window)
        self.deposit_entry.pack(pady=5)

        tk.Button(
            self.deposit_window,
            text="Deposit",
            command=self.deposit_amount
        ).pack(pady=5)

    def deposit_amount(self):
        try:
            amount = int(self.deposit_entry.get())
            self.account.deposit(amount)
            self.update_balance()

            messagebox.showinfo(
                "Deposit",
                f"You deposited ${amount}.\n"
                f"New balance: ${self.account_bal}"
            )

            self.generate_receipt("Deposit", amount)
            self.deposit_window.destroy()

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def withdraw(self):
        self.withdraw_window = tk.Toplevel(self.root)
        self.withdraw_window.title("Withdraw")

        tk.Label(
            self.withdraw_window,
            text="Enter amount to withdraw:"
        ).pack(pady=5)

        self.withdraw_entry = tk.Entry(self.withdraw_window)
        self.withdraw_entry.pack(pady=5)

        tk.Button(
            self.withdraw_window,
            text="Withdraw",
            command=self.withdraw_amount
        ).pack(pady=5)

    def withdraw_amount(self):
        try:
            amount = int(self.withdraw_entry.get())
            self.account.withdraw(amount)
            self.update_balance()

            messagebox.showinfo(
                "Withdrawal",
                f"You withdrew ${amount}.\n"
                f"New balance: ${self.account_bal}"
            )

            self.generate_receipt("Withdrawal", amount)
            self.withdraw_window.destroy()

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def transfer(self):
        self.transfer_window = tk.Toplevel(self.root)
        self.transfer_window.title("Transfer")

        tk.Label(
            self.transfer_window,
            text="Enter amount to transfer:"
        ).pack(pady=5)

        self.transfer_entry = tk.Entry(self.transfer_window)
        self.transfer_entry.pack(pady=5)

        tk.Label(
            self.transfer_window,
            text="Enter recipient's account number:"
        ).pack(pady=5)

        self.user_entry = tk.Entry(self.transfer_window)
        self.user_entry.pack(pady=5)

        tk.Button(
            self.transfer_window,
            text="Transfer",
            command=self.transfer_amount
        ).pack(pady=5)

    def transfer_amount(self):
        try:
            amount = int(self.transfer_entry.get())
            recipient = self.user_entry.get().strip()

            self.account.transfer(amount, recipient)
            self.update_balance()

            messagebox.showinfo(
                "Transfer",
                f"You simulated a transfer of ${amount} "
                f"to account {recipient}.\n"
                f"New balance: ${self.account_bal}"
            )

            self.generate_receipt("Transfer", amount, recipient)
            self.transfer_window.destroy()

        except ValueError as error:
            messagebox.showerror("Error", str(error))

