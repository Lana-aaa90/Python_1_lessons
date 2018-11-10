# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

# создаем класс ФИО родителей
class Person:
    def __init__(self, n, f, l):
        self.name = n
        self.first_name = f
        self.last_name = l
    @property
    def full_name(self):
        return'{}{} {}'.format(self.name, self.first_name, self.last_name)
# создаем учебный предмет
class Subject:
    def __init__(self, name_lesson):
        self.name_lesson = name_lesson
# создаем класс учитель с атрибутом предмет (subject)
class Teacher(Person):
    def __init__(self, n, f, l, subject):
        Person.__init__(self, n, f, l)
        self.subject = subject
# создаем класс - ученик с атрибутами мать и отец
class Student(Person):
    def __init__(self, n, f, l, mother, father):
        Person.__init__(self, n, f, l)
        self.mother = mother
        self.father = father
    def get_parents(self):
        return(self.mother.full_name, self.father.full_name)
# создаем учебный клас. Атрибуды цифра и буква, дополнительно список учетилей и учеников.
class My_Class:
    def __init__(self, nomber, char):
        self.nomber = nomber
        self.char = char
        self.teachers = []
        self.students = []
#метод- атрибут - имя класса
    @property
    def name(self):
        return'{}{}'.format(self.nomber, self.char)
    def add_teacher(self, *args):
        for a in args:
            self.add_teachers.append(a)
    def add_student(self, *args):
        for a in args:
            self.add.students.append(a)
# школа
class School:
    def __init__(self):
        self.classes = []
    def add_class(self, *args):
        for a in args:
            self.classes.append(a)
    def get_classes(self):
        return [x.name for x in self.classes]
    def get_students(self, classname):
        students = [x.students for x in self.classes if x.name == classname]
        return [el.full_name for el in students [0]]
    def get_subjects(self, studentname):
        classes = [x for x in self.classes if studentname in [y.full_name for y in x.students]]
        return [x.subject.name for x in classes[0].teachers]
#метод - получить родителей
    def get_parents(self, studentname):
        class_student = [x.students for x in self.classes if studentname in [y.full_name for y in x.students]]
        students = [x for x in class_students[0] if studentname == x.full_name]
        return students[0].get_parents()
    def get_teachers(self, classname):
        teachers = [x.teachers for x in salf.classes if x.name == classname]
        return [x.full_name for x in teachers[0]]
#родителт
mother1 = Person("А.", "Б.", "Иванова")
father1 = Person("В.", "Г.", "Иванов")
mother2 = Person("Д.", "Е.", "Сидорова")
father2 = Person("Ж.", "З.", "Сидоров")
mother3 = Person("И.", "К.", "Гундяева")
father3 = Person("Л.", "М.", "Гудяев")

#предметы
math_subj = Subject("Математика")
liter_subj = Subject("Литература")
ekon_subj = Subject("Экономика")

#Учителя
math_teacher = Teacher("Н.", "О.", "Петрова", math_subj)
liter_teacher = Teacher("П.", "Р.", "Кутузова", liter_subj)
ekon_teacher = Teacher("С.", "Т.", "Родртговна", ekon_subj)

#учеики
student1 = Student("У.", "В.", "Иванов", mother1, father1)
student2 = Student("Ф.", "Ж.", "Сидоров", mother2, father2)
student3 = Student("Х.", "Л.", "Гундяев", mother3, father3)

#классы
class1 = My_Class(8, "А")
class2 = My_Class(9, "Б")

#учителя+классы
class1.add_teacher(math_teacher, ekon_teacher, liter_teacher)
class2.add_teacher(math_teacher, ekon_teacher)

#ученики + классы
class1.add_student(student1)
class1.add_student(student2)
class2.add_student(student3)

#создаем школу
shcool = School()
shcool.add_class(class1, class2)

print("Классы школы: ", school.get_classes())
need_class = "9A"
print('Список учеников класса {}:'.format(need_class), school.get_students(need_class))
need_student = "У.В. Иванов"
print('Предметы ученика {}:'.format(need_class), school.get_subjects(need_class))
print('Родители ученика {}:'.format(need_class), school.get_parents(need_class))
print('Учителя класса {}:'.format(need_class), school.get_teachers(need_class))
