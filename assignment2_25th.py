def add_ing_or_ly(input_string):
    if len(input_string) < 3:
        return input_string
    elif input_string[-3:] == 'ing':
        return input_string + 'ly'
    else:
        return input_string + 'ing'

sample_strings = ['abc', 'string', 'on']
for string in sample_strings:
    result = add_ing_or_ly(string)
    print(f"Sample String: '{string}', Expected output: '{result}'")
