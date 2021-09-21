class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def avg_grade(self):
        average_grade = {}
        avg_grade_total = float()
        for course in self.grades:
            average_grade.setdefault(course, 0)
            for grade in self.grades[course]:
                average_grade[course] += grade
        for course in average_grade:
            average_grade[course] = average_grade[course] / len(self.grades[course])
            avg_grade_total += average_grade[course]
        if avg_grade_total == 0:
            return 0
        else:
            avg_grade_total = avg_grade_total / len(average_grade)
            return avg_grade_total

    def rate_lec(self, lecturer, course, grade):
        if grade <= 10:
            if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                print('Ошибка, такого лектора на курсе не найдено')
        else:
            print('Оценка лектора может быть только от 0 до 10')

    def __str__(self):
        sep = ', '
        course_progress = sep.join(self.courses_in_progress)
        course_finished = sep.join(self.finished_courses)

        msg = (f'Имя: {self.name} \n'
               f'Фамилия: {self.surname} \n'
               f'Средняя оценка за лекции: {self.avg_grade()}\n'
               f'Курсы в процессе изучения: {course_progress}\n'
               f'Завершенные курсы: {course_finished}\n')
        return msg

    def __lt__(self, other):
        if isinstance(other, Student):
            if self.avg_grade() == other.avg_grade():
                msg = (
                    f'Средние оценки у студентов {self.name} {self.surname} и {other.name} {other.surname} одинаковы\n')
                return msg
            elif self.avg_grade() > other.avg_grade():
                msg = (
                        f'Средняя оценка у студента {self.name} {self.surname} выше, чем у студента {other.name} {other.surname}\n')
                return msg
            else:
                msg = (
                        f'Средняя оценка у студента {other.name} {other.surname} выше, чем у студента {self.name} {self.surname}\n')
                return msg
        else:
            msg = f'{other.name} {other.surname} не является студентом!'
            return msg


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        self.courses_attached = []

    def avg_grade(self):
        average_grade = {}
        avg_grade_total = float()
        for course in self.grades:
            average_grade.setdefault(course, 0)
            for grade in self.grades[course]:
                average_grade[course] += grade
        for course in average_grade:
            average_grade[course] = average_grade[course] / len(self.grades[course])
            avg_grade_total += average_grade[course]
        if avg_grade_total == 0:
            return 0
        else:
            avg_grade_total = avg_grade_total / len(average_grade)
            return avg_grade_total

    def __str__(self):
        msg = (f'Имя: {self.name} \n'
               f'Фамилия: {self.surname} \n'
               f'Средняя оценка за лекции: {self.avg_grade()}\n')
        return msg

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            if self.avg_grade() == other.avg_grade():
                msg = (
                    f'Средние оценки у лекторов {self.name} {self.surname} и {other.name} {other.surname} одинаковы\n')
                return msg
            elif self.avg_grade() > other.avg_grade():
                msg = (
                        f'Средняя оценка у лектора {self.name} {self.surname} выше, чем у лектора {other.name} {other.surname}\n')
                return msg
            else:
                msg = (
                        f'Средняя оценка у лектора {other.name} {other.surname} выше, чем у лектора {self.name} {self.surname}\n')
                return msg
        else:
            msg = f'{other.name} {other.surname} не является лектором!'
            return msg


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        self.courses_attached = []

    def rate_student(self, student, course, grade):
        if grade <= 10:
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                print('Ошибка, проверьте закрепленные списки курсов')
        else:
            print('Оценка студента может быть только от 0 до 10')

    def __str__(self):
        msg = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n')
        return msg


# Инициализация объектов
first_student = Student('Roy', 'Pablo', 'Male')
second_student = Student('Boy', 'Pablo', 'Male')
first_lecturer = Lecturer('Chris', 'Lector')
second_lecturer = Lecturer('Leon', 'Lecturer')
first_reviewer = Reviewer('John', 'Review')
second_reviewer = Reviewer('Jane', 'Reviewer')

# Добавление атрибутов классов
first_student.courses_in_progress.append('Python')
first_student.courses_in_progress.append('C#')
first_student.finished_courses.append('Git')
second_student.courses_in_progress.append('Python')
second_student.courses_in_progress.append('Git')
second_student.finished_courses.append('C#')

first_lecturer.courses_attached.append('Python')
first_lecturer.courses_attached.append('C#')
second_lecturer.courses_attached.append('Git')
second_lecturer.courses_attached.append('Python')

first_reviewer.courses_attached.append('Python')
first_reviewer.courses_attached.append('C#')
second_reviewer.courses_attached.append('Python')
second_reviewer.courses_attached.append('Git')

# Наполняем атрибуты классов
first_student.rate_lec(first_lecturer, 'Python', 9)
first_student.rate_lec(first_lecturer, 'Python', 10)
first_student.rate_lec(second_lecturer, 'Python', 8)
first_student.rate_lec(first_lecturer, 'C#', 7)
first_student.rate_lec(first_lecturer, 'C#', 10)
second_student.rate_lec(second_lecturer, 'Git', 9)
second_student.rate_lec(second_lecturer, 'Git', 10)

first_reviewer.rate_student(first_student, 'Python', 8)
first_reviewer.rate_student(first_student, 'Python', 8)
first_reviewer.rate_student(first_student, 'C#', 8)
second_reviewer.rate_student(first_student, 'Python', 8)
second_reviewer.rate_student(second_student, 'Python', 6)
second_reviewer.rate_student(second_student, 'Git', 7)
second_reviewer.rate_student(second_student, 'Git', 9)

# проверка методов
print(first_student)
print(second_student)
print(first_lecturer)
print(second_lecturer)
print(first_reviewer)
print(second_reviewer)
print(first_lecturer > second_lecturer)
print(first_student > second_student)


def get_avg_students(stud_list, course):
    grade_list = list()
    grade_avg = int()
    grade_total = int()
    for student in stud_list:
        if course in student.courses_in_progress:
            for name, grade in student.grades.items():
                if name == course:
                    for value in grade:
                        grade_avg += value
            grade_list.append(grade_avg / len(student.grades[course]))
            grade_avg = 0
    for grades in grade_list:
        grade_total += grades
    print(f'Средняя оценка студентов на курсе {course}: {grade_total / len(grade_list)}')


def get_avg_lecturers(lect_list, course):
    grade_list = list()
    grade_avg = int()
    grade_total = int()
    for lecturer in lect_list:
        if course in lecturer.courses_attached:
            for name, grade in lecturer.grades.items():
                if name == course:
                    for value in grade:
                        grade_avg += value
            grade_list.append(grade_avg / len(lecturer.grades[course]))
            grade_avg = 0
    for grades in grade_list:
        grade_total += grades
    print(f'Средняя оценка лекторов на курсе {course}: {grade_total / len(grade_list)}')


list_of_students = [first_student, second_student]
list_of_lecturers = [first_lecturer, second_lecturer]
get_avg_students(list_of_students, 'Git')
get_avg_lecturers(list_of_lecturers, 'Python')
