
print("===== COURSE REGISTRATION VALIDATION =====")

n = int(input("Enter number of registrations: "))

if n <= 0:
    print("Invalid number of registrations!")

else:
    registrations = []

    for i in range(n):
        print("\nRegistration", i + 1)

        student = input("Enter student name: ")
        course = input("Enter course code: ").upper()

        record = (student, course)
        registrations.append(record)

    print("\n===== REGISTRATION RECORDS =====")

    for record in registrations:
        print(record)

    print("\n===== VALIDATION REPORT =====")

    for i in range(len(registrations)):
        for j in range(i + 1, len(registrations)):

            if registrations[i] == registrations[j]:
                print("Duplicate registration:", registrations[i])

    students = []

    for record in registrations:
        if record[0] not in students:
            students.append(record[0])

    for student in students:
        courses = []

        for record in registrations:
            if record[0] == student:
                courses.append(record[1])

        if "PY101" in courses and "PY102" in courses:
            print(student, "has an invalid course combination.")

    print("\nValidation Completed.")
