def repeat_string_or_return(input_str, num):
    if isinstance(num, int):
        return input_str * num
    else:
        return input_str

input_str1 = 'hello'
num1 = 3
input_str2 = 'hi'
num2 = 4.5

output1 = repeat_string_or_return(input_str1, num1)
output2 = repeat_string_or_return(input_str2, num2)

print(output1)
print(output2)
