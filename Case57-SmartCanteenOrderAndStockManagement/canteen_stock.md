
# Case Study 57: Smart Canteen Order and Stock Management

## Aim
To develop a Python program to process canteen orders, calculate bills and manage stock.

## Problem Statement
Develop a canteen system that accepts successive customer orders, checks stock, calculates bills and summarizes daily sales.

## INPUT
- Food item selection
- Order quantity
- Available stock
- Item price

## PROCESS
1. Display the menu.
2. Accept customer orders.
3. Check stock availability.
4. Calculate the bill.
5. Update inventory.
6. Repeat for successive orders.
7. Display daily sales and remaining stock.

## OUTPUT
- Order details
- Individual bills
- Daily sales
- Remaining stock

## Assumptions
- Order quantity must be positive.
- Orders cannot exceed available stock.
- Prices are fixed.
- The menu contains three items.

## Algorithm
1. Start.
2. Initialize food items, prices and stock.
3. Display the menu.
4. Input item selection and quantity.
5. Validate the order.
6. Check stock availability.
7. Calculate bill and update stock.
8. Repeat until exit.
9. Display daily sales and remaining stock.
10. Stop.

## Pseudocode

START
INITIALIZE items, prices, stock
SET total_sales = 0

REPEAT
    DISPLAY menu
    INPUT choice

    IF choice is valid
        INPUT quantity
        IF stock is sufficient
            CALCULATE bill
            UPDATE stock
            UPDATE total_sales
        ELSE
            DISPLAY insufficient stock
        END IF
    END IF
UNTIL exit selected

DISPLAY total_sales
DISPLAY remaining stock
STOP

## Flowchart

START
 |
INITIALIZE MENU AND STOCK
 |
DISPLAY MENU
 |
INPUT ORDER
 |
CHECK STOCK
 |
CALCULATE BILL AND UPDATE STOCK
 |
MORE ORDERS?
 | YES → REPEAT
 | NO
 |
DISPLAY DAILY SALES
 |
STOP

## Test Cases
1. Stock = 20, Order = 5, Price = 30
   Expected: Bill = Rs. 150.

2. Stock = 15, Order = 10, Price = 50
   Expected: Bill = Rs. 500.

3. Stock = 5, Order = 8
   Expected: Insufficient stock.

4. Order quantity = 0
   Expected: Invalid quantity.

5. Stock = 10, Order = 3, Price = 20
   Expected: Bill = Rs. 60; remaining stock = 7.

## Conclusion
The program processes multiple canteen orders, calculates sales and maintains updated inventory.
