# Case Study 53: Food Waste Monitoring System

## 1. Aim
To develop a Python program to monitor food waste by comparing prepared meals, meals served, and leftover meals across several days. Calculate wastage percentages and identify days exceeding the acceptable wastage limit.

## 2. Problem Statement
Food waste is a major problem in canteens and food-serving institutions. This program monitors the number of meals prepared, meals served, and meals left over each day. It calculates the wastage percentage and identifies days when food wastage exceeds the acceptable limit.

## 3. Objectives
1. To record the number of meals prepared each day.
2. To record the number of meals served.
3. To calculate leftover meals.
4. To calculate food wastage percentage.
5. To identify days exceeding the acceptable wastage limit.

## 4. Assumptions
1. All meal quantities are non-negative integers.
2. Meals served cannot exceed meals prepared.
3. Leftover meals are calculated by subtracting meals served from meals prepared.
4. The acceptable wastage limit is assumed to be 10%.
5. Data is collected for multiple days.

## 5. INPUT
- Number of days.
- Meals prepared each day.
- Meals served each day.
- Acceptable wastage percentage (10%).

## 6. PROCESS
1. Read the number of days.
2. Read prepared meals and served meals for each day.
3. Calculate leftover meals.
4. Calculate wastage percentage.
5. Compare the wastage percentage with the acceptable limit.
6. Display the results for each day.

Formula:

Leftover Meals = Prepared Meals - Served Meals

Wastage Percentage = (Leftover Meals / Prepared Meals) × 100

## 7. OUTPUT
- Meals prepared.
- Meals served.
- Leftover meals.
- Wastage percentage.
- Wastage status (Within Limit or Exceeded Limit).

## 8. Algorithm
1. Start.
2. Read the number of days.
3. Set the acceptable wastage limit to 10%.
4. Repeat for each day:
   - Read prepared meals.
   - Read served meals.
   - Calculate leftover meals.
   - Calculate wastage percentage.
   - Check whether wastage exceeds 10%.
   - Display the results.
5. Stop.

## 9. Pseudocode

START

INPUT number_of_days

SET acceptable_limit = 10

FOR each day FROM 1 TO number_of_days

    INPUT prepared_meals
    INPUT served_meals

    leftover = prepared_meals - served_meals

    IF prepared_meals > 0 THEN
        wastage = (leftover / prepared_meals) * 100
    ELSE
        wastage = 0
    END IF

    IF wastage > acceptable_limit THEN
        DISPLAY "Exceeded Limit"
    ELSE
        DISPLAY "Within Limit"
    END IF

    DISPLAY prepared_meals
    DISPLAY served_meals
    DISPLAY leftover
    DISPLAY wastage

END FOR

STOP

## 10. Flowchart

START
  |
  v
INPUT Number of Days
  |
  v
INPUT Prepared and Served Meals
  |
  v
Calculate Leftover Meals
  |
  v
Calculate Wastage Percentage
  |
  v
Is Wastage > 10%?
  |
  |---- YES ----> Display Exceeded Limit
  |
  |---- NO -----> Display Within Limit
  |
  v
Display Results
  |
  v
More Days?
  |
  |---- YES ----> Repeat
  |
  |---- NO -----> STOP

## 11. Test Cases

### Test Case 1
Input:
Prepared Meals = 100
Served Meals = 90

Expected Output:
Leftover Meals = 10
Wastage Percentage = 10%
Status = Within Limit

### Test Case 2
Input:
Prepared Meals = 100
Served Meals = 80

Expected Output:
Leftover Meals = 20
Wastage Percentage = 20%
Status = Exceeded Limit

### Test Case 3
Input:
Prepared Meals = 200
Served Meals = 190

Expected Output:
Leftover Meals = 10
Wastage Percentage = 5%
Status = Within Limit

### Test Case 4
Input:
Prepared Meals = 50
Served Meals = 30

Expected Output:
Leftover Meals = 20
Wastage Percentage = 40%
Status = Exceeded Limit

### Test Case 5
Input:
Prepared Meals = 150
Served Meals = 150

Expected Output:
Leftover Meals = 0
Wastage Percentage = 0%
Status = Within Limit

## 12. Conclusion

The Food Waste Monitoring System successfully calculates leftover meals and wastage percentages. It identifies days with excessive food wastage and helps institutions monitor and reduce food waste.
