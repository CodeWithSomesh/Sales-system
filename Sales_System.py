import os


def validate_Name():

    # Initialize Variables
    valid = True
    name = ""


    while valid: # Validate input
        name = input("Enter Employee Name: ") # Ask user for Employee Name
        if name.isnumeric():
            print("Invalid Input, Please Key In The Correct Name")
            continue  # If invalid input, then user get to retry until they enter a valid input
        else:
            return name.title()


def validate_Tier():

    # Initialize Variables
    valid = True
    tier = ""

    while valid:  # Validate input
        tier = input("Enter Employee Tier: ").upper()  # Ask user for Employee Tier
        if tier == 'B':
            return tier
        elif tier == 'M':
            return tier
        elif tier == 'P':
            return tier
        else:
            print("Invalid Input, Please Key In The Correct Tier")
            continue  # If invalid input, then user get to retry until they enter a valid input



def validate_BaseSalary():

    # Initialize Variables
    valid = True
    baseSalary = 0.00

    while valid:  # Validate input
        baseSalary = input("Enter Base Salary: ")  # Ask user for Employee Tier
        if baseSalary.isalpha():
            print("Invalid Input, Please Key In The Correct Salary")
            continue  # If invalid input, then user get to retry until they enter a valid input
        else:
            baseSalary = float(baseSalary)
            return round(baseSalary, 2)


def validate_ItemsSold():

    # Initialize Variables
    valid = True
    itemsSold = 0

    while valid:  # Validate input
        itemsSold = input("Enter Number Of Items Sold: ")  # Ask user for Employee Tier
        if itemsSold.isalpha():
            print("Invalid Input, Please Key In The Correct Salary")
            continue  # If invalid input, then user get to retry until they enter a valid input
        else:
            return int(itemsSold)



def calculate_MonthlyPayment(tier, baseSalary, itemsSold):

    # Initialize Variables
    commission = 0
    monthlyPayment = 0.00

    if tier == 'B':
        if itemsSold < 6:
            print("WARNING: Sales must improve.")
        elif 9 < itemsSold < 16:
            commission = (itemsSold - 9) * 50
            monthlyPayment = baseSalary + commission
            return round(monthlyPayment, 2)
        else:
            print("Invalid")
    elif tier == 'M':
        if itemsSold < 9:
            print("Sales must improve in order to stay in Tier M.")
        elif 14 < itemsSold < 21:
            commission = (itemsSold - 14) * 60
            monthlyPayment = baseSalary + commission
            return round(monthlyPayment, 2)
        else:
            print("Invalid")
    elif tier == 'P':
        if itemsSold < 14:
            print("Sales must improve to stay in Tier P.")
        elif 19 < itemsSold < 26:
            commission = (itemsSold - 19) * 75
            monthlyPayment = baseSalary + commission
            return round(monthlyPayment, 2)
        else:
            print("Invalid")










def main():

    # Declare and Initialize Variables

    # Ask user for Employee Name, Tier, Base Salary and Number of items sold
    name = validate_Name()
    tier = validate_Tier()
    baseSalary = validate_BaseSalary()
    itemsSold = validate_ItemsSold()
    monthlyPayment = calculate_MonthlyPayment(tier, baseSalary, itemsSold)

    print(f"Employee: {name}")
    print(f"Monthly Base: {baseSalary}")
    print(f"Tier: {tier}")
    print(f"Employee: {name}")
    print(f"Items Sold: {itemsSold}")
    print(f"Monthly Payment: {monthlyPayment}")

main()