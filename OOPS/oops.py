class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return (sum(self.marks) / len(self.marks))


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

        
daksh=WorkingStudent('daksh','Almamater',19000)
daksh.marks.append(99)
daksh.marks.append(99)
daksh.marks.append(99)
r=daksh.average()
print(r)