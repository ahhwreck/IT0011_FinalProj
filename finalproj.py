import tkinter as tk
from tkinter import messagebox
import ast

class BankingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Anita MaxBank - Login")
        self.geometry("925x500+300+200")
        self.configure(bg="#2d2c3a")
        self.resizable(False, False)
        self.current_account = ""
        self.accounts_file = "accounts.txt"

        self.login_screen()

    def login_screen(self):
        # Clear existing window widgets
        self.clear_window()
        
        # Logo label
        logo = tk.Label(self, text="Anita MaxBank", bg="#2d2c3a", fg="white", font=("Montserrat", 30, "bold"))
        logo.place(x=290, y=20)

        # Login screen components
        header = tk.Label(self, text="Log In", bg="#2d2c3a", fg="white", font=("Montserrat", 14, "bold"))
        header.place(x=410, y=100)
        # Email entry and label
        email_label = tk.Label(self, text="EMAIL", bg="#2d2c3a", fg="white", font=("Montserrat", 8, "bold"))
        self.email_entry = tk.Entry(self, width=25, fg="white", bg="#2d2c3a", font=("Montserrat", 10))
        email_label.place(x=335, y=150)
        self.email_entry.place(x=335, y=170)
        # Password entry and label
        pwd_label = tk.Label(self, text="PASSWORD", bg="#2d2c3a", fg="white", font=("Montserrat", 8, "bold"))
        self.pwd_entry = tk.Entry(self, width=25, fg="white", bg="#2d2c3a", font=("Montserrat", 10), show="*")
        pwd_label.place(x=335, y=210)
        self.pwd_entry.place(x=335, y=230)
        # Login button
        login_button = tk.Button(self, width=20, pady=7, text="Log In", bg="#01f4f8", fg="#2d2c3a", border=0,
                                 font=("Montserrat", 12, "bold"), cursor="hand2", command=self.login)
        login_button.place(x=335, y=280)
        # Register label and button
        register_label = tk.Label(self, text="Don't have an account?", bg="#2d2c3a", fg="white",
                                  font=("Montserrat", 9, "bold"))
        register_button = tk.Button(self, width=6, text="Sign Up", border=False, bg="#2d2c3a", fg="#01f4f8",
                                    font=("Montserrat", 9, "bold"), cursor="hand2", command=self.signup_screen)
        register_label.place(x=345, y=340)
        register_button.place(x=495, y=340)

    def signup_screen(self):
        # Clear existing window widgets
        self.clear_window()
        
        # Logo label
        logo = tk.Label(self, text="Anita MaxBank", bg="#2d2c3a", fg="white", font=("Montserrat", 30, "bold"))
        logo.place(x=290, y=20)

        # Signup screen components
        header = tk.Label(self, text="Sign Up", bg="#2d2c3a", fg="white", font=("Montserrat", 14, "bold"))
        header.place(x=410, y=100)
        # Email entry and label
        email_label = tk.Label(self, text="EMAIL", bg="#2d2c3a", fg="white", font=("Montserrat", 8, "bold"))
        self.email_entry = tk.Entry(self, width=25, fg="white", bg="#2d2c3a", font=("Montserrat", 10))
        email_label.place(x=335, y=150)
        self.email_entry.place(x=335, y=170)
        # Password entry and label
        pwd_label = tk.Label(self, text="PASSWORD", bg="#2d2c3a", fg="white", font=("Montserrat", 8, "bold"))
        self.pwd_entry = tk.Entry(self, width=25, fg="white", bg="#2d2c3a", font=("Montserrat", 10), show="*")
        pwd_label.place(x=335, y=210)
        self.pwd_entry.place(x=335, y=230)
        # Confirm Password entry and label
        confirm_label = tk.Label(self, text="CONFIRM PASSWORD", bg="#2d2c3a", fg="white",
                                  font=("Montserrat", 8, "bold"))
        self.confirm_entry = tk.Entry(self, width=25, fg="white", bg="#2d2c3a", font=("Montserrat", 10), show="*")
        confirm_label.place(x=335, y=270)
        self.confirm_entry.place(x=335, y=290)
        # Register button
        register_button = tk.Button(self, width=20, pady=7, text="Sign Up", bg="#01f4f8", fg="#2d2c3a", border=0,
                                    font=("Montserrat", 12, "bold"), cursor="hand2", command=self.register)
        register_button.place(x=335, y=330)
        # Login label and button
        login_label = tk.Label(self, text="Already have an account?", bg="#2d2c3a", fg="white",
                               font=("Montserrat", 9, "bold"))
        login_button = tk.Button(self, width=6, text="Log In", border=False, bg="#2d2c3a", fg="#01f4f8",
                                 font=("Montserrat", 9, "bold"), cursor="hand2", command=self.login_screen)
        login_label.place(x=340, y=380)
        login_button.place(x=500, y=380)

    def main_screen(self):
        # Clear existing window widgets
        self.clear_window()

        # Logo label
        logo = tk.Label(self, text="Anita MaxBank", bg="#2d2c3a", fg="white", font=("Montserrat", 30, "bold"))
        logo.place(x=370, y=20)
        
        # Buttons for banking operations
        check_account_button = tk.Button(self, text="Check Account", command=self.check_account, height=5, width=15,
                                         font=("Monsterrat", 12, "bold"), bg="#01f4f8", fg="black", cursor="hand2")
        check_account_button.place(x=300, y=100)

        withdraw_button = tk.Button(self, text="Withdraw", command=self.withdraw, height=5, width=15,
                                    font=("Monsterrat", 12, "bold"), bg="#01f4f8", fg="black", cursor="hand2")
        withdraw_button.place(x=500, y=100)

        deposit_button = tk.Button(self, text="Deposit", command=self.deposit, height=5, width=15,
                                   font=("Monsterrat", 12, "bold"), bg="#01f4f8", fg="black", cursor="hand2")
        deposit_button.place(x=300, y=250)

        delete_account_button = tk.Button(self, text="Delete Account", command=self.delete_account, height=5, width=15,
                                          font=("Monsterrat", 12, "bold"), bg="#01f4f8", fg="black", cursor="hand2")
        delete_account_button.place(x=500, y=250)

    def clear_window(self):
        # Clear all widgets from the window
        for widget in self.winfo_children():
            widget.destroy()

    def login(self):
        # Retrieve email and password from entries
        email = self.email_entry.get()
        password = self.pwd_entry.get()

        try:
            # Attempt to open accounts file
            with open(self.accounts_file, "r") as file:
                accounts = file.readlines()

                # Iterate over accounts in file
                for account in accounts:
                    data = ast.literal_eval(account)
                    if data["email"] == email:
                        if data["password"] == password:
                            self.current_account = email
                            self.main_screen()  # Proceed to main screen if login successful
                            return
                        else:
                            messagebox.showerror(title="Invalid Account", message="Password is incorrect")
                            return
                messagebox.showerror(title="Invalid Account", message="Account not found")

        except FileNotFoundError:
            messagebox.showerror(title="Error", message="Account file not found")

    def register(self):
        # Retrieve email, password, and confirm password from entries
        email = self.email_entry.get()
        password = self.pwd_entry.get()
        confirm_password = self.confirm_entry.get()

        if password != confirm_password:
            messagebox.showerror(title="Invalid Password", message="The passwords should match")
            return

        try:
            # Check if email already exists
            with open(self.accounts_file, "r") as file:
                accounts = file.readlines()

                for account in accounts:
                    data = ast.literal_eval(account)
                    if data["email"] == email:
                        messagebox.showerror(title="Invalid Email", message="The email address is already in use")
                        return

            # If email does not exist, add account to file
            with open(self.accounts_file, "a") as file:
                data = {"email": email, "password": password, "balance": 0}
                file.write(str(data) + "\n")

            self.main_screen()  # Proceed to main screen after successful registration

        except FileNotFoundError:
            # If file doesn't exist, create file and add account
            with open(self.accounts_file, "w") as file:
                data = {"email": email, "password": password, "balance": 0}
                file.write(str(data) + "\n")
                self.main_screen()

    def check_account(self):
        try:
            with open(self.accounts_file, "r") as file:
                for line in file:
                    data = ast.literal_eval(line)
                    if data["email"] == self.current_account:
                        messagebox.showinfo(title="Account Info", message=f"Balance for {self.current_account}: {data['balance']}")
                        return
            messagebox.showerror(title="Error", message="Account not found")

        except FileNotFoundError:
            messagebox.showerror(title="Error", message="Account file not found")


    def withdraw(self):
        # Open a new window for withdrawal
        withdraw_window = tk.Toplevel(self)
        withdraw_window.title("Withdraw Money")
        withdraw_window.geometry("300x200")
        withdraw_window.configure(bg="#2d2c3a")
        
        # Label and entry for withdrawal amount
        wdraw_label = tk.Label(withdraw_window, text="Enter amount to withdraw:", bg="#2d2c3a", fg="white")
        wdraw_label.pack()
        
        wdraw_entry = tk.Entry(withdraw_window)
        wdraw_entry.pack()
        
        # Button to confirm withdrawal
        withdraw_button = tk.Button(withdraw_window, text="Withdraw", command=lambda: self.withdraw_money(withdraw_window, wdraw_entry.get()), bg="#01f4f8", fg="#2d2c3a")
        withdraw_button.pack()

    def withdraw_money(self, withdraw_window, amount):
        try:
            amount = int(amount)
            if amount <= 0:
                messagebox.showerror(title="Error", message="Please enter a valid amount")
                return

            with open(self.accounts_file, "r") as file:
                lines = file.readlines()

            with open(self.accounts_file, "w") as file:
                for line in lines:
                    data = ast.literal_eval(line)
                    if data["email"] == self.current_account:
                        if data["balance"] >= amount:
                            data["balance"] -= amount
                            messagebox.showinfo(title="Withdraw Successful", message=f"Withdrawn {amount} from {self.current_account} account")
                        else:
                            messagebox.showerror(title="Error", message="Insufficient balance")
                    file.write(str(data) + "\n")

            withdraw_window.destroy()

        except ValueError:
            messagebox.showerror(title="Error", message="Please enter a valid amount")

    def deposit(self):
        # Open a new window for deposit
        deposit_window = tk.Toplevel(self)
        deposit_window.title("Deposit Money")
        deposit_window.geometry("300x200")
        deposit_window.configure(bg="#2d2c3a")
        
        # Label and entry for deposit amount
        ddraw_label = tk.Label(deposit_window, text="Enter amount to deposit:", bg="#2d2c3a", fg="white")
        ddraw_label.pack()
        
        ddraw_entry = tk.Entry(deposit_window)
        ddraw_entry.pack()
        
        # Button to confirm deposit
        deposit_button = tk.Button(deposit_window, text="Deposit", command=lambda: self.deposit_money(deposit_window, ddraw_entry.get()), bg="#01f4f8", fg="#2d2c3a")
        deposit_button.pack()

    def deposit_money(self, deposit_window, amount):
        try:
            amount = int(amount)
            if amount <= 0:
                messagebox.showerror(title="Error", message="Please enter a valid amount")
                return

            with open(self.accounts_file, "r") as file:
                lines = file.readlines()

            with open(self.accounts_file, "w") as file:
                for line in lines:
                    data = ast.literal_eval(line)
                    if data["email"] == self.current_account:
                        data["balance"] += amount
                        messagebox.showinfo(title="Deposit Successful", message=f"Deposited {amount} to {self.current_account} account")
                    file.write(str(data) + "\n")

            deposit_window.destroy()

        except ValueError:
            messagebox.showerror(title="Error", message="Please enter a valid amount")

    def delete_account(self):
        # Open a new window for account deletion
        delete_window = tk.Toplevel(self)
        delete_window.title("Delete Account")
        delete_window.geometry("300x200")
        delete_window.configure(bg="#2d2c3a")
        
        # Label and entry for password
        delpass_label = tk.Label(delete_window, text="Enter password to delete account:", bg="#2d2c3a", fg="white")
        delpass_label.pack()
        
        delpass_entry = tk.Entry(delete_window, show="*")
        delpass_entry.pack()
        
        # Button to confirm account deletion
        delete_button = tk.Button(delete_window, text="Delete Account", command=lambda: self.delete(delete_window, delpass_entry.get()), bg="#01f4f8", fg="#2d2c3a")
        delete_button.pack()

    def delete(self, delete_window, password):
        try:
            with open(self.accounts_file, "r") as file:
                lines = file.readlines()

            with open(self.accounts_file, "w") as file:
                for line in lines:
                    data = ast.literal_eval(line)
                    if data["email"] == self.current_account and data["password"] == password:
                        messagebox.showinfo(title="Account Deleted", message=f"Account {self.current_account} deleted successfully")
                    else:
                        file.write(line)

            delete_window.destroy()
            self.current_account = ""
            self.login_screen()

        except FileNotFoundError:
            messagebox.showerror(title="Error", message="Account file not found")

if __name__ == "__main__":
    app = BankingApp()
    app.mainloop()
