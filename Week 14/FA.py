class VehicleEfficiency:
    def __init__(self, vehicle_id, fuel_capacity, fuel_consumed):
        self.vehicle_id = vehicle_id
        self.fuel_capacity = fuel_capacity
        self.fuel_consumed =fuel_consumed

    def show_info(self):
        print(f"Vehicle ID    : {self.vehicle_id}")
        print(f"Fuel Capacity : {self.fuel_capacity}")
        print(f"Fuel Consumed : {self.fuel_consumed}")

    def check_efficiency(self):
        total_fuel_used = sum(self.fuel_consumed)
        remaining_fuel = self.fuel_capacity - total_fuel_used

        if remaining_fuel > 20:
            status = "High Efficiency"
        elif remaining_fuel > 10:
            status = "Moderate Efficiency"
        else:
            status = "Low Efficiency"

        print(f"Total Fuel Used : {total_fuel_used}L")
        print(f"remaining Fuel  : {remaining_fuel}L")
        print(f"Status          : {status}")

    def get_peak_trip(self):
        print(f"Fuel consumed: {max(self.fuel_consumed)}L")

vehicle_id = input("Enter vehicle id: ")

while True:
    try:
        fuel_capity = float(input("Enter fuel capacity: "))
        if fuel_capity > 0:
            break
        print("Capacity must be greater than 0")
    except ValueError:
        print("Invalid input! Please enter number.")

fuel_consumed = []

i = 1
while i <= 2:
    try:
        fuel = float(input(f"Enter fuel consumed for trip {i}(L)"))
        if fuel >= 0:
            fuel_consumed.append(fuel)
            i+=1
        else:
            print("Value cannot be negative")
    except ValueError:
        print("Invalid input! Please enter number.")

v1 = VehicleEfficiency(vehicle_id, fuel_capity, fuel_consumed)
v1.show_info()
v1.check_efficiency()
v1.get_peak_trip()