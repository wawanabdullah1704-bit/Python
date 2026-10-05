class Book:
    def __init__(self, book_title, price, quantity):
        self.book_title = book_title
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def calculate_discount(self):
        total = self.calculate_total()

        if total > 100:
            discount_amount = total * 0.10
            discounted_total = total - discount_amount
            return discounted_total
        else:
            return total

    def display_information(self):
        print(f"Book Title : {self.book_title}")
        print(f"Price      : RM{self.price:.2f}")
        print(f"Quantity   : {self.quantity}")
        print(f"Total Sales: RM{self.calculate_total():.2f}")

        if self.calculate_total() > 100:
            print(f"Discounted Total (10%): RM{self.calculate_discount():.2f}")


def display_header():
    print("=" * 50)
    print("BOOK SALES RECORD SYSTEM")
    print("=" * 50)


def main():
    display_header()

    book_list = []

    total_books = int(input("How many books would you like to enter? "))

    counter = 0

    while counter < total_books:
        print(f"\nEnter Book {counter + 1}")

        book_title = input("Book Title: ")
        price = float(input("Price (RM): "))
        quantity = int(input("Quantity: "))

        book = Book(book_title, price, quantity)

        book_list.append(book)

        counter += 1

    print("\n" + "=" * 50)
    print("BOOK SALES REPORT")
    print("=" * 50)

    index = 0
    grand_total = 0

    while index < len(book_list):
        book = book_list[index]

        print(f"\nBook Number : {index + 1}")
        book.display_information()

        grand_total += book.calculate_total()

        index += 1

    print("\n" + "=" * 50)
    print(f"GRAND TOTAL SALES: RM{grand_total:.2f}")
    print("=" * 50)


if __name__ == "__main__":
    main()