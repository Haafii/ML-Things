NumberOfBottlesOneLitterOrLess = int(
    input("Enter number of bottles one ltr or less:"))
NumberOfBottles2To5Litters = int(
    input("Enter number of bottles between 2 and 5 ltr:"))
refundAmount = NumberOfBottlesOneLitterOrLess * \
    10 + NumberOfBottles2To5Litters * 25
print("refund amount is ", round(refundAmount, 2))

