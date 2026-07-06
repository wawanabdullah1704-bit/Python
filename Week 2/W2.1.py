print("Employee Salary Calculator")

hourlyWage = float(input("Hourly Wage: "))
hoursWork = float(input("Number of Hours Work: "))

grossSalary = hourlyWage * hoursWork
print(f"Gross Sallary: {grossSalary}")

netSallary = grossSalary - (grossSalary * 0.11)
print(f"Net Sallary: {netSallary}")