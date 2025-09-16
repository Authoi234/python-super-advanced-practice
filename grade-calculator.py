from bisect import bisect

def calculate_grade(marks):
    if marks >= 80:
        return "A+"
    elif marks >= 70:
        return "A"
    elif marks >= 60:
        return "A-"
    elif marks >= 50:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

def calculate_grade_bisect(marks):
    grades = ["F", "C", "B", "A-", "A", "A+"]
    grade_thresholds = [40,50,60,70,80]
    i = bisect(grade_thresholds, marks)
    return grades[i]

if __name__ == "__main__":
    for i in range(101):
        assert calculate_grade(i) == calculate_grade_bisect(i), i