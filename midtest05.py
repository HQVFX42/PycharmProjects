class Department:
    def __init__(self, deptName):
        self.deptName = deptName
    def __str__(self):
        return "[학과] "+self.deptName

class Student(Department):
    def __init__(self, deptName, studentName):
        Department.__init__(self, deptName)
        self.studentName = studentName
    def __str__(self):
        return super().__str__() + " [이름] " + self.studentName

def main():
    student1 = list()
    for i in range(2):
        deptName = input("학과")
        studentName = input("이름")
        student1.append(Student(deptName,studentName))

    for i in student1:
        print(i.__str__())

main()