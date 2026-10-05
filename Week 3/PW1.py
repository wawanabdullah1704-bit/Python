categoryCode = ("CAT01", "CAT02", "CAT03")

staffID = {"STF101", "STF102", "STF103"}

itemPrice = {
    "fanta": 300,
    "sprite": 50,
    "cola": 30,
    "ribena": 100,
}

totalItems = 0
totalRevenue = 0.0

IdInput = input("Enter Staff ID (STF101, STF102, STF103): ")

if IdInput in staffID:
    print("Access Granted")

    while True:
        categoryInput = input("Enter Category Code (CAT01, CAT02, CAT03): ")

        if categoryInput in categoryCode:
            item = input("Enter Item Name (fanta, sprite, cola, rebina): ")

            if item in itemPrice:
                quantity = int(input("Enter Quantity: "))
                amount = itemPrice[item] * quantity

                if amount > 200:
                    discount = amount * 0.05
                    finalAmount = amount - discount
                    print("5% Discount Applied: RM", discount)
                else:
                    finalAmount = amount

                print("Transaction Total: RM", finalAmount)
                totalItems += quantity
                totalRevenue += finalAmount
            else:
                print("Invalid Item Name")
        else:
            print("Invalid Category Code")

        choice = input("Record another transaction? (Y/N): ").upper()
        if choice != "Y":
            break

    print("\n--- Summary ---")
    print("Total Items Sold:", totalItems)
    print("Total Revenue: RM", totalRevenue)
else:
    print("Access Denied")