# Modular Function
def computeNetSalary(grossSalary):
    taxRate = 0.06
    taxAmount = grossSalary * taxRate
    netSalary = grossSalary - taxAmount
    return netSalary

# Parent Class
class Employee:
    def __init__(self, empID, empName, empBaseSalary):
        self.__id = empID
        self.__name = empName
        self.__baseSalary = empBaseSalary

    # Getter Methods
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_baseSalary(self):
        return self.__baseSalary

    # Setter Methods
    def set_id(self, empID):
        self.__id = empID

    def set_name(self, empName):
        self.__name = empName

    def set_baseSalary(self, empBaseSalary):
        self.__baseSalary = empBaseSalary

# Child Class
class Manager(Employee):
    def __init__(self, empID, empName, empBaseSalary, empDepartment):
        super().__init__(empID, empName, empBaseSalary)
        self.empDepartment = empDepartment

    # Function Overloading (calculate monthly bonus)
    def calculateBonus(self, factor1=0.0, factor2=0.0):
        bonus1 = self.get_baseSalary() * factor1
        bonus2 = self.get_baseSalary() * factor2
        return bonus1 + bonus2

# Main Execution
if __name__ == "__main__":
    # Buat Manager objects
    manager1 = Manager("M001", "Wawan", 5000.00, "IT Department")
    manager2 = Manager("M002", "Izzati", 4000.00, "HR Department")

    # Store semua employee objects dalam  list
    employeeList = [manager1, manager2]

    print("-" * 40)
    print("PROFESSIONAL PAYROLL MANAGEMENT SYSTEM")
    print("-" * 40)

    # Loop untuk generate payroll slip
    for emp in employeeList:
        if emp.get_id() == "M001":
            bonus = emp.calculateBonus(0.01)
        else:
            bonus = emp.calculateBonus(0.01, 0.05)

        grossSalary = emp.get_baseSalary() + bonus
        netSalary = computeNetSalary(grossSalary)

        # Output
        print("PAYROLL SLIP")
        print(f"Name: {emp.get_name()}")
        print(f"ID: {emp.get_id()}")
        print(f"Department: {emp.empDepartment}")
        print(f"Base Salary: RM{emp.get_baseSalary():.2f}")
        print(f"Bonus: RM{bonus:.2f}")
        print(f"Gross Salary: RM{grossSalary:.2f}")
        print(f"Net Salary: RM{netSalary:.2f}")
        print("-" * 40)
        