print("Buy Now, Pay Later (BNPL)")

retailPrice = float(input("Laptop Retail Price (RM): "))
installmentDuration = int(input("Installment Plan Duration (months): "))
interestRate = float(input("Store Financing Interest Rate (%): "))

tax = retailPrice * 0.06
print(f"Tech Import/Luxury Tax: RM{tax}")

afterTax = retailPrice + tax
print(f"Subtotal After Tax: RM{afterTax}")

totalInterest = (afterTax * interestRate) * installmentDuration
print(f"Total Financing Interest: RM{totalInterest}")

totalAmount = totalInterest + afterTax
print(f"Total Amount: RM{totalAmount}")

monthlyPayment = totalAmount / installmentDuration
print(f"Monthly Installment Payment: RM{monthlyPayment}")