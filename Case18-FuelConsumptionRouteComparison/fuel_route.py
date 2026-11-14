
print("===== FUEL AND ROUTE COMPARISON =====")

distance = float(input("Enter journey distance: "))
fuel_price = float(input("Enter fuel price per litre: "))
n = int(input("Enter number of vehicles: "))

if distance <= 0 or fuel_price < 0 or n <= 0:
    print("Invalid input!")

else:
    vehicles = []

    for i in range(n):
        print("\nVehicle", i + 1)

        name = input("Enter vehicle name: ")
        mileage = float(input("Enter mileage: "))

        if mileage <= 0:
            print("Invalid mileage!")
            continue

        fuel = distance / mileage
        total_fuel = fuel + fuel * 10 / 100
        cost = total_fuel * fuel_price

        vehicles.append((name, total_fuel, cost))

    if len(vehicles) > 0:
        print("\n===== VEHICLE REPORT =====")

        for vehicle in vehicles:
            print("Vehicle:", vehicle[0])
            print("Fuel Required:", round(vehicle[1], 2))
            print("Journey Cost: Rs.", round(vehicle[2], 2))

        best = min(vehicles, key=lambda x: x[2])

        print("\nLowest Cost Vehicle:", best[0])
        print("Minimum Cost: Rs.", round(best[2], 2))
