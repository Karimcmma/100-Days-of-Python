# Goal: Calculate a tip and split the total bill among people.
# This project is a placeholder for the day's Python exercise.
# Showcasing data types, functions, integers and strings

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

tip_amount = total_bill * (tip_percentage / 100)
total_with_tip = total_bill + tip_amount
amount_per_person = total_with_tip / num_people

print(f"Each person should pay: ${amount_per_person:.2f}")
