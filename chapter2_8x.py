print("number".rjust(6), "square".rjust(6), "cube".rjust(6))

for number in range(6):
    square = number ** 2
    cube = number ** 3
    
    print(str(number).rjust(6), str(square).rjust(6), str(cube).rjust(6))
