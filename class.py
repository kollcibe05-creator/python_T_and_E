class Student:
    #class attributes belong to the whole class
    student_list = []
    student_count = 0
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name
        self.track_student_count()
        self.add_new_student(self)
    @classmethod
    def track_student_count(cls):
        cls.student_count += 1  
    @classmethod
    def add_new_student(cls,self):
        cls.student_list.append(self)      
    
    pass

s1 = Student("Collins", "Kibet")   
s2 =    Student("Yvonne", "Kaino") 
# print(s1.first_name)  
print(Student.student_list)

for student in Student.student_list:
    print(student.first_name, student.second_name)

list_ = [1,0,5,8,9,1,6,5,7,6,11,14,1,0,1,4,14]
print(list_)

set_list = set(list_)    # set ~ unique ~ curly braces  ## tuple ~ duplicated ~ randomized
print(set_list)