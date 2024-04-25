def find_maximum(numbers):
    if not numbers:
        return None
    
    max_number = numbers[0]
    for num in numbers[1:]:
        if num > max_number:
            max_number = num
    
    return max_number

numbers = [8, 4, 9, 2, 5, 7, 3]
maximum = find_maximum(numbers)
print(maximum)
