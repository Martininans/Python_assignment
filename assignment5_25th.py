def find_minimum(numbers):
    if not numbers:
        return None
    
    min_number = numbers[0]
    for num in numbers[1:]:
        if num < min_number:
            min_number = num
    
    return min_number

numbers = [8, 4, 9, 2, 5, 7, 3]

minimum = find_minimum(numbers)
print(minimum)
