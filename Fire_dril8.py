base_four = 4
base_eight = 8

sum_four = 0
sum_eight = 0

power_four = 1
for i in range(1, 6):
    power_four *= base_four
    sum_four += power_four

power_eight = 1
for i in range(1, 6):
    power_eight *= base_eight
    sum_eight += power_eight

total_sum = sum_four + sum_eight
print(total_sum)
