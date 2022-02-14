
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    
    def __str__(self):
        return (f'\nСтудент\n{"Имя:":.<27} {self.name}\n{"Фамилия:":.<27} {self.surname}\n'
                f'{"Средняя оценка:":.<27} {self.average_grade()}\n'
                f'{"курсы в процессе изучения:":.<27} {", ".join(self.courses_in_progress)} \n'
                f'{"Завершенные курсы:":.<27} { ", ".join(self.finished_courses)}\n')                                                                                 

    def average_grade(self):
        total = 0
        grade_number = 0
        for k,val in self.grades.items():
            for iter_v in val:
                grade_number += 1
                total += iter_v
        return round(total/grade_number, 1)

    def rate_lec(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def average_grade(self):
        total = 0
        grade_number = 0
        for k,v in self.grades.items():
            for iter_v in v:
                grade_number += 1
                total += iter_v
        return round(total/grade_number, 1)

    def __str__(self):
        return (f'\nЛектор\n{"Имя:":.<27} {self.name}\n{"Фамилия:":.<27} {self.surname}\n'
                f'{"Средняя оценка за лекции:":.<27} {self.average_grade()}\n')
                

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'\nРевьюер\n{"Имя:" :.<27} {self.name}\n{"Фамилия:":.<27} {self.surname}\n')

def stud_course_grade(students, course):
        sum_grades = 0
        grade_num = 0
        for stud in students:
            if isinstance(stud, Student) and course in stud.grades.keys():
                for y in stud.grades[course]:
                    sum_grades += y
                    grade_num += 1
        total = round(sum_grades / grade_num, 1) 
        return (f'Средняя оценка за курс {course} всех студентов: {total}\n')

def lecturer_course_grade(lectors, course): #средняя оц.лекторов
        sum_grades = 0
        grade_num = 0
        for lec in lectors:
            if isinstance(lec, Lecturer) and course in lec.grades.keys():
                for y in lec.grades[course]:
                    sum_grades += y
                    grade_num += 1
        total = round(sum_grades / grade_num, 1) 
        return (f'Средняя оценка за курс {course} всех лекторов {total}\n')


first_student = Student('Richard', 'Rou', 'male')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Java']
first_student.finished_courses += ['Git']
second_student = Student('Frank', 'Foreman', 'male')
second_student.courses_in_progress += ['Python']
second_student.finished_courses += ['Git']

cool_reviewer = Reviewer('Joe', 'Doe')
cool_reviewer.courses_attached += ['Python']
super_reviewer = Reviewer('John', 'Smith')
super_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(first_student, 'Python', 10)
cool_reviewer.rate_hw(first_student, 'Python', 6)
cool_reviewer.rate_hw(first_student, 'Python', 8)
cool_reviewer.rate_hw(first_student, 'Python', 5)
cool_reviewer.rate_hw(second_student, 'Python', 9)
cool_reviewer.rate_hw(second_student, 'Python', 9)
cool_reviewer.rate_hw(second_student, 'Python', 8)
cool_reviewer.rate_hw(second_student, 'Python', 7)

cool_lector = Lecturer('Alex','Gendel')
cool_lector.courses_attached += ['Python']
super_lector = Lecturer('Georg','Händel')
super_lector.courses_attached += ['Python']

first_student.rate_lec(cool_lector,'Python', 8)
first_student.rate_lec(cool_lector,'Python', 10)
first_student.rate_lec(super_lector,'Python', 9)
second_student.rate_lec(cool_lector,'Python', 10)
second_student.rate_lec(super_lector,'Python', 10)
second_student.rate_lec(super_lector,'Python', 10)

print(first_student)
print(second_student)
print(cool_lector)
print(super_lector)
print(cool_reviewer)
print(super_reviewer)

print(stud_course_grade([first_student, second_student],'Python'))
print(lecturer_course_grade([super_lector, cool_lector],'Python'))