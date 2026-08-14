# Banking-App-Intermediate-Micro-Project
A purely academic exercise for a simple user-facing banking app with extremely limited functionality. Goal to logical reasoning with use of nested dictionaries, for/while loops, and if/elif/else statements.

# CLI Banking Application

A command-line banking application written in Python to practice account management, input validation, nested data structures, state mutation, and transaction processing.

This project was built independently from a set of functional requirements as an intermediate-level Python micro-project. It uses no third-party libraries and relies entirely on core Python functionality and the standard library.

## Features

- User account lookup and validation
- Account balance viewing
- Deposits
- Withdrawals
- Account-to-account transfers
- Transaction history
- Public-facing bank information
- Numeric input validation
- Insufficient-funds protection
- Zero-value transaction prevention
- Self-transfer prevention
- Dynamic account and transfer-recipient lookup
- Persistent account state throughout program execution
- Menu-driven command-line interface

## Account Structure

Account information is stored in a nested dictionary.

Each account ID acts as a key to another dictionary containing the customer's name, current balance, and transaction history.

```python
accounts = {
    "1001": {
        "name": "alice",
        "balance": 1250.00,
        "transactions": []
    }
}
```

This structure allows account information to be accessed dynamically using an account ID while maintaining related customer information within a single data structure.

## How It Works

The application follows a menu-driven execution loop:

```text
Start Application
       |
       v
Initialize Accounts
       |
       v
Display Menu
       |
       v
Validate Customer
       |
       v
Determine Account ID
       |
       v
Validate Menu Selection
       |
       +----------------------+
       |          |           |
       v          v           v
   Balance     Deposit    Withdrawal
       |          |           |
       +----------+-----------+
                  |
             +----+----+
             |         |
             v         v
          Transfer  History
             |         |
             +----+----+
                  |
                  v
             Return to Menu
```

Account data remains in memory while the application runs, allowing deposits, withdrawals, transfers, and transaction records to persist between menu operations.

## Transactions

### Deposits

The application prompts the customer for a deposit amount and validates that the input can be converted to a numeric value.

Successful deposits:

- Increase the customer's balance
- Reject zero-value inputs
- Record the transaction in the customer's transaction history

### Withdrawals

Withdrawals are validated before being finalized.

The application:

- Validates numeric input
- Rejects zero-value inputs
- Prevents the account balance from remaining below zero
- Restores the original balance when funds are insufficient
- Records only successful withdrawals

### Transfers

Transfers modify two accounts as part of a single operation.

For a successful transfer, the application:

1. Identifies the source account.
2. Accepts and validates the transfer amount.
3. Searches the account database for the recipient.
4. Prevents transfers to the same account.
5. Verifies that sufficient funds are available.
6. Subtracts funds from the source account.
7. Adds funds to the destination account.
8. Records the transaction in both customers' transaction histories.

Recipient accounts are located dynamically from the account data rather than through a hard-coded name-to-account mapping.

## Transaction History

Each account maintains its own transaction list.

Example:

```text
[
    "Deposited 500.0",
    "Withdrew 125.0",
    "250.0 sent to bob"
]
```

Transfers generate records for both the sending and receiving accounts.

## Bank Information

The application provides generic, sanitized public-facing information about the bank.

Bank-wide financial statistics are intentionally not exposed through the customer interface because the application does not implement a separate administrative authentication or authorization system.

## Requirements

### Python

- Python 3

### Standard Library

- `sys`

`sys` is included with Python and does **not** require installation through `pip`.

The application has **no third-party dependencies**.

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

No package installation is required.

## Usage

Run the application with:

```bash
python banking_app.py
```

The program displays the available customer operations:

```text
Choose a menu option:

(1) View Account Balance
(2) Deposit Funds
(3) Withdraw Funds
(4) Transfer Funds
(5) View Transaction History
(6) View Bank Statistics
(7) Exit
```

Enter a valid username and select the desired operation.

The application continues running until the user selects the exit option.

## Concepts Practiced

This project provided practical experience with:

- Nested dictionaries
- Lists
- Mutable data structures
- Dictionary traversal
- Dynamic key lookup
- Functions and parameters
- Function decomposition
- Loops
- Conditional logic
- Exception handling
- User-input validation
- Type conversion
- State management
- Data integrity
- Transaction processing
- String formatting
- Menu-driven application design
- Defensive programming
- Program control flow

## Design Considerations

### Mutable State

The account dictionary is initialized once during program execution and passed to functions responsible for banking operations.

Because dictionaries and their nested lists are mutable, these functions can update account balances and transaction histories while preserving those changes when control returns to the main application loop.

### Data-Driven Account Lookup

Account IDs are determined by searching the account dictionary rather than maintaining separate hard-coded mappings between usernames and account numbers.

The same approach is used when locating transfer recipients.

This allows additional accounts to be added to the underlying data structure without requiring a separate conditional branch for every customer.

### Transaction Integrity

Operations that can fail are designed to avoid leaving account balances in an invalid state.

For example, an attempted withdrawal or transfer that would result in insufficient funds restores the source account's original balance rather than leaving the failed transaction applied.

## Limitations

This application is an educational command-line simulation rather than a production banking system.

It does not currently implement:

- Persistent database storage
- Password authentication
- Administrative roles
- Encryption
- Concurrent transactions
- Decimal-based financial arithmetic
- Network communication
- Audit logging
- Production-grade security controls

Account data exists only for the duration of the running program.

## Project Purpose

The primary objective of this project was to practice designing a complete intermediate Python program independently from functional requirements without relying on external modules or libraries.

Particular emphasis was placed on managing nested mutable data structures and maintaining consistent state across multiple operations.

The transfer functionality provides the central example: a single successful operation must coordinate changes to two account balances and two transaction histories while ensuring that failed operations do not leave the account data in an invalid state.

## Development

This project was developed iteratively.

The initial working version established the menu system and core banking operations. Subsequent revisions improved:

- Input validation
- Transaction logging
- Insufficient-funds handling
- Zero-value transaction handling
- Self-transfer prevention
- Dynamic account lookup
- Dynamic transfer-recipient lookup
- Separation of customer-facing and privileged bank information

## License

This project is intended for educational and portfolio use.

See the repository's `LICENSE` file for applicable licensing terms.
