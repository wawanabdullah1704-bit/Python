print("Loan barang elektrik")

hargaAsal = float(input("Masukkan harga asal barang: "))

hargaCukai = hargaAsal + (hargaAsal * 0.06)
print(f"Harga barang selepas cuka 6% ialah: {hargaCukai}")

bayarBulan = (hargaCukai + (hargaCukai*0.3))/12
print(f"Bayaran bulan adalah sebanyak (loan setahun): {bayarBulan:.2f}")