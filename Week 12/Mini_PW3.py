# Mini Practical Work 3: Stability with Exception Handling (Week 11)
# Program untuk kira umur pengguna menggunakan try-except

CURRENT_YEAR = 2026

print("=== AGE CALCULATOR SYSTEM ===")

try:
    # Minta user masukkan tahun lahir
    birth_year = int(input("Enter your Year of Birth: "))

    # Kira umur dan papar output
    age = CURRENT_YEAR - birth_year
    print(f"You are {age} years old.")

except ValueError:
    # Papar error message jika user masukkan input bukan angka
    print("Invalid input! Please enter a 4-digit year.")
