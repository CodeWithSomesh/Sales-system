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
            print("\n")
            return int(itemsSold)


def restartProgram():

    # Initialize Variables
    restart = ""

    # Ask User for input to whether restart or exit program
    while True:
        restart = input("Print next employee's details? [Y/N]: ").upper()
        if restart == "Y":
            os.system("pause")
            os.system("cls")
            main()
        elif restart == "N":
            print("Thanks for using the system, have a nice day!")
            exit()
        else:
            print("Invalid Input, Please Key In The Correct Input")
            continue


def main():

    # Declare and Initialize Variables
    name = ''
    tier = ''
    baseSalary = 0.00
    itemsSold = 0
    commission = 0
    monthlyPayment = 0.00
    restart = ""

    # Ask user for Employee Name, Tier, Base Salary and Number of Items Sold
    name = validate_Name()
    tier = validate_Tier()
    baseSalary = validate_BaseSalary()
    itemsSold = validate_ItemsSold()

    # Print Employee Details
    print(f"Employee: {name}")
    print(f"Monthly Base: {baseSalary}")
    print(f"Tier: {tier}")
    print(f"Employee: {name}")
    print(f"Items Sold: {itemsSold}")


    # Calculate and Print Monthly Payment
    if tier == 'B':
        if itemsSold > 15:
            commission = ((itemsSold - 15) * 75) + (50 * 6)
            monthlyPayment = baseSalary + commission
            print(f"Monthly Payment: {monthlyPayment}")
            print("\n")
        elif itemsSold > 9:
            commission = (itemsSold - 9) * 50
            monthlyPayment = baseSalary + commission
            print(f"Monthly Payment: {monthlyPayment}")
            print("\n")
        elif itemsSold < 6:
            print(f"Monthly Payment: {baseSalary}")
            print("WARNING: Sales must improve.")
            print("\n")
        else:
            print(f"Monthly Payment: {baseSalary}")
            print("\n")
    elif tier == 'M':
        if itemsSold > 20:
            commission = ((itemsSold - 20) * 100) + (60 * 6)
            monthlyPayment = baseSalary + commission
            print(f"Monthly Payment: {monthlyPayment}")
            print("\n")
        elif itemsSold > 14:
            commission = (itemsSold - 14) * 60
            monthlyPayment = baseSalary + commission
            print(f"Monthly Payment: {monthlyPayment}")
            print("\n")
        elif itemsSold < 9:
            print(f"Monthly Payment: {baseSalary}")
            print("WARNING: Sales must improve in order to stay in Tier M.")
            print("\n")
        else:
            print(f"Monthly Payment: {baseSalary}")
            print("\n")
    elif tier == 'P':
        if itemsSold > 25:
            commission = ((itemsSold - 25) * 125) + (75 * 6)
            monthlyPayment = baseSalary + commission
            print(f"Monthly Payment: {monthlyPayment}")
            print("\n")
        elif itemsSold > 19:
            commission = (itemsSold - 19) * 75
            monthlyPayment = baseSalary + commission
            print(f"Monthly Payment: {monthlyPayment}")
            print("\n")
        elif itemsSold < 14:
            print(f"Monthly Payment: {baseSalary}")
            print("WARNING: Sales must improve to stay in Tier P.")
            print("\n")
        else:
            print(f"Monthly Payment: {baseSalary}")
            print("\n")

            
    # Ask User for input to whether restart or exit program
    restart = restartProgram()


main()
