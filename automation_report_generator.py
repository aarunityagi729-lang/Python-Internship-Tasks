students = {
    "Aisha": 85,
    "Rahul": 72,
    "Priya": 91,
    "Rohan": 78
}

total = sum(students.values())
average = total / len(students)

highest_student = max(students, key=students.get)
highest_marks = students[highest_student]

report = "STUDENT REPORT\n\n"

for name, marks in students.items():
    report += f"{name}: {marks}\n"

report += f"\nAverage Marks: {average:.2f}"
report += f"\nHighest Marks: {highest_marks} ({highest_student})"

with open("report.txt", "w") as file:
    file.write(report)

print(report)
print("Report generated successfully!")