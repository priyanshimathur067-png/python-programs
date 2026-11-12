class University:
    def __init__(self, name):
        self.name = name

    class Department:
        def __init__(self, dept_name, hod):
            self.dept_name = dept_name
            self.hod = hod

u = University("MJPRU")
d = u.Department("Computer Science", "Mr. Sharma")

print(u.name)
print(d.dept_name)
print(d.hod)