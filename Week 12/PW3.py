# Program Secure Mathematical Calculation System (PW3)
# Menggunakan Multiple Exception Handling untuk operasi bahagi

print("=== SECURE MATHEMATICAL CALCULATION SYSTEM ===")

# While loop supaya program terus berjalan sehingga calculation berjaya
while True:
    try:
        # Input handling: minta user masukkan dua nombor untuk division
        num1 = float(input("\nEnter first number (numerator): "))
        num2 = float(input("Enter second number (divisor): "))

        # Buat operasi bahagi
        result = num1 / num2

        # Papar output dalam format 2 decimal places
        print(f"Result: {num1} / {num2} = {result:.2f}")

        # Bila calculation dah berjaya, kita stop loop guna break
        break

    # 3.2.1 Handle error kalau user tersilap masukkan teks selain nombor
    except ValueError:
        print("Error! Sila masukkan nombor sahaja.")

    # 3.2.2 Handle error kalau user letak 0 sebagai divisor
    except ZeroDivisionError:
        print("Error! Divisor tidak boleh 0.")

    # Finally block akan sentiasa dipanggil setiap kali selesai satu cycle
    finally:
        print("Calculation cycle completed.")
