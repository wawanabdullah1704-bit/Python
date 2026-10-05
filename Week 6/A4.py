class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def display_information(self):
        print("Product Name:", self.product_name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total Price:", self.calculate_total())


def main():
    product_name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    product = Product(product_name, price, quantity)

    product.display_information()


if __name__ == "__main__":
    main()