class User:
    def __init__(self, name):
        print("User.__init__ called.")
        self.name = name

    def log_in(self, name):
        self.logged_in = True

class Student(User):
    def __init__(self, name, grade):
        print("Student.__init__ called.")
        super().__init__(name)
        self.grade = grade
    def log_in(self):
        super().log_in()
        self.in_class = True 
        return self.in_class       

stude = Student("Collo", 99)
# print(stude.name)
# print(stude.__dict__)


multiply = lambda n: n + 9

# print(multiply(60))

def myfunc(x):
    return lambda a,b : (a +b) * x

sum_1 = myfunc(60)    

# print(sum_1(20,40))




list_ = [0,1,2,3,4,5,6,7,8,9]

print(list_[::-1])

reversed_name = list(reversed('Collo'))
name = "Collo"
print(reversed_name == list(name[::-1]))





#reversing a string##################

# word = "americano"
# # print(word)

# # print(word.())
# # print(dir(word))
# string_holder_list = []

# for letter in word:
#     # print(letter)
#     string_holder_list.append(letter)
# print(string_holder_list)
# string_holder_list.reverse()
# print(string_holder_list)



# i = [['red','truck'],['blue','truck'],['red','sedan']]
# print(sorted(i, key=lambda v: v[1]))



# print(str.__dir__)



    
