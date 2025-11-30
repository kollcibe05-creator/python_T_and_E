list_example = ["Collins", "Barasa", "Collins", "Voke", 'Collins', "Barasa"]

my_dict = {}

for name in list_example:
    # my_dict[name] = my_dict.get(name, 0) + 1
    if name in my_dict:
        my_dict[name] += 1
    else:
        my_dict[name] = 1    
print(my_dict)  

even_remove_odd = [2, 4, 0, 100, 4, 11, 2602, 36] #-->  11 (the only odd number)

odd_remove_even = [160, 3, 1719, 19, 11, 13, -21] #--> 160 (the only even number)



def find_outlier(integers):
    pass

# print(find_outlier(even_remove_odd))   


a = [1,2,3]
b = [1,2,3]

if a is b:
    print("same")
else:
    print("different")    
