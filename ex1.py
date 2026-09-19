# AI - Pass/Fail Predictor
print("=== AI Pass/Fail Predictor ===")
marks = int(input("Enter student marks (0-100): "))

if marks >= 35:
    print(f"Marks = {marks} -> Result: PASS")
    print("AI Prediction: Student will pass")
else:
    print(f"Marks = {marks} -> Result: FAIL")
    print("AI Prediction: Student needs improvement")

print("\nWelcome to Artificial Intelligence")