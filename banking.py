import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Dictionary to store account details
accounts = {}

# ---------------- FUNCTIONS ---------------- #

def create_account():
    acc_no = entry_acc.get().strip()
    name = entry_name.get().strip()
    balance = entry_balance.get().strip()

    if not acc_no or not name or not balance:
        messagebox.showerror("Error", "All fields are required!")
        return

    if not acc_no.isdigit():
        messagebox.showerror("Error", "Account number must be numeric!")
        return

    if acc_no in accounts:
        messagebox.showerror("Error", "Account already exists!")
        return

    try:
        balance = float(balance)
        if balance < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter a valid balance!")
        return

    accounts[acc_no] = {
        "name": name,
        "balance": balance,
        "transactions": [f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} - Account created with â¹{balance}"]
    }

    messagebox.showinfo("Success", "Account Created Successfully!")
    clear_fields()


def deposit():
    acc_no = entry_acc.get().strip()
    amount = entry_amount.get().strip()

    if acc_no not in accounts:
        messagebox.showerror("Error", "Account not found!")
        return

    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter valid deposit amount!")
        return

    accounts[acc_no]["balance"] += amount
    accounts[acc_no]["transactions"].append(
        f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} - Deposited â¹{amount}"
    )

    messagebox.showinfo("Success",
                        f"Deposited Successfully!\nNew Balance: â¹{accounts[acc_no]['balance']:.2f}")
    entry_amount.delete(0, tk.END)


def withdraw():
    acc_no = entry_acc.get().strip()
    amount = entry_amount.get().strip()

    if acc_no not in accounts:
        messagebox.showerror("Error", "Account not found!")
        return

    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter valid withdrawal amount!")
        return

    if accounts[acc_no]["balance"] < amount:
        messagebox.showerror("Error", "Insufficient Balance!")
        return

    accounts[acc_no]["balance"] -= amount
    accounts[acc_no]["transactions"].append(
        f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} - Withdrawn â¹{amount}"
    )

    messagebox.showinfo("Success",
                        f"Withdrawn Successfully!\nNew Balance: â¹{accounts[acc_no]['balance']:.2f}")
    entry_amount.delete(0, tk.END)


def check_balance():
    acc_no = entry_acc.get().strip()

    if acc_no not in accounts:
        messagebox.showerror("Error", "Account not found!")
        return

    name = accounts[acc_no]["name"]
    balance = accounts[acc_no]["balance"]

    messagebox.showinfo("Account Details",
                        f"Account Holder: {name}\nCurrent Balance: â¹{balance:.2f}")


def delete_account():
    acc_no = entry_acc.get().strip()

    if acc_no not in accounts:
        messagebox.showerror("Error", "Account not found!")
        return

    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this account?")
    if confirm:
        del accounts[acc_no]
        messagebox.showinfo("Success", "Account Deleted Successfully!")
        clear_fields()


def show_transactions():
    acc_no = entry_acc.get().strip()

    if acc_no not in accounts:
        messagebox.showerror("Error", "Account not found!")
        return

    transactions = accounts[acc_no]["transactions"]

    if not transactions:
        messagebox.showinfo("Transactions", "No transactions yet.")
    else:
        messagebox.showinfo("Transactions", "\n".join(transactions))


def clear_fields():
    entry_acc.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_balance.delete(0, tk.END)
    entry_amount.delete(0, tk.END)


# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()
root.title("Banking Management System")
root.geometry("420x550")
root.config(bg="lightblue")
root.resizable(False, False)

tk.Label(root, text="Banking Management System",
         font=("Arial", 16, "bold"), bg="lightblue").pack(pady=15)

frame = tk.Frame(root, bg="lightblue")
frame.pack()

tk.Label(frame, text="Account Number", bg="lightblue").grid(row=0, column=0, sticky="w")
entry_acc = tk.Entry(frame)
entry_acc.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Name", bg="lightblue").grid(row=1, column=0, sticky="w")
entry_name = tk.Entry(frame)
entry_name.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Initial Balance", bg="lightblue").grid(row=2, column=0, sticky="w")
entry_balance = tk.Entry(frame)
entry_balance.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Amount", bg="lightblue").grid(row=3, column=0, sticky="w")
entry_amount = tk.Entry(frame)
entry_amount.grid(row=3, column=1, pady=5)

tk.Button(root, text="Create Account", command=create_account,
          bg="green", fg="white", width=20).pack(pady=5)

tk.Button(root, text="Deposit", command=deposit,
          bg="blue", fg="white", width=20).pack(pady=5)

tk.Button(root, text="Withdraw", command=withdraw,
          bg="red", fg="white", width=20).pack(pady=5)

tk.Button(root, text="Check Balance", command=check_balance,
          bg="purple", fg="white", width=20).pack(pady=5)

tk.Button(root, text="Delete Account", command=delete_account,
          bg="black", fg="white", width=20).pack(pady=5)

tk.Button(root, text="Transaction History",
          command=show_transactions,
          bg="orange", fg="white", width=20).pack(pady=5)

tk.Button(root, text="Exit", command=root.quit,
          bg="gray", fg="white", width=20).pack(pady=10)

root.mainloop()
