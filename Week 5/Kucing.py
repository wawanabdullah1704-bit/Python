class Kucing:
    def __init__(self, nama, baka, tenaga = 100):
        self.nama = nama
        self.baka = baka
        self.tenaga = tenaga

    def makan(self):
        self.tenaga += 20
        print(f"{self.nama} sedang makan. Teanaga bertambah! (Tenaga semasa: {self.tenaga})")

    def main(self):
        if self.tenaga >= 30:
            self.tenaga -= 30
            print(f"{self.nama} sedang bermain! (Tenaga semasa: {self.tenaga})")
        elif self.tenaga < 30:
            print(f"{self.nama} terlalu letih untuk bermain! Perlu makan dulu.")

    def status(self):
        print(f"Kucing: {self.nama} | Baka: {self.baka} | Tenaga: {self.tenaga}")

