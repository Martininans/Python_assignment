pass_mark = 45
pass_count = 0
fail_count = 0

print("Enter the scores of 15 students:")
for i in range(1, 16):
    score = int(input(f"Enter score for student {i}: "))
    if score >= pass_mark:
        pass_count += 1
    else:
        fail_count += 1

print("\nNumber of students that passed:", pass_count)
print("Number of students that failed:", fail_count)
