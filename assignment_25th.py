def calculate_string_length(input_string):
    length = 0
    for char in input_string:
        length += 1
    return length

string = "Welcome to Semicolon"
length = calculate_string_length(string)
print("Length of the string:", length)
