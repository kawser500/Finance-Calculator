import math

# Definitions below will come up automatically
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# User input fore either investment or bond calculator 
bond_or_inv = input("Enter either investment or bond from the menu above to proceed: ")
lower_bond_or_inv = bond_or_inv.lower()         #makes input lower case to run below

# If investment selected below inputs required to run calculation
# Simple interest calculation = deposit * (1 * (interest_rate divide 100) * years)
# Compound interest = deposit * (1 + (interest_rate divide 100)) to power of years

if lower_bond_or_inv == "investment": 
    deposit = float(input("Please enter the amount of money you wish to deposit: "))
    inv_interest_rate = float(input("Please enter the interest rate as a percentage: "))
    years = int(input("Please enter how many years you plan on investing: "))
    simple_or_compound = input("Please enter if you would like simple or compound interest: ")
    lower_simple_or_compound = simple_or_compound.lower()           # Input becomes lowercase

    inv_interest_rate_divide_100 = inv_interest_rate/100            
    
    # If input simple - then simple interest calculation as below
    if lower_simple_or_compound == "simple":
        simple_interest = deposit * (1 + inv_interest_rate_divide_100 * years)
        simple_interest_rounded = round(simple_interest, 2)         # Rounded to 2 decimal places
        print(simple_interest)

    # If input compound then compound interest formula as below
    elif lower_simple_or_compound == "compound":
        compound_interest = deposit * math.pow((1 + inv_interest_rate_divide_100),years)
        compound_interest_rounded = round(compound_interest, 2)     # Rounded to 2 decimal places
        print(compound_interest_rounded)

    else:
        # Error handling message
        print("Error. Please enter simple or compound.")           

# If bond entered then below inputs required
elif lower_bond_or_inv == "bond": 
    house_value = int(input("Please enter the value of the house: "))
    bond_interest_rate = float(input("Please enter the interest rate: "))
    bond_month_repay = int(input("Please enter how many months you plan to take to repay the bond: "))

    # Bond_interest_rate assumes annual interest rate so is divided by 100 then to get monthly rate is divided by 12
    monthly_interest_rate = (bond_interest_rate/100)/12  

    repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate) ** (-bond_month_repay))        # Bond monthly repayment formula
    repayment_rounded = round(repayment, 2)                  # Rounded to 2 decimal places

    print(f"You will have to repay £{repayment_rounded} every month")


else:
    # Error handling message
    print("Error. Please enter either investment or bond to continue.")
