# Parte 1 - Room e Building
class Room:
    def __init__(self, id: str, floor: int, seats: int):
        self.id = id
        self.floor = floor
        self.seats = seats

    def get_id(self) -> str:
        return self.id

    def get_floor(self) -> int:
        return self.floor

    def get_seats(self) -> int:
        return self.seats

    def get_area(self) -> float:
        return self.seats * 2

class Building:
    def __init__(self, name: str, address: str, floors: tuple):
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = []

    def get_floors(self):
        return self.floors

    def get_rooms(self):
        return self.rooms

    def add_room(self, room):
        if self.floors[0] <= room.get_floor() <= self.floors[1]:
            if room not in self.rooms:
                self.rooms.append(room)

    def area(self):
        return sum(room.get_area() for room in self.rooms)

# Parte 2 - Person, Student, Lecturer, Group
class Person:
    def __init__(self, cf: str, name: str, surname: str, age: int):
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age

class Student(Person):
    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)
        self.group = None

    def set_group(self, group):
        self.group = group

class Lecturer(Person):
    def __init__(self, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)

class Group:
    def __init__(self, name: str, limit: int):
        self.name = name
        self.limit = limit
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
            return (len(self.students) + 9) // 10

    def add_student(self, student):
        if len(self.students) < self.limit:
            self.students.append(student)
            student.set_group(self)

    def add_lecturer(self, lecturer):
        if len(self.lecturers) < self.get_limit_lecturers():
            self.lecturers.append(lecturer)

# Parte 3 - Course
class Course:
    def __init__(self, name: str, groups: list = None):
        self.name = name
        self.groups = groups if groups is not None else []

    def register(self, student):
        for group in self.groups:
            if len(group.get_students()) < group.get_limit():
                group.add_student(student)
                return

    def get_groups(self):
        return self.groups

    def add_group(self, group):
        self.groups.append(group)