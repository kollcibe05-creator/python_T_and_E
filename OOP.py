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
# print(kamau.teacher.name)
# murioki.add_student(kamau)

# print(kamau.teacher.name)
# print(murioki.students())

# for student in murioki.students():
#     print(student.name)


# print(Kamau.teacher)

# Murioki.add_student("Kamau")

# print(Murioki.students)


class Car:
    def __init__(self, engine):
        self.engine = engine

class Engine:
    def __init__(self, cylinders, fuelType):
        self.cylinders = cylinders
        self.fuelType = fuelType   


four_cylinder_engine = Engine(4, "Diesel")
mazda = Car(four_cylinder_engine)

# print(mazda.engine.cylinders)
# print(mazda.engine.fuelType)


class CPU:
    def __init__(self, cpu_type):
        self.cpu_type = cpu_type

class Computer:
    def __init__(self, cpu_type):
        self.CPU = CPU(cpu_type)


# cpu_ios = CPU("cpu_ios")  

# print(cpu_ios.cpu_type)

Hp = Computer("cpu_ios")

# print(dir(CPU))

class Parent:
    all = []
    def __init__(self,name, children="None"):
        self.name = name
        self._children = []
        if children:
            for child in children:
                self.add_child(child)
        Parent.all.append(self) 
    def children(self):
        return self._children
    def add_child(self, child):
        if isinstance(child, Child):
            self._children.append(child)
        else:
            raise ValueError("Child must be an instance of the Child class.")

class Child:
    def __init__(self, name):
        self.name = name
    def parents(self):
        return [parent for parent in Parent.all if self in  parent.children()]
    def add_parent(self, parent):
        if isinstance(parent, Parent):
            parent.add_child(self)
        else:
            raise ValueError("Parent must be an instance of the Parent Class.") 

# parent1 = Parent("Morgan")
# parent2 = Parent("Tate") 
# child1 = Child("Morty")
# child2 = Child("Dora") 

# parent1.add_child(child1)
# parent2.add_child(child)
# child2.add_parent(parent1)
# child2.add_parent(parent2)


# [print(c.name) for c in parent1.children()]

