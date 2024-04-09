def print_right_triangle(n):
    for i in range(1, n + 1):
        print("* " * i)

input_number = int(input("Enter a number: "))
if input_number <= 0:
    print("Please enter a positive integer.")
else:
    print("Sample output:")
    print_right_triangle(input_number)
