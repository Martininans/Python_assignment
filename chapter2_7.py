
def check_multiple(number, divisor):
    if number % divisor == 0:
        print(number, "is a multiple of", divisor)
    else:
        print(number, "is not a multiple of", divisor)

check_multiple(1024, 4)
check_multiple(2, 10)
