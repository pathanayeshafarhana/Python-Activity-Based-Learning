
# Case Study 12: Attendance Recovery Computation

## Aim
To develop a Python program to calculate student attendance and determine the additional classes required to reach the minimum attendance percentage.

## Problem Statement
A college requires students to maintain at least 75% attendance. Develop a program to calculate current attendance and the additional consecutive classes needed to reach 75%.

## INPUT
- Student name
- Total classes conducted
- Classes attended

## PROCESS
1. Read student details.
2. Validate the number of classes.
3. Calculate attendance percentage.
4. Check whether attendance is at least 75%.
5. If attendance is below 75%, calculate additional classes needed.
6. Display the result.

## OUTPUT
- Student name
- Attendance percentage
- Attendance status
- Additional classes required

## Assumptions
- Minimum required attendance is 75%.
- Total classes must be greater than zero.
- Attended classes cannot exceed conducted classes.
- Additional classes are assumed to be attended without absence.

## Algorithm
1. Start.
2. Input student name.
3. Input total classes.
4. Input attended classes.
5. Validate the inputs.
6. Calculate attendance percentage.
7. If attendance is at least 75%, display eligible status.
8. Otherwise, calculate additional classes required.
9. Display the result.
10. Stop.

## Pseudocode

START
INPUT name
INPUT total_classes
INPUT attended_classes

IF total_classes <= 0 OR attended_classes < 0 OR attended_classes > total_classes
    DISPLAY "Invalid input"
ELSE
    percentage = attended_classes / total_classes * 100

    IF percentage >= 75
        DISPLAY "Attendance is sufficient"
    ELSE
        additional = 0
        WHILE (attended_classes + additional) /
              (total_classes + additional) < 0.75
            additional = additional + 1
        END WHILE
        DISPLAY additional
    END IF
END IF

STOP

## Flowchart

START
  |
INPUT STUDENT DETAILS
  |
VALIDATE INPUT
  |
CALCULATE ATTENDANCE %
  |
IS ATTENDANCE >= 75%?
  | YES                 | NO
DISPLAY SUFFICIENT      CALCULATE EXTRA CLASSES
  |                     |
  |                 DISPLAY RESULT
  |                     |
  ------ STOP ----------

## Test Cases

1. Input: Total = 100, Attended = 80
   Expected: 80%, sufficient attendance.

2. Input: Total = 100, Attended = 60
   Expected: 60%, 60 additional classes.

3. Input: Total = 50, Attended = 40
   Expected: 80%, sufficient attendance.

4. Input: Total = 40, Attended = 20
   Expected: 50%, 40 additional classes.

5. Input: Total = 0, Attended = 0
   Expected: Invalid input.

## Conclusion
The program calculates attendance percentage and determines how many additional consecutive classes are required to reach 75%.
