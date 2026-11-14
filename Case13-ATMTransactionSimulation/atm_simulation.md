
# Case Study 13: ATM Transaction Sequence Simulation

## Aim
To develop a Python program to simulate basic ATM transactions.

## Problem Statement
Develop a program that allows a user to check balance, deposit money, and withdraw money.

## INPUT
- Initial balance
- Transaction choice
- Transaction amount

## PROCESS
1. Display ATM menu.
2. Accept transaction choice.
3. Check balance, deposit, or withdraw money.
4. Validate the transaction.
5. Display updated balance.

## OUTPUT
- Transaction details
- Updated account balance
- Transaction status

## Assumptions
- Initial balance cannot be negative.
- Deposit amount must be positive.
- Withdrawal cannot exceed available balance.

## Algorithm
1. Start.
2. Input initial balance.
3. Display ATM menu.
4. Input transaction choice.
5. Perform the selected transaction.
6. Display updated balance.
7. Repeat until Exit is selected.
8. Stop.

## Pseudocode

START
INPUT balance

REPEAT
    DISPLAY ATM MENU
    INPUT choice

    IF choice = 1
        DISPLAY balance
    ELSE IF choice = 2
        INPUT deposit
        IF deposit > 0
            balance = balance + deposit
        END IF
    ELSE IF choice = 3
        INPUT withdrawal
        IF withdrawal > 0 AND withdrawal <= balance
            balance = balance - withdrawal
        END IF
    ELSE IF choice = 4
        DISPLAY "Thank you"
    ELSE
        DISPLAY "Invalid choice"
    END IF
UNTIL choice = 4

STOP

## Flowchart

START
  |
INPUT INITIAL BALANCE
  |
DISPLAY ATM MENU
  |
INPUT CHOICE
  |
PERFORM TRANSACTION
  |
UPDATE BALANCE
  |
EXIT SELECTED?
  | NO → REPEAT
  | YES
  |
STOP

## Test Cases

1. Balance = 1000, Choice = 1
   Expected: Balance = Rs. 1000

2. Balance = 1000, Deposit = 500
   Expected: Balance = Rs. 1500

3. Balance = 1000, Withdraw = 300
   Expected: Balance = Rs. 700

4. Balance = 1000, Withdraw = 1500
   Expected: Insufficient balance.

5. Balance = 1000, Choice = 4
   Expected: Exit message.

## Conclusion
The program simulates basic ATM transactions using conditional statements and loops.
