print("Hotel Booking Cost")

ratePerNight = float(input("Room Rate Per Night: "))
numOfNight = int(input("Number Of Nights: "))

roomCost = ratePerNight * numOfNight
print(f"Room Cost: {roomCost}")

roomCostST = roomCost + (roomCost * 0.06)
print(f"Final Payment: {roomCostST}")