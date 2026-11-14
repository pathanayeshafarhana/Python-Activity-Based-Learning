
# Case Study 18: Fuel Consumption and Route Comparison

## Aim
To calculate fuel requirements and journey costs for different vehicles and identify the lowest-cost option.

## Problem Statement
Compare different vehicles based on distance, mileage, fuel price and reserve requirements to find the lowest-cost feasible vehicle.

## INPUT
- Journey distance
- Number of vehicles
- Vehicle names
- Mileage of each vehicle
- Fuel price
- Reserve percentage

## PROCESS
1. Read journey details.
2. Read vehicle details.
3. Calculate fuel required for each vehicle.
4. Add reserve fuel.
5. Calculate journey cost.
6. Identify the lowest-cost vehicle.

## OUTPUT
- Vehicle name
- Fuel required
- Journey cost
- Lowest-cost vehicle

## Assumptions
- Distance and mileage must be positive.
- Fuel price cannot be negative.
- Reserve percentage is 10%.

## Algorithm
1. Start.
2. Input journey distance and fuel price.
3. Input vehicle details.
4. Calculate fuel required.
5. Add reserve fuel.
6. Calculate journey cost.
7. Compare vehicle costs.
8. Display the lowest-cost vehicle.
9. Stop.

## Pseudocode

START
INPUT distance
INPUT fuel_price
INPUT number_of_vehicles

FOR each vehicle
    INPUT name, mileage
    fuel = distance / mileage
    total_fuel = fuel + fuel * 10 / 100
    cost = total_fuel * fuel_price
    STORE vehicle details
END FOR

FIND minimum cost
DISPLAY results
STOP

## Flowchart

START
 |
INPUT JOURNEY DETAILS
 |
INPUT VEHICLE DETAILS
 |
CALCULATE FUEL AND COST
 |
COMPARE VEHICLE COSTS
 |
DISPLAY LOWEST-COST VEHICLE
 |
STOP

## Test Cases
1. Distance = 100, Mileage = 20, Fuel price = 100
   Expected: Fuel with reserve = 5.5 litres; Cost = Rs. 550.

2. Distance = 200, Mileage = 10, Fuel price = 100
   Expected: Fuel with reserve = 22 litres; Cost = Rs. 2200.

3. Distance = 100, Mileage = 25, Fuel price = 100
   Expected: Fuel with reserve = 4.4 litres; Cost = Rs. 440.

4. Distance = 150, Mileage = 15, Fuel price = 100
   Expected: Fuel with reserve = 11 litres; Cost = Rs. 1100.

5. Distance = 0
   Expected: Invalid distance.

## Conclusion
The program compares vehicle fuel requirements and journey costs to identify the most economical option.
