class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.rates = {}


class Lecturer(Mentor):

    def __mid_rates(self):
        mid_sum = 0
        for course_grades in self.rates.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            course_mid = course_sum / len(course_grades)
            mid_sum += course_mid
        if mid_sum == 0:
            return f'Оценки пока не выставлялись!'
        else:
            return f"{mid_sum / len(self.rates.values()):.2f}"

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        res += f'Средняя оценка за лекции: {self.__mid_rates()}\n'
        return res

    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print('Не лектор!')
            return
        return self.__mid_rates() < lecturer.__mid_rates()


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer,
                      Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'

    def __mid_grade(self):
        mid_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            course_mid = course_sum / len(course_grades)
            mid_sum += course_mid
        if mid_sum == 0:
            return f'Оценки пока не выставлялись!'
        else:
            return f"{mid_sum / len(self.grades.values()):.2f}"

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        res += f'Средняя оценка за домашние задания: {self.__mid_grade()}\n'
        res += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        res += f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def __lt__(self, student):
        if not isinstance(student, Student):
            print('Не студент!!')
            return
        return self.__mid_grade() < student.__mid_grade()


def stud_grades(stud_list, course):
    mid_sum = 0
    iterations = 0
    for stud in stud_list:
        if course in stud.grades.keys():
            stud_sum = 0
            for grades in stud.grades[course]:
                stud_sum += grades
            stud_mid = stud_sum / len(stud.grades[course])
            mid_sum += stud_mid
            iterations += 1
    if mid_sum == 0:
        return f'Оценок нет!'
    else:
        return f"{mid_sum / iterations:.2f}"


def lector_rates(lector_list, course):
    mid_sum = 0
    iterations = 0
    for lector in lector_list:
        if course in lector.rates.keys():
            lector_sum = 0
            for rates in lector.rates[course]:
                lector_sum += rates
            lector_mid = lector_sum / len(lector.rates[course])
            mid_sum += lector_mid
            iterations += 1
    if mid_sum == 0:
        return f'Оценок нет!'
    else:
        return f"{mid_sum / iterations:.2f}"


# create students
first_student = Student('Roy', 'Eman', 'Male')
first_student.courses_in_progress += ['Enter course']
first_student.courses_in_progress += ['GIT']
first_student.courses_in_progress += ['Python']

second_student = Student('John', 'Dow', 'Male')
second_student.courses_in_progress += ['Enter course']
second_student.courses_in_progress += ['GIT']
second_student.courses_in_progress += ['Python']

# create reviewers
first_reviewer = Reviewer('Some', 'Buddy')
first_reviewer.courses_attached += ['Python']

second_reviewer = Reviewer('Once', 'Told')
second_reviewer.courses_attached += ['Enter course']
second_reviewer.courses_attached += ['GIT']

# create lecturers
first_lecturer = Lecturer('Methe', 'World')
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Isgona', 'Rollme')
second_lecturer.courses_attached += ['Enter course']
second_lecturer.courses_attached += ['GIT']

# students grades
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 8)
first_reviewer.rate_hw(first_student, 'Python', 9)
first_reviewer.rate_hw(second_student, 'Python', 7)
first_reviewer.rate_hw(second_student, 'Python', 8)
first_reviewer.rate_hw(second_student, 'Python', 8)

second_reviewer.rate_hw(first_student, 'GIT', 9)
second_reviewer.rate_hw(first_student, 'GIT', 9)
second_reviewer.rate_hw(first_student, 'GIT', 8)
second_reviewer.rate_hw(second_student, 'GIT', 8)
second_reviewer.rate_hw(second_student, 'GIT', 7)
second_reviewer.rate_hw(second_student, 'GIT', 7)

second_reviewer.rate_hw(first_student, 'Enter course', 9)
second_reviewer.rate_hw(second_student, 'Enter course', 7)

# lectures rates
first_student.finished_courses += ['Enter course']
first_student.courses_in_progress.remove('Enter course')
first_student.finished_courses += ['GIT']
first_student.courses_in_progress.remove('GIT')
first_student.rate_lecturer(second_lecturer, 'Enter course', 7)
first_student.rate_lecturer(second_lecturer, 'GIT', 10)
first_student.rate_lecturer(second_lecturer, 'GIT', 9)
first_student.rate_lecturer(second_lecturer, 'GIT', 9)

second_student.finished_courses += ['Enter course']
second_student.courses_in_progress.remove('Enter course')
second_student.rate_lecturer(second_lecturer, 'Enter course', 8)
second_student.finished_courses += ['Python']
second_student.courses_in_progress.remove('Python')
second_student.rate_lecturer(first_lecturer, 'Python', 9)
second_student.rate_lecturer(first_lecturer, 'Python', 10)
second_student.rate_lecturer(first_lecturer, 'Python', 8)

print(first_student)
print(second_student)
if first_student > second_student:
    print("Первый студент учится лучше! \n")
else:
    print("Второй студент учится лучше! \n")
print(first_reviewer)
print(second_reviewer)
print(first_lecturer)
print(second_lecturer)
if first_lecturer > second_lecturer:
    print("Первый лектор оценивается выше! \n")
else:
    print("Второй лектор оценивается выше! \n")


students_list = [first_student, second_student]

print(f'Средняя оценка среди студентов курса "Python": {stud_grades(students_list, "Python")}')
print(f'Средняя оценка среди студентов курса "GIT": {stud_grades(students_list, "GIT")}')
print(f'Средняя оценка среди студентов курса "Enter course": {stud_grades(students_list, "Enter course")}\n')

lectors_list = [first_lecturer, second_lecturer]

print(f'Средняя оценка лекторов курса "Python": {lector_rates(lectors_list, "Python")}')
print(f'Средняя оценка лекторов курса "GIT": {lector_rates(lectors_list, "GIT")}')
print(f'Средняя оценка лекторов курса "Enter course": {lector_rates(lectors_list, "Enter course")}')
