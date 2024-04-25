def multiplication_table(number):
    for i in range(1, 13):
        result = number * i
        print(f"{number} x {i} = {result}")

input_number = int(input("Enter a number: "))
print("Multiplication table for", input_number)
multiplication_table(input_number)
