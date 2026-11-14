
# Case Study 27: Advanced Numeric Pattern Generator

## Aim
To develop a Python program to generate numeric patterns using nested loops.

## Problem Statement
Create a program that accepts the number of rows and displays an increasing numeric pattern.

## INPUT
- Number of rows

## PROCESS
1. Read the number of rows.
2. Use an outer loop for rows.
3. Use an inner loop to print numbers.
4. Display the pattern.

## OUTPUT
A numeric pattern based on the entered number of rows.

## Assumptions
- Number of rows must be positive.
- Each row begins with number 1.
- Numbers increase from 1 in every row.

## Algorithm
1. Start.
2. Input number of rows.
3. Validate the number.
4. Repeat for each row.
5. Print numbers from 1 to the current row number.
6. Move to the next line.
7. Stop.

## Pseudocode

START
INPUT rows

IF rows <= 0
    DISPLAY "Invalid rows"
ELSE
    FOR i = 1 TO rows
        FOR j = 1 TO i
            DISPLAY j WITHOUT NEWLINE
        END FOR
        MOVE TO NEXT LINE
    END FOR
END IF

STOP

## Flowchart

START
  |
INPUT ROWS
  |
IS ROWS POSITIVE?
  |
  YES
  |
OUTER LOOP
  |
INNER LOOP
  |
PRINT NUMBERS
  |
NEXT ROW
  |
ALL ROWS COMPLETED?
  |
STOP

## Test Cases

1. Input: 1
   Expected Output:
   1

2. Input: 2
   Expected Output:
   1
   12

3. Input: 3
   Expected Output:
   1
   12
   123

4. Input: 4
   Expected Output:
   1
   12
   123
   1234

5. Input: 0
   Expected Output: Invalid rows.

## Conclusion
The program generates numeric patterns using nested loops.
