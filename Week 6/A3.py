def calculate_total(price, quantity):
    return price * quantity

def main():
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    total = calculate_total(price, quantity)

    print(f"Total Price: {total}")

if __name__ == "__main__":
    main()