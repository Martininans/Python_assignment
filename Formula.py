import math

C = 50
H = 30

def calculate_Q(D):
    return math.sqrt((2 * C * D) / H)

D = float(input("Enter the value of D: "))

Q = calculate_Q(D)

print("Value of Q:", Q)
