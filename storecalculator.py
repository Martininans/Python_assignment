print("Welcome to E-Store")
customerName = input("Please Enter Name: ")

print("Welcome to E-Store:", customerName)
numberOfItem = int(input("Please Enter the number of items purchased: "))
rate = float(input("Please Enter interest rate: "))

counter = numberOfItem
bonusCondition = 200
interestRate = rate / 100
initialPrice = 0

while counter != 0:
    costOfItem = int(input("Please Enter cost for Item" + str(counter) + ": "))
    initialPrice += costOfItem
    counter -=

discountPrice = initialPrice * 0.10

if initialPrice >= bonusCondition:
    priceAfterDiscount = initialPrice - discountPrice
    print("Customer Name:", customerName)
    print("Original cost:", initialPrice)
    print("Discounted cost:", round(discountPrice, 2))
    print("Thanks for using E-store!!!")
else:
    print("Discounted cost: 0 (no discount)")
