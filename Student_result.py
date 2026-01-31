def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

for i in range(10):
    print("Student", i+1)
    marks = []
    for j in range(5):
        marks.append(int(input("Enter mark: ")))

    total = sum(marks)
    avg = total / 5
    print("Total:", total)
    print("Average:", avg)
    print("Grade:", grade(avg))
