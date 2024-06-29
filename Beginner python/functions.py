def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius

def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

def Temperature_converter():
    temp = int(input("Enter your temperature: "))
    unit = input("Enter either (C/F): ").upper()
    
    if unit == "C":
        print(f"{temp} degrees Celsius is equal to {celsius_to_fahrenheit(temp):.2f} degrees Fahrenheit")
    elif unit == "F":
        print(f"{temp} degrees Fahrenheit is equal to {fahrenheit_to_celsius(temp):.2f} degrees Celsius")
    else:
        print("Invalid unit")

Temperature_converter()
