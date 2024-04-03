
p = 1000

r = 0.07

years = [10, 20, 30]

for year in years:

    a = p * (1 + r) ** year
    print(f"After {year} years, the amount on deposit will be ${a:.2f}")
