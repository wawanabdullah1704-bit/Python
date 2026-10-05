class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity


def main():
    product_list = []

    total_products = int(
        input("How many products would you like to enter? ")
    )

    counter = 0

    while counter < total_products:
        product_name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        product = Product(product_name, price, quantity)

        product_list.append(product)

        counter += 1

    print("\nProduct List")

    index = 0
    grand_total = 0

    while index < len(product_list):
        product = product_list[index]

        total_price = product.calculate_total()

        print(f"Product Number: {index + 1}")
        print(f"Product Name: {product.product_name}")
        print(f"Price: {product.price}")
        print(f"Quantity: {product.quantity}")
        print(f"Total Price: {total_price}")

        grand_total += total_price

        index += 1

    print(f"Grand Total: {grand_total}")


if __name__ == "__main__":
    main()