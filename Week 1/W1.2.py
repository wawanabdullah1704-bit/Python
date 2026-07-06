hotel = float(input("Bayaran hotel semalam(seorang): "))

bilPelajar = 20
print(f"Bilangan pelajar: {bilPelajar} orang")

bilHari = int(input("Bilangan hari menginap: "))

bayar = hotel * bilPelajar * bilHari
print(f"Bayaran perlu dibayar(sebelum cukai): {bayar}")

cukai = bayar*0.06
print(f"Jumlah cukai: {cukai}")

bayarCukai = bayar + cukai
print(f"Bayaran perlu dibayar(selepas cukai): {bayarCukai}")

