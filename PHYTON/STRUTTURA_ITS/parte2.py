class Person:
    def __init__(self, cf:str, name:str, surname:str, age:int):
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age

class Student(Person):
    def __init__ (self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)
        self.group = None

    def set_group(self, group):
        self.group = group

class Lecturer(Person):
    def __init__(self, cf:str, name:str, surname:str, age:int):
        super().__init__(cf, name, surname, age)

class Group:
    def __init__(self, name:str, limit:int):
        self.name = name
        self.limit = 10
        self.students = []
        self.lecturers = []
    def get_name(self):
        return self.name
    def get_limit(self):
        return self.limit
    def get_students(self):
        return self.students
    
    def get_limit_lecturers(self):
        if self.limit > 0:
            return (len(self.students) + 9 // 10)
        
    def add_student(self, student):
        if len(self.students) < self.limit:
            self.students.append(student)
        
    def add_lecturer(self, lecturer):
        if len(self.lecturers) < (self.get_limit_lecturers()):
            self.lecturers.append(lecturer)
        

