class EnergyTracker:
    def __init__(self, account_id, monthly_budget_kWh, weekly_usage_kWh):
        self.account_id = account_id
        self.monthly_budget_kWh = monthly_budget_kWh
        self.weekly_usage_kWh = weekly_usage_kWh

    def show_info(self):
        print(f"Account ID     : {self.account_id}")
        print(f"Monthly Budget : {self.monthly_budget_kWh}kWh")
        print(f"Weekly Usage   : {self.weekly_usage_kWh}kWh")

    def check_budget(self):
        total_usage = sum(self.weekly_usage_kWh)
        remaining_budget = self.monthly_budget_kWh - total_usage

        if remaining_budget > 150:
            status = "Efficient Consumption"
        elif remaining_budget > 50:
            status = "Moderate Consumption"
        else:
            status = "Excessive Consumption"

        print(f"Total Usage      : {total_usage}kWh")
        print(f"Remaining Budget : {remaining_budget}")
        print(f"Status           : {status}")

    def get_peak_week(self):
        print(f"Highest Usage : {max(self.weekly_usage_kWh)}kWh")

account_id = input("Enter Account ID : ")

while True:
    try:
        monthly_budget_kWh = float(input("Enter Monthly Budget: "))
        if monthly_budget_kWh > 0:
            break
        print("Budget must be greater than 0")
    except ValueError:
        print("Invalid input! Please enter number.")

weekly_usage_kWh = []

i = 1
while i <= 2:
    try:
        usage = float(input(f"Enter usage {i}: "))
        if usage <= 0:
            weekly_usage_kWh.append(usage)
            i+=1
        else:
            print("Value cannot be negative")
    except ValueError:
        print("Invalid input! Please enter number.")

v1 = EnergyTracker(account_id, weekly_usage_kWh, monthly_budget_kWh)
v1.show_info
v1.check_budget
v1.get_peak_week        