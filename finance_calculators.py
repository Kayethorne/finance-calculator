import math
# User to access to different finance calculators
# Investment calculator and Home repayment calculator
# User to choose which calculation they want to do
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# User to input their choice "investment" or "bond"
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Assumming the user chooses "investment"
if user_choice == "investment":
   principal = float(input("Please enter the amount of money that you are depositing: "))  # User to input the amount of money the user will be depositing (principal amount)
   rate = float(input("Please enter the interest rate that you are depositing (percentage): ")) /100  # User to input the interest rate
   years = int(input("Please enter the number of years that you plan on investing: "))    # The user to input the number of years they will be investing
   interest = input("Enter either 'simple' or 'compound' interest: ").lower()  # The user to choose which interest type "simple" or "compound" interest

   if interest == "simple":
      amount = principal * (1 + rate * years)  # The total amount with simple interest
   elif interest == "compound":
      amount = principal * math.pow((1 + rate), years)  # The amount with compound interest
   else:
      print("Invalid response") # Appropriate error message for invalid response that is not 'simple' or 'compound'
      

   print(f"The total amount after {years} will be {amount}")  # The years and total amount will be displayed

# Assume the user chooses 'bond'
elif user_choice == "bond":
    present_value = float(input("Please enter the present value of the house: ")) # User to enter the present value of the house
    interest_rate = float(input("Please enter the interest rate: ")) /100    # User to enter the interest type
    months = int(input("Please enter the number of months to repay the bond: ")) # The user to enter the number of months that they have to repay the bond
   
    monthly_interest_rate = interest_rate / 12 # Calulating the monthly interest rate
    repayment = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), - months)) 
    
    print(f"The monthly repayment amount will be {repayment}") # The monthly repayment amount should be displayed

else:
   print("Invalid choice")  # Display appropriate error message for invalid response
