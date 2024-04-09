def sum_of_multiples_of_10():
    total = 0
    for i in range(10, 20001, 10):
        total += i
    return total

result = sum_of_multiples_of_10()
formatted_result = "{:,}".format(result)
print("Sum of multiples of 10 between 1 and 20,000 is:", formatted_result)
