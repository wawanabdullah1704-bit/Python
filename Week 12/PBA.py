# Parent Class untuk kategori umum kenderaan
class Vehicle:
    def __init__(self, plate_number, brand, rental_rate):
        self.plate_number = plate_number
        self.brand = brand
        self.rental_rate = rental_rate

    # Method untuk display maklumat asas kenderaan
    def display_info(self):
        print(f"Plate Number : {self.plate_number}")
        print(f"Brand        : {self.brand}")
        print(f"Daily Rate   : RM {self.rental_rate:.2f}")


# Child Class yang inherit dari class Vehicle
class CargoLorry(Vehicle):
    def __init__(self, plate_number, brand, rental_rate, load_capacity):
        # Panggil constructor parent guna super()
        super().__init__(plate_number, brand, rental_rate)
        # Atribut tambahan khas untuk lori
        self.load_capacity = load_capacity

    # Method overriding untuk custom display guna balik logic parent
    def display_info(self):
        super().display_info()
        print(f"Load Capacity: {self.load_capacity} Tons")


# Main execution
if __name__ == "__main__":
    print("=== VEHICLE MANAGEMENT SYSTEM ===")

    try:
        # Prompt user untuk masukkan details kenderaan
        plate_number = input("Enter plate number: ")
        brand = input("Enter vehicle brand: ")
        rental_rate = float(input("Enter daily rental rate (RM): "))
        load_capacity = float(input("Enter load capacity (tons): "))

        # Instantiate object untuk Child Class
        lorry = CargoLorry(plate_number, brand, rental_rate, load_capacity)

        # Papar output summary kat console
        print("\n--- VEHICLE SUMMARY ---")
        lorry.display_info()

    except ValueError:
        # Tangkap error kalau user tersilap masukkan selain nombor
        print("\nError: Please enter a valid numerical value for rate or capacity.")
