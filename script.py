#!/usr/bin/env python3
import datetime


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
    account_transactions = []

    def __init__(self, owner: str, account_number: str):
        self.owner = owner
        self.account_number = account_number
        self._balance = 0
        print(f"Account with {self.account_number} created for {self.owner}")

    def __str__(self):
        return f"Account with {self.account_number} belongs to {self.owner} and has a balance of {self._balance:.2f} €"

    @classmethod
    def log_transaction(cls, account_transaction: dict, trans_direction: str = "deposit"):
        cls.account_transactions.append(account_transaction)
        for acc_trans in cls.account_transactions:
            acc_trans_str = f"{acc_trans['timestamp']} | "
            if trans_direction == "deposit":
                acc_trans_str += f"Deposit {acc_trans['amount']} € | "
            else:
                acc_trans_str += f"Withdraw {acc_trans['amount']} € | "
            acc_trans_str += f"Balance: {acc_trans['balance']} €"
            print(acc_trans_str)



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

    def set_log_transaction_list(self,amount: float, trans_direction: str = "deposit"):
        if trans_direction == "deposit":
            self.log_transaction({"timestamp": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                  "balance": self.get_balance(),
                                  "amount": amount})
        else:
            self.log_transaction({"timestamp": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                  "balance": self.get_balance(),
                                  "amount": amount}, "withdraw")


k1 = BankAccount("Gion Desax", "99348489")
print(k1)
k1.deposit(100)
k1.withdraw(50)
k1.deposit(200)
k1.deposit(100)
print(k1)
k1.withdraw(500)
print(k1)
