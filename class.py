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
