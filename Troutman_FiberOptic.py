# Calvin Troutman
# CIS245 Introduction to Programming
# 3.1 Assignment

# A program that will calculate the cost of installing fiber optic cable at a cost of .87 per ft for a company.

# Display Welcome Message
print("Welcome to Fiber Optic 4 U!")

# Request Company Name
CompanyName = input("What is your Company's name?")

# Request Number of Feet Needed
NumberOfFeet = float(input("Enter amount of fiber optic needed in feet:"))

# Compute Total Cost
TotalCost = NumberOfFeet*0.87

# Display Total Cost for Company
print(f"It will cost {CompanyName} ${TotalCost} to install fiber optic.")
