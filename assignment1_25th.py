def get_first_and_last_two_chars(s):
    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[-2:]
    
print(get_first_and_last_two_chars('semicolon'))
