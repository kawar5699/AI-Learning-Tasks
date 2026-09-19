# Weather AI - Celsius to Fahrenheit
print("=== Weather AI - Temperature Converter ===")
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C = {fahrenheit}°F")

if fahrenheit > 86:
    print("AI Alert: Hot Weather")
elif fahrenheit < 50:
    print("AI Alert: Cold Weather")
else:
    print("AI Alert: Normal Weather")