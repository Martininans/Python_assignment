
def calculate_sum(numbers):
    return sum(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

def find_smallest(numbers):
    return min(numbers)

def find_largest(numbers):
    return max(numbers)

def main():

    numbers = [int(input("Enter integer {}: ".format(i + 1))) for i in range(3)]
    
    print("Sum:", calculate_sum(numbers))
    print("Average:", calculate_average(numbers))
    print("Product:", calculate_product(numbers))
    print("Smallest:", find_smallest(numbers))
    print("Largest:", find_largest(numbers))

if __name__ == "__main__":
    main()
