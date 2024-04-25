def square_elements(input_list):
    squared_list = [num ** 2 for num in input_list]
    return squared_list

input_list = [2, 3, 4, 5, 7]

output_list = square_elements(input_list)
print(output_list)
