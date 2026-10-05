class AkaunBank:
    def __init__(self, pemilik, baki = 0.0):
        self.pemilik = pemilik
        self.baki = baki

    def deposit(self, jumlah):
        self.baki += jumlah
        print(f"RM{jumlah} berjaya disimpan. Baki baru: RM{self.baki}")

    def pengeluaran(self, jumlah):
        if self.baki >= jumlah:
            self.baki -= jumlah
            print(f"RM{jumlah} berjaya dikeluarkan. Baki terkini: RM{self.baki}")
        elif self.baki < jumlah:
            print(f"Pengeluaran gagal! Baki tidak mencukupi. (Baki semasa: RM{self.baki})")

    def semak_baki(self):
        print(f"Akaun: {self.pemilik} | Baki Semasa: RM{self.baki}")

akaun_ahmad = AkaunBank("Ahmad", 100)
akaun_ahmad.semak_baki()
akaun_ahmad.deposit(50)
akaun_ahmad.pengeluaran(120)
akaun_ahmad.pengeluaran(50)