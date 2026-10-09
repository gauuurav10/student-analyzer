class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()

        if not self.marks:
            return "N/A"
        elif avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


student1 = Student("Rahul", 22, [85, 90, 80])
student2 = Student("Priya", 23, [95, 92, 88])
student3 = Student("Amit", 21, [65, 70, 68])

for student in [student1, student2, student3]:
    print(
        f"{student.name} - "
        f"Average: {student.average():.2f} - "
        f"Grade: {student.grade()}"
    )