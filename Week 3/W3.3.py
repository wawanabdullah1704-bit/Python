print("Tuple")

print(" Custom Theme Color Generator")

# Gather the three components of an RGB color
r = int(input("Enter Red value (0-255): "))
g = int(input("Enter Green value (0-255): "))
b = int(input("Enter Blue value (0-255): "))

# Pack them into a single tuple
custom_color = (r, g, b)

# Check the locked tuple against specific color configurations
if custom_color == (255, 255, 255):
    print("\n You picked White!")
elif custom_color == (0, 0, 0):
    print("\n You picked Black!")
else:
    print(f"\n Your custom RGB code is locked in: {custom_color}")