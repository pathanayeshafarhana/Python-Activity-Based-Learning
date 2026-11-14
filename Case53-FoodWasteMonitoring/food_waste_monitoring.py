
print("===================================")
print("     FOOD WASTE MONITORING SYSTEM")
print("===================================")

acceptable_limit = 10

days = int(input("Enter number of days: "))

if days <= 0:
    print("Invalid number of days!")

else:
    for day in range(1, days + 1):

        print("\nDay", day)

        prepared = int(input("Enter meals prepared: "))
        served = int(input("Enter meals served: "))

        if prepared <= 0 or served < 0 or served > prepared:
            print("Invalid meal quantities!")
            print("Please enter valid values.")
            continue

        leftover = prepared - served

        wastage = (leftover / prepared) * 100

        print("\n----- DAILY REPORT -----")
        print("Meals Prepared:", prepared)
        print("Meals Served:", served)
        print("Leftover Meals:", leftover)
        print("Wastage Percentage:", round(wastage, 2), "%")

        if wastage > acceptable_limit:
            print("Status: Exceeded Limit")
        else:
            print("Status: Within Limit")

    print("\nFood Waste Monitoring Completed")
