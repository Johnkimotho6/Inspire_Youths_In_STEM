distance = int(input("Distance: "))
unit = input("(K) or (M): ")
if unit.upper() == "K":
    converted = distance * 1000
    print("Distance is", converted , "meters")
else:
    converted = distance / 1000
    print("Distance is", converted, "Kilometers")