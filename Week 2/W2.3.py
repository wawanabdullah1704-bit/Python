print("Cost of Buying Car")

carPrice = float(input("Car Price (RM): "))
loanPeriod = int(input("Loan Period (years): "))
interestRate = float(input("Annual Interest rate (%): "))

tax = carPrice * 0.06
print(f"Tax: {tax}")

cpAfterTax = carPrice + tax
print(f"Car Price After Tax: {cpAfterTax}")

annualInterest = cpAfterTax * interestRate
print(f"Annual Interest: {annualInterest}")

totalInterest = annualInterest * loanPeriod
print(f"Total Interest: {totalInterest}")

totalLoan = totalInterest + cpAfterTax
print(f"Total Loan: {totalLoan}")

monthlyPayment = totalLoan / (loanPeriod*12)
print(f"Monthly Payment: {monthlyPayment}")