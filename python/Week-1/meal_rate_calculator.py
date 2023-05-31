rateOfMeal = float(input("Enter the rate of meal:"))
tax = (12.5*rateOfMeal)/100
tip = (18*rateOfMeal)/100
totalAmount = rateOfMeal + tax + tip
print("Rate of meal is-->", rateOfMeal)
print("Tax is-->", tax)
print("Tip amount is-->", tip)
print("Total amount is-->", round(totalAmount, 2))
