
from datetime import date

print("📅 Age Calculator")

birth_year = int(input("Enter your birth year: "))
current_year = date.today().year

age = current_year - birth_year

print("You are", age, "years old.")
