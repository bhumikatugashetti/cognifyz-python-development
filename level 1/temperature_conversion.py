def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temperature = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").upper()

if unit == "C":
    result = celsius_to_fahrenheit(temperature)
    print("Converted temperature:", result, "F")

elif unit == "F":
    result = fahrenheit_to_celsius(temperature)
    print("Converted temperature:", result, "C")

else:
    print("Invalid unit.")
    