item1 = float(input("Masukkan harga item 1: "))
item2 = float(input("Masukkan harga item 2: "))
item3 = float(input("Masukkan harga item 3: "))
item4 = float(input("Masukkan harga item 4: "))
item5 = float(input("Masukkan harga item 5: "))

total = item1 + item2 + item3 + item4 + item5

print(f"total item  yang telah dibeli ialah: {total}")

pay = float(input("total duit dibayar oleh pelanggan: "))

baki = pay - total

print(f"Baki duit pelanggan: {baki}")