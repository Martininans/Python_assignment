principal_amount = int(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: ")) / 100
duration_of_loan = int(input("Enter loan duration in years: "))

NUMBER_OF_MONTHS = 12

rate1 = rate / NUMBER_OF_MONTHS + 1
total_loan = duration_of_loan * NUMBER_OF_MONTHS
numerator = rate / NUMBER_OF_MONTHS * (rate1 ** total_loan)
denominator = (rate1 ** total_loan) - 1

mortgage = principal_amount * (numerator / denominator)

print("Monthly mortgage payment:", mortgage)
