# Operators Demo for AI Calculations
print("=== AI Operators Demo ===")

# Input
a = int(input("Enter marks of Subject 1: "))
b = int(input("Enter marks of Subject 2: "))

# Arithmetic Operators
total = a + b
average = total / 2
percentage = (total / 200) * 100

print(f"\nTotal: {total}")
print(f"Average: {average}")
print(f"Percentage: {percentage}%")

# Comparison & Logical Operators
print("\n--- AI Decision ---")
if average >= 50 and percentage >= 50:
    print("Result: PASS (AI Approved)")
else:
    print("Result: FAIL (AI Rejected)")

# Assignment Operator
accuracy = 90
accuracy += 5  # Improved model
print(f"Improved Model Accuracy: {accuracy}%")