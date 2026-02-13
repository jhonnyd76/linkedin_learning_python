#!/usr/bin/env python3
import datetime
from xxlimited_35 import Null


# Aufgabe: Erstellen Sie eine Klasse 'BankAccount', die ein einfaches Bankkonto repräsentiert.

# 1. Die Klasse soll die folgenden Attribute (Member-Variablen) haben:
#    - Inhaber: Der Name des Kontoinhabers (öffentlich).
#    - Kontonummer: Eine eindeutige Kontonummer (öffentlich).
#    - __kontostand: Der aktuelle Kontostand (nicht öffentlich).

# 2. Implementieren Sie die folgenden Methoden:
#    - __init__: Initialisiert den Kontoinhaber, die Kontonummer und den anfänglichen Kontostand.
#    - einzahlen: Erhöht den Kontostand um einen bestimmten Betrag.
#    - abheben: Verringert den Kontostand um einen bestimmten Betrag, wenn genügend Guthaben vorhanden ist.
#    - get_kontostand: Gibt den aktuellen Kontostand zurück.

# 3. Implementieren Sie außerdem eine Methode __str__, die eine benutzerfreundliche Darstellung des Kontos zurückgibt.

# Optional:
# - Erstellen Sie eine Methode, die Transaktionen protokolliert und eine Liste von Ein- und Auszahlungen ausgibt.

class BankAccount:

    def __init__(self, owner: str, account_number: str):
        self.owner = owner
        self.account_number = account_number
        self._balance = 0
        self._transactions = []
        print(f"Account with {self.account_number} created for {self.owner}")

    def __str__(self):
        return f"Account with {self.account_number}"


    def log_transaction(self, account_transaction: dict):
        self._transactions.append(account_transaction)

    def transactions_print(self):
        acc_transactions_string = f"""
-----------------------------------------------------------------------------
Accounttransactions of Account-Nr.: {self.account_number}
Account-Owner: {self.owner}
"""

        for acc_trans in self._transactions:
            try:
                if acc_trans['account'] != Null and acc_trans['direction'] == 'receive':
                    acc_transactions_string += f"Date: {acc_trans['timestamp']} | {acc_trans['direction']} from {acc_trans['account']} | Amount: {acc_trans['amount']} € | Balance: {acc_trans['balance']} € |  \n"
                elif acc_trans['account'] and acc_trans["direction"] == 'transfer':
                    acc_transactions_string += f"Date: {acc_trans['timestamp']} | {acc_trans['direction']} to {acc_trans['account']} | Amount: {acc_trans['amount']} € | Balance: {acc_trans['balance']} € | \n"
            except KeyError:
                acc_transactions_string += f"Date: {acc_trans['timestamp']} | {acc_trans['direction']} | Amount: {acc_trans['amount']} € | Balance: {acc_trans['balance']} € |  \n"
        acc_transactions_string += f"============================================================================="

        print(acc_transactions_string)

    def deposit(self, amount: float):
        self.set_balance(amount)
        self.set_log_transaction_list(amount)

    def withdraw(self, amount: float):
        if self.get_balance() >= amount:
            self.set_balance(-amount)
            self.set_log_transaction_list(amount, "withdraw")
        else:
            print(f"Withdrawal of {amount} € failed: You have {self.get_balance()} € left in your account.")

    def get_balance(self) -> float:
        return self._balance

    def set_balance(self, amount: float):
        self._balance += amount

    def transfer(self, amount: float, target_account: BankAccount):
        if self.get_balance() >= amount:
            self.set_balance(-amount)
            target_account.receive(amount, self)
            self.set_log_transaction_list(amount, "transfer", target_account)

    def receive(self, amount: float, source_account: BankAccount):
        self.set_balance(amount)
        self.set_log_transaction_list(amount, "receive", source_account)


    def set_log_transaction_list(self,amount: float, trans_direction: str = "deposit", account: BankAccount = None):
        if trans_direction == "deposit":
            self.log_transaction({"timestamp": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                  "balance": self.get_balance(),
                                  "amount": amount,
                                  "direction": trans_direction,})
        elif trans_direction == "withdraw":
            self.log_transaction({"timestamp": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                  "balance": self.get_balance(),
                                  "amount": amount,
                                  "direction": trans_direction,})
        elif trans_direction == "transfer":
            self.log_transaction({"timestamp": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                  "balance": self.get_balance(),
                                  "amount": amount,
                                  "direction": trans_direction,
                                  "account": account})
        elif trans_direction == "receive":
            self.log_transaction({"timestamp": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                  "balance": self.get_balance(),
                                  "amount": amount,
                                  "direction": trans_direction,
                                  "account": account})


k1 = BankAccount("Gion Desax", "99348489")
print(k1)
k1.deposit(100)
k1.withdraw(50)
k1.deposit(200)
k1.deposit(100)
print(k1)
k1.withdraw(500)
print(k1)
k2 = BankAccount("Patrizia Desax", "22394995")
k2.deposit(1000)
k2.transfer(200, k1)
k1.transactions_print()
k2.transactions_print()
k1.deposit(10000)
k1.transfer(200, k2)
k2.transactions_print()
k1.transactions_print()
k2.withdraw(500)
k1.transfer(1000,k2)
k2.transactions_print()
