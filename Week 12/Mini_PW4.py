import numpy as np

# Mini Practical Work 4: Fundamentals of Matrix Processing (Week 13)

print("=== MINI PRACTICAL WORK 4 ===")

# a. Bina 1D NumPy array dengan 5 nombor
numbers = np.array([15, 25, 35, 45, 55])
print("Array Elements :", numbers)

# b. Kira Sum dan Mean guna NumPy function
total_sum = np.sum(numbers)
average_mean = np.mean(numbers)

# c. Papar result kat console
print(f"Sum of Array   : {total_sum}")
print(f"Mean of Array  : {average_mean:.2f}")
