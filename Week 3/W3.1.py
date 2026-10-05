import sys

print("VIP status tier")

packagePrice = float(input("Base contract package price (RM): "))
membershipDuration = int(input("Member Duration (Options; 1, 2, or 3 years): "))
memberType = int(input("Member type (Option: 1=VIP 2=Standard): "))

if membershipDuration == 1:
    annualRate = 0.05
    if memberType == 1:
        finalAnnualRate = annualRate - 0.01
    else:
        finalAnnualRate = annualRate
elif membershipDuration == 2:
    annualRate = 0.04
    if memberType == 1:
        finalAnnualRate = annualRate - 0.015
    else:
        finalAnnualRate = annualRate
elif membershipDuration == 3:
    annualRate = 0.03
    if memberType == 1:
        finalAnnualRate = annualRate - 0.02
    else:
        finalAnnualRate = annualRate
else:
    print("Error")
    sys.exit()

oneTimeRegTax = packagePrice * 0.06
print(f"One-time registration tax: {oneTimeRegTax:.2f}")

subtotalCost = packagePrice + oneTimeRegTax
print(f"Subtotal Cost: RM{subtotalCost:.2f}")

totalInterst = subtotalCost * (finalAnnualRate/1.0) * membershipDuration
print(f"Total administrative interest: RM{totalInterst:.2f}")

contractValue = subtotalCost + totalInterst
print(f"Total contract value: RM{contractValue:.2f}")

monthlyMemberFee = contractValue / (membershipDuration * 12)
print(f"Monthly membership fee: RM{monthlyMemberFee:.2f}")