class Student:

    def __init__(self, name, m1, m2, m3):

        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def calculate_total(self):

        return self.m1 + self.m2 + self.m3

    def calculate_percentage(self):

        total = self.calculate_total()

        return total / 3

    def calculate_grade(self):

        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "A+"

        elif percentage >= 80:
            return "A"

        elif percentage >= 70:
            return "B"

        elif percentage >= 60:
            return "C"

        else:
            return "D"

    def display_result(self):

        total = self.calculate_total()
        percentage = self.calculate_percentage()

        print("Student Name:", self.name)
        print("Total Marks:", total)
        print("Percentage:", percentage, "%")
        print("Grade:", self.calculate_grade())

        if all(40 <= mark <= 100 for mark in
               [self.m1, self.m2, self.m3]):
            print("Result: Pass")
        else:
            print("Result: Fail")


s1 = Student("Priya", 85, 90, 80)

s1.display_result()