studName = input("Student Name: ")
mathMark =  int(input("Mark for Mathematics (0 t0 100): "))
scienceMark =  int(input("Mark for Science (0 t0 100): "))
engMark =  int(input("Mark for English (0 t0 100): "))

totalMark = mathMark + scienceMark + engMark
print(f"Total Marks: {totalMark}")

averagePercentage = totalMark / 3
print(f"Average Percentage: {averagePercentage:.2f}")

if averagePercentage >= 85:
    category = "Distinction"
    flag = "Excellent Student Honor Roll"
elif averagePercentage >= 80:
    category = "High Merit"
    flag = "Excellent Student Honor Roll"
elif averagePercentage >= 60:
    category = "Pass"
    flag = "No Honor Roll"
elif averagePercentage < 60:
    category = "Need Improvement"
    flag = "No Honor Roll"

print(f"Category: {category}")
print(f"Flag: {flag}")