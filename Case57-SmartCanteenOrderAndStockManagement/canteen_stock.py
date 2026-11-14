
print("===== SMART CANTEEN MANAGEMENT =====")

items = ["Sandwich", "Burger", "Juice"]
prices = [30, 50, 20]
stock = [20, 15, 25]

total_sales = 0

while True:
    print("\n===== MENU =====")

    for i in range(len(items)):
        print(i + 1, items[i],
              "Rs.", prices[i],
              "Stock:", stock[i])

    print("0. Exit")

    choice = int(input("Enter item number: "))

    if choice == 0:
        break

    if choice < 1 or choice > len(items):
        print("Invalid selection!")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Invalid quantity!")

    else:
        index = choice - 1

        if quantity <= stock[index]:
            bill = quantity * prices[index]
            stock[index] -= quantity
            total_sales += bill

            print("Item:", items[index])
            print("Bill: Rs.", bill)
            print("Remaining Stock:", stock[index])

        else:
            print("Insufficient stock!")

print("\n===== DAILY SUMMARY =====")
print("Total Sales: Rs.", total_sales)

for i in range(len(items)):
    print(items[i], "Remaining:", stock[i])

print("Thank you!")
