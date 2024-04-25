def sum_of_squared_elements(input_list):
    sum_of_squares = sum(num ** 2 for num in input_list)
    return sum_of_squares

input_list = [2, 3, 4, 5, 7]

result = sum_of_squared_elements(input_list)
print(result)
