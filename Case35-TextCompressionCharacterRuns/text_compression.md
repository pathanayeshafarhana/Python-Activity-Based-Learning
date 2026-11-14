
# Case Study 35: Text Compression Using Character Runs

## Aim
To develop a Python program to compress text by grouping consecutive repeated characters.

## Problem Statement
Create a program that identifies consecutive repeated characters, counts their occurrences and generates compressed text.

## INPUT
- Original text

## PROCESS
1. Read the text.
2. Identify consecutive repeated characters.
3. Count each character's occurrences.
4. Generate compressed text.
5. Compare original and compressed lengths.
6. Display the shorter representation.

## OUTPUT
- Original text
- Compressed text
- Original length
- Compressed length
- Selected representation

## Assumptions
- Text is case-sensitive.
- Compression groups consecutive identical characters.
- Each group is represented as character:count.

## Algorithm
1. Start.
2. Input text.
3. Check whether text is empty.
4. Count consecutive repeated characters.
5. Create compressed representation.
6. Compare both lengths.
7. Display the shorter representation.
8. Stop.

## Pseudocode

START
INPUT text
SET compressed = empty string
SET count = 1

FOR each character from second position
    IF character = previous character
        count = count + 1
    ELSE
        ADD previous character and count
        RESET count = 1
    END IF
END FOR

ADD last character and count

COMPARE LENGTHS
DISPLAY RESULT
STOP

## Flowchart

START
 |
INPUT TEXT
 |
COUNT REPEATED CHARACTERS
 |
GENERATE COMPRESSED TEXT
 |
COMPARE LENGTHS
 |
DISPLAY RESULT
 |
STOP

## Test Cases
1. Input: aaabbc
   Expected: a:3;b:2;c:1

2. Input: aaaa
   Expected: a:4

3. Input: abc
   Expected: Original text is shorter.

4. Input: xxxyyy
   Expected: x:3;y:3

5. Input: empty text
   Expected: Empty input message.

## Conclusion
The program compresses consecutive repeated characters and compares the compressed and original text lengths.
