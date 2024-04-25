def remove_odd_index_chars(input_str):
    result = ""
    for index, char in enumerate(input_str):
        if index % 2 != 0:
            result += char
    return result

input_str = "semicolon"
output_str = remove_odd_index_chars(input_str)
print(output_str)
