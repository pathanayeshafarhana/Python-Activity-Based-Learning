
print("===== STUDENT MARKS ANALYSIS =====")

students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

if students <= 0 or subjects <= 0:
    print("Invalid number of students or subjects!")

else:
    marks = []

    for i in range(students):
        student_marks = []
        print("\nStudent", i + 1)

        for j in range(subjects):
            mark = float(input("Enter marks for subject " + str(j + 1) + ": "))

            if mark < 0 or mark > 100:
                print("Invalid marks!")
                mark = 0

            student_marks.append(mark)

        marks.append(student_marks)

    print("\n===== RESULTS =====")

    for i in range(students):
        total = sum(marks[i])
        average = total / subjects

        print("\nStudent", i + 1)
        print("Marks:", marks[i])
        print("Total:", total)
        print("Average:", round(average, 2))
