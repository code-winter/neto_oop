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
        sep = ' '
        course_progress = sep.join(self.courses_in_progress)
        course_finished = sep.join(self.finished_courses)

        msg = (f'Имя: {self.name} \n'
               f'Фамилия: {self.surname} \n'
               f'Средняя оценка за лекции: {self.avg_grade()}\n'
               f'Курсы в процессе изучения: {course_progress}\n'
               f'Завершенные курсы: {course_finished}')
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
        avg_grade_total = avg_grade_total / len(average_grade)
        return avg_grade_total

    def __str__(self):
        msg = (f'Имя: {self.name} \n'
               f'Фамилия: {self.surname} \n'
               f'Средняя оценка за лекции: {self.avg_grade()}')
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
               f'Фамилия: {self.surname}')
        return msg


student_first = Student('My', 'Name', 'Gender')
lecturer_first = Lecturer('My', 'Lecturer')
reviewer_first = Reviewer('My', 'Reviewer')

student_first.courses_in_progress += ['Python']
student_first.courses_in_progress += ['Python1']
student_first.courses_in_progress += ['Python2']
student_first.finished_courses += ['Git']
lecturer_first.courses_attached += ['Python']
lecturer_first.courses_attached += ['Python1']
lecturer_first.courses_attached += ['Python2']
lecturer_first.courses_attached += ['Python22']
reviewer_first.courses_attached += ['Python']

student_first.rate_lec(lecturer_first, 'Python', 10)
student_first.rate_lec(lecturer_first, 'Python1', 10)
student_first.rate_lec(lecturer_first, 'Python', 8)
reviewer_first.rate_student(student_first, 'Python', 10)

lecturer_first.avg_grade()

print(reviewer_first)
print(lecturer_first)
print(student_first)
print(student_first.grades)
print(lecturer_first.grades)