from abc import ABC, abstractclassmethod


class Person:
    def __init__(self, name: str, yob: int):
        self.name = name
        self.yob = yob

    def get_yob(self):
        return self.yob

    @abstractclassmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(
            f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")


class Ward:
    def __init__(self, name: str):
        self.name = name
        self.people_list = []

    def add_person(self, person: Person):
        self.people_list.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.people_list:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.people_list:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.people_list.sort(key=lambda x: x.get_yob(), reverse=True)

    def compute_average(self):
        total_teacher_age = 0
        count = 0
        for person in self.people_list:
            if isinstance(person, Teacher):
                total_teacher_age += person.get_yob()
                count += 1
        return total_teacher_age/count


student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()


print()
teacher2 = Teacher(name="teacherB ", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name=" Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

print(f"\nNumber of doctors : {ward1.count_doctor()}")

print("\nAfter sorting Age of Ward1 people ")
ward1.sort_age()
ward1.describe()

print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
