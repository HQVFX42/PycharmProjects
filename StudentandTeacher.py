class Person:
    def __init__(self,name,number):
        self.name = name
        self.number = number
    def __str__(self):
        return "이름 = "+self.name+"\n주민번호 = "+self.number

class Student(Person):
    def __init__(self, name, number, classes, gpa):
        Person.__init__(self,name,number)
        self.classes = classes
        self.gpa = gpa
    def __str__(self):
        return super().__str__()+"\n수강과목 = "+str(self.classes)+"\n평점 = "+str(self.gpa)

class Teacher(Person):
    def __init__(self, name, number, courses, salary):
        Person.__init__(self,name,number)
        self.courses = courses
        self.salary = salary
    def __str__(self):
        return super().__str__()+"\n강의과목 = " + str(self.courses) + "\n평점 = " + str(self.salary)

person1 = Student('홍길동', '12345678', ['자료구조'],0)
person2 = Teacher('김철수', '123456790', ['Python'], 3000000)
print(person1)
print(person2)