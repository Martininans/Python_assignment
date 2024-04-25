def calculate_string_length(input_string):
    length = 0
    for char in input_string:
        length += 1
    return length

def get_first_and_last_two_chars(s):
    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[-2:]

def add_ing_or_ly(input_string):
    if len(input_string) < 3:
        return input_string
    elif input_string[-3:] == 'ing':
        return input_string + 'ly'
    else:
        return input_string + 'ing'

def longest_word_and_length(words):
    if not words:
        return None, 0
    
    longest_word = ''
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
    
    return longest_word, max_length

def remove_odd_index_chars(input_str):
    result = ""
    for index, char in enumerate(input_str):
        if index % 2 != 0:
            result += char
    return result

def find_minimum(numbers):
    if not numbers:
        return None
    
    min_number = numbers[0]
    for num in numbers[1:]:
        if num < min_number:
            min_number = num
    
    return min_number

def find_maximum(numbers):
    if not numbers:
        return None
    
    max_number = numbers[0]
    for num in numbers[1:]:
        if num > max_number:
            max_number = num
    
    return max_number

def repeat_string_or_return(input_str, num):
    if isinstance(num, int):
        return input_str * num
    else:
        return input_str

def square_elements(input_list):
    squared_list = [num ** 2 for num in input_list]
    return squared_list

def sum_of_squared_elements(input_list):
    sum_of_squares = sum(num ** 2 for num in input_list)
    return sum_of_squares
