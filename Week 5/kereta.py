class Kereta:
    def __init__(self, jenama, warna):
        self.jenama = jenama
        self.warna = warna

    def bunyi_hon(self):
        print(f"Kereta {self.jenama} berbunyi: honnnn")

kereta1 = Kereta("Proton", "Merah")
kereta2 = Kereta("Honda", "Putih")

print(kereta1.jenama)
kereta2.bunyi_hon()