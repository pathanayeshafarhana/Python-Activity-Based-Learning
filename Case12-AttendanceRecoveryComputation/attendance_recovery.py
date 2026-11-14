
print("================================")
print(" ATTENDANCE RECOVERY SYSTEM")
print("================================")

name = input("Enter student name: ")
total = int(input("Enter total classes conducted: "))
attended = int(input("Enter classes attended: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details!")

else:
    percentage = (attended / total) * 100

    print("\nStudent Name:", name)
    print("Attendance Percentage:", round(percentage, 2), "%")

    if percentage >= 75:
        print("Status: Sufficient Attendance")
        print("Additional Classes Required: 0")

    else:
        additional = 0

        while (attended + additional) / (total + additional) < 0.75:
            additional += 1

        print("Status: Shortage of Attendance")
        print("Additional Classes Required:", additional)
