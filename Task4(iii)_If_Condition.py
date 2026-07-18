australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city1 = input("Enter first city: ")
city2 = input("Enter second city: ")

if city1 in india and city2 in india:
    print("Both cities are in India")
elif city1 in uae and city2 in uae:
    print("Both cities are in UAE")
elif city1 in australia and city2 in australia:
    print("Both cities are in Australia")
else:
    print("They don't belong to the same country")