
# Case Study 64: Tuple-Based Course Registration Validation

## Aim
To develop a Python program to validate student course registrations using tuples.

## Problem Statement
Create a program to store course registrations as tuples, identify duplicate registrations and detect invalid course combinations.

## INPUT
- Number of registrations
- Student name
- Course code

## PROCESS
1. Read registration details.
2. Store details as tuples.
3. Check duplicate student-course registrations.
4. Check invalid course combinations.
5. Display registration results.

## OUTPUT
- Registration records
- Duplicate registrations
- Invalid course combinations
- Validation status

## Assumptions
- Course codes are entered in uppercase.
- A student cannot register for the same course twice.
- PY101 and PY102 cannot be selected together in the same term. This is a sample validation rule.

## Algorithm
1. Start.
2. Input number of registrations.
3. Create an empty registration list.
4. Input student and course details.
5. Store each registration as a tuple.
6. Check duplicate registrations.
7. Check invalid course combinations.
8. Display the results.
9. Stop.

## Pseudocode

START
INPUT number_of_registrations
CREATE empty registration list

FOR each registration
    INPUT student, course
    STORE (student, course)
END FOR

CHECK duplicate student-course pairs

FOR each student
    CHECK registered courses
    IF PY101 AND PY102 both exist
        DISPLAY invalid combination
    END IF
END FOR

DISPLAY results
STOP

## Flowchart

START
 |
INPUT REGISTRATION DETAILS
 |
STORE AS TUPLES
 |
CHECK DUPLICATES
 |
CHECK COURSE COMBINATIONS
 |
DISPLAY VALIDATION REPORT
 |
STOP

## Test Cases
1. Student A registers for PY101.
   Expected: Valid registration.

2. Student A registers for PY101 twice.
   Expected: Duplicate registration.

3. Student B registers for PY101 and PY102.
   Expected: Invalid course combination.

4. Student C registers for DB101 and PY101.
   Expected: Valid combination.

5. Student D registers for DB101 twice.
   Expected: Duplicate registration.

## Conclusion
The program uses tuples to store and validate course registration records.
