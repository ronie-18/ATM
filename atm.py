class ATM:

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input(
            """
            Hello how would you like to proceed?
            1. Press 1 to create pin
            2. Press 2 to deposit
            3. Press 3 to withdraw
            4. Press 4 to check balance
            5. Press 5 to exit
        """
        )
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            print("Thank you for using our ATM")
            exit()
        else:
            print("Invalid input")
            self.menu()

    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Pin set successfully")
        self.menu()

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            self.balance = self.balance + amount
            print("Deposit successful")
            print(f"Your current balance is: ₹{self.balance}")
        else:
            print("Invalid pin")
        self.menu()

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("Withdrawal successful")
                print(f"Your current balance is: ₹{self.balance}")
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin")
        self.menu()

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print(f"Your balance is: ₹{self.balance}")
        else:
            print("Invalid pin")
        self.menu()
