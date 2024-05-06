def main():
    print("How many students do you have?")
    number_of_students = int(input())

    print("How many subjects do they offer?")
    number_of_subjects = int(input())

    print("Saving >>>>>>>>>>>>>>>>>>\nSaved successfully\n")

    subjects = []
    for i in range(number_of_subjects):
        print("Enter the name of subject", i + 1)
        subjects.append(input())

    scores = []
    for i in range(number_of_students):
        print("Entering scores for student", i + 1)
        student_scores = []
        for j in range(number_of_subjects):
            score = -1
            while score < 0 or score > 100:
                try:
                    score = int(input("Enter score for {} for student {}: ".format(subjects[j], i + 1)))
                    if score < 0 or score > 100:
                        print("Enter a valid score (within 0 to 100)")
                except ValueError:
                    print("Please enter a valid integer score.")
            student_scores.append(score)
        scores.append(student_scores)
        print("Saving >>>>>>>>>>>>>>>>>>\nSaved successfully\n")

    print("====================================================")
    print("STUDENT\t\t\t", end="")
    for i in range(number_of_subjects):
        print("SUB{}".format(i + 1), end="\t")
    print("Total\tAverage\tPosition")
    print("====================================================")

    for i, student_scores in enumerate(scores, start=1):
        print("Student", i, end="\t\t")
        total = sum(student_scores)
        for score in student_scores:
            print(score, end="\t")
        average = total / number_of_subjects
        print("{}\t{:.2f}\t{}".format(total, average, i))

    print("======================================================")
    print("=======================================================")


main()
