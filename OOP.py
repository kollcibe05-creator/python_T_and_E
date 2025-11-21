# class Shopper:
#     def __init__(self, name):
#         self.name = name
#         self.grocery_items = []

# class GroceryItem:
#     def __init__(self, name, price):
#         self.name = name 
#         self.price = price 

# shopper = Shopper("Malik")
# item1 = GroceryItem("Pine-apple", 500)
# item2 = GroceryItem("Butternut", 900)

# shopper.grocery_items.append(item1)  
# shopper.grocery_items.append(item2)


# for grocery_item in shopper.grocery_items:
#     print(grocery_item.name, grocery_item.price)

class Student:
    all = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #teacher is protected because it is not a part of the constructor#
        self._teacher = None
        Student.all.append(self)

    @property
    def teacher(self):
        return self._teacher
    @teacher.setter
    def teacher(self, value):
        if not isinstance(value, Teacher):
            raise TypeError("Teacher must be an instance of Teacher Class")
        self._teacher = value  

class Teacher:
    def __init__(self, name):
        self.name = name
    def students(self):
        return [student for student in Student.all if student.teacher == self]    #to return their names use student.name   # it is a data accessor or getter ~ retrieve info to be used by other parts of the program
    def add_student(self, student):                                               #it follows the single responsiblity principle and allows flexibility as one can later count(len[]) or filter([s for s in murioki.students() if s.age == 22]) 0r save to database                  
        if not isinstance(student, Student):
            raise TypeError("Student must be an instance of Student Class")
        student.teacher = self    


kamau = Student("Kamau", 22)
murioki = Teacher("Murioki")
jane = Student("jane", 16)

jane.teacher = murioki

kamau.teacher = murioki
print(kamau.teacher.name)
# murioki.add_student(kamau)

# print(kamau.teacher.name)
print(murioki.students())

for student in murioki.students():
    print(student.name)


# print(Kamau.teacher)

# Murioki.add_student("Kamau")

# print(Murioki.students)