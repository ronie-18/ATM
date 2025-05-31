# ATM

# ATM Program

A simple command-line ATM (Automated Teller Machine) simulation program written in Python. This program provides basic banking operations through an interactive menu system.

## Features

- PIN Creation: Set up a secure PIN for account access
- Deposit: Add money to your account
- Withdraw: Take out money from your account
- Balance Check: View your current account balance
- Secure Operations: All transactions require PIN verification

## Requirements

- Python 3.x

## How to Run

1. Make sure you have Python installed on your system
2. Download the `atm.py` file
3. Open your terminal/command prompt
4. Navigate to the project directory
5. Run the program using:
   ```
   python atm.py
   ```

## Usage

When you run the program, you'll be presented with a menu with the following options:

1. Create PIN (Must be done first)
2. Deposit money
3. Withdraw money
4. Check balance
5. Exit

### Important Notes

- You must create a PIN before performing any other operations
- All transactions (deposit, withdrawal, balance check) require PIN verification
- The program uses the Indian Rupee (₹) symbol for currency display
- Invalid PIN entries will return you to the main menu
- Withdrawal amount cannot exceed your current balance

## Example Usage

1. First, select option 1 to create your PIN
2. Use option 2 to make your first deposit
3. Use option 3 to make withdrawals
4. Use option 4 to check your balance at any time
5. Use option 5 to safely exit the program

## Security Features

- PIN verification required for all transactions
- Balance amount is protected and only accessible with correct PIN
- Program exits securely when requested

## Contributing

Feel free to fork this project and make improvements or add new features.

## License

This project is open source and available for educational and personal use. 
