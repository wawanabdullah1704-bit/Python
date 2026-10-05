import sys

print("Buy Now, Pay Later 2.0 (BNPL2.0)")

retailPrice = float(input("Laptop retail price (RM): "))
installmentDuration = int(input("Installment Plan Duration (Option 3, 6, 12, or 24 months): "))

if installmentDuration == 3:
    interestRate = 0.00
elif installmentDuration == 6:
    interestRate = 0.035
elif installmentDuration == 12:
    interestRate = 0.05
elif installmentDuration == 24:
    interestRate = 0.075
else:
    print("Invalid installment period")
    sys.exit()

tax = retailPrice * 0.06
print(f"Tech Import/Luxury Tax: RM{tax}")

afterTax = retailPrice + tax
print(f"Subtotal After Tax: RM{afterTax}")

interest = afterTax * (interestRate/100) * (installmentDuration/12)
print(f"Total financing interest: {interest}")

totalPayment = afterTax + interest
print(f"Total Amount Payable: {totalPayment}")

monthlyPayment = totalPayment / installmentDuration
print(f"Monthly installment payment: {monthlyPayment:.2f}")

