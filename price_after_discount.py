
price = float(input("Enter the price: "))
discount_percentage = float(input("Enter the discount percentage: "))

discount_amount = price * (discount_percentage / 100)

price_after_discount = price - discount_amount

print("Price after discount:", price_after_discount)
