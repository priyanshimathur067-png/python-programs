class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 80:
            return "A Grade"
        elif percentage >= 60:
            return "B Grade"
        elif percentage >= 40:
            return "C Grade"
        else:
            return "Fail"


s1 = Student("Priya", [85, 90, 78, 88, 95])

print("Total:", s1.calculate_total())
print("Percentage:", s1.calculate_percentage())
print("Grade:", s1.calculate_grade())