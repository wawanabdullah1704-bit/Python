def  calculate_trip_cost(distance_km):
    liters = distance_km/15
    cost = liters * 2.05
    return liters, cost

distance_km = float(input("Enter travel distance (in km): "))

liters, cost = calculate_trip_cost(distance_km)

print(f"Total fuel used (in liters): {liters:.2f}")
print(f"Total cost (in RM): {cost:.2f}")