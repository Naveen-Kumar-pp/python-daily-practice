"""
Program: Temperature Converter
Description: Converts temperature between Celsius and Fahrenheit
Author: Naveen
"""

# METHOD 1: TEMPERATURE USING (CONDITIONAL CONDITIONAL)

unit = input("Enter a temperature unit (C/F): ").upper()
temp = float(input("Enter the temperature: "))

if unit == "C":
    converted = round((temp * 9/5) + 32, 1)
    print(f"The temperature in Fahrenheit is: {converted}°F")

elif unit == "F":
    converted = round((temp - 32) * 5/9, 1)
    print(f"The temperature in Celsius is: {converted}°C")

else:
    print(f"{unit} is an invalid unit of measurement")


# METHOD 2: TEMPERATURE USING (Function + Return)

def temperature(temp, unit):
    if unit == "C":
        return round((temp * 9/5) + 32, 1), "F"
    elif unit == "F":
        return round((temp - 32) * 5/9, 1), "C"
    else:
        return None, None


unit = input("Enter temperature unit (C/F): ").upper()
temp = float(input("Enter the temperature: "))

result, new_unit = temperature(temp, unit)

if result is not None:
    print(f"Converted temperature: {result}°{new_unit}")
else:
    print("Invalid unit entered")

# METHOD 3: TEMPERATURE USING (Function)

def convert_temperature():
    unit = input("Enter temperature unit (C/F): ").upper()
    temp = float(input("Enter the temperature: "))

    if unit == "C":
        print(f"Converted temperature: {round((temp * 9/5) + 32, 1)}°F")
    elif unit == "F":
        print(f"Converted temperature: {round((temp - 32) * 5/9, 1)}°C")
    else:
        print("Invalid unit entered")


convert_temperature()




