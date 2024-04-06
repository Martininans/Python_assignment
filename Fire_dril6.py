base_four = 4
base_eight = 8
power_four = 1

for i in range(1, 6):
    power_four *= base_four
    print(power_four, end=" ")

power_eight = 1
for i in range(1, 6):
    power_eight *= base_eight
    print(power_eight, end=" ")
