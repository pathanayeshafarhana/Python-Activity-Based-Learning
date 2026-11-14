
# Case Study 42: Student Marks Matrix Analysis

## Aim
To develop a Python program to store and analyse student marks using a nested list.

## Problem Statement
Create a program to store marks of multiple students in different subjects and calculate each student's total and average marks.

## INPUT
- Number of students
- Number of subjects
- Marks of each student

## PROCESS
1. Read the number of students and subjects.
2. Store marks in a nested list.
3. Calculate the total marks of each student.
4. Calculate the average marks.
5. Display the results.

## OUTPUT
- Student-wise marks
- Total marks
- Average marks

## Assumptions
- At least one student and one subject must be entered.
- Marks must be between 0 and 100.

## Algorithm
1. Start.
2. Input number of students and subjects.
3. Create an empty nested list.
4. Input and store marks for every student.
5. Calculate each student's total.
6. Calculate each student's average.
7. Display the results.
8. Stop.

## Pseudocode

START
INPUT students, subjects
CREATE empty marks list

FOR each student
    CREATE empty student list
    FOR each subject
        INPUT mark
        ADD mark to student list
    END FOR
    ADD student list to marks
END FOR

FOR each student in marks
    total = SUM(student)
    average = total / subjects
    DISPLAY total, average
END FOR

STOP

## Flowchart

START
  |
INPUT STUDENTS AND SUBJECTS
  |
INPUT MARKS INTO NESTED LIST
  |
CALCULATE TOTAL AND AVERAGE
  |
DISPLAY RESULTS
  |
STOP

## Test Cases

1. Input: 1 student, marks = 80, 90
   Expected: Total = 170, Average = 85.

2. Input: 1 student, marks = 50, 60
   Expected: Total = 110, Average = 55.

3. Input: 1 student, marks = 100, 100
   Expected: Total = 200, Average = 100.

4. Input: 1 student, marks = 0, 40
   Expected: Total = 40, Average = 20.

5. Input: 1 student, marks = 70, 80, 90
   Expected: Total = 240, Average = 80.

## Conclusion
The program uses nested lists to store and analyse student marks and calculate totals and averages.
