print("List")

dit1a = []

print("Enter student name. Type done when you are finished")

while True:
    item = input(">  ")
    
    if item.lower() == "done":
        break
    
    dit1a.append(item)
    
print("Student dit1A are:")
print(dit1a)