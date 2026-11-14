# Case Study 53: Food Waste Monitoring System

## Aim
To develop a Python program to monitor food waste and calculate wastage percentages across several days.

## INPUT
- Number of days
- Meals prepared each day
- Meals served each day
- Acceptable wastage limit (10%)

## PROCESS
1. Read the number of days.
2. Read prepared and served meals.
3. Calculate leftover meals.
4. Calculate wastage percentage.
5. Compare wastage with the 10% limit.
6. Display the daily report.

## OUTPUT
- Meals prepared
- Meals served
- Leftover meals
- Wastage percentage
- Wastage status

## Algorithm
1. Start.
2. Input the number of days.
3. Set acceptable limit to 10%.
4. Repeat for each day.
5. Input prepared and served meals.
6. Validate the quantities.
7. Calculate leftover meals.
8. Calculate wastage percentage.
9. Check whether wastage exceeds 10%.
10. Display the results.
11. Stop.

## Pseudocode

START
INPUT days
SET limit = 10

IF days <= 0
    DISPLAY "Invalid number of days"
ELSE
    FOR each day
        INPUT prepared, served

        IF prepared <= 0 OR served < 0 OR served > prepared
            DISPLAY "Invalid quantities"
        ELSE
            leftover = prepared - served
            wastage = (leftover / prepared) * 100

            IF wastage > limit
                DISPLAY "Exceeded Limit"
            ELSE
                DISPLAY "Within Limit"
            END IF
        END IF
    END FOR
END IF

STOP

## Flowchart

START
  |
INPUT Number of Days
  |
Is Days > 0?
  |
  YES
  |
INPUT Prepared and Served Meals
  |
Validate Quantities
  |
Calculate Leftover Meals
  |
Calculate Wastage Percentage
  |
Is Wastage > 10%?
  |
Display Status
  |
More Days?
  |
Repeat or STOP

## Test Cases

### Test Case 1
Input: Prepared = 100, Served = 90
Expected Output: Leftover = 10, Wastage = 10%
Status: Within Limit

### Test Case 2
Input: Prepared = 100, Served = 80
Expected Output: Leftover = 20, Wastage = 20%
Status: Exceeded Limit

### Test Case 3
Input: Prepared = 200, Served = 190
Expected Output: Leftover = 10, Wastage = 5%
Status: Within Limit

### Test Case 4
Input: Prepared = 50, Served = 30
Expected Output: Leftover = 20, Wastage = 40%
Status: Exceeded Limit

### Test Case 5
Input: Prepared = 150, Served = 150
Expected Output: Leftover = 0, Wastage = 0%
Status: Within Limit

## Conclusion
The Food Waste Monitoring System calculates leftover meals and wastage percentages and identifies days with excessive food wastage.
