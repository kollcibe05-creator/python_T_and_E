list_example = ["Collins", "Barasa", "Collins", "Voke", 'Collins', "Barasa"]

my_dict = {}

for name in list_example:
    # my_dict[name] = my_dict.get(name, 0) + 1
    if name in my_dict:
        my_dict[name] += 1
    else:
        my_dict[name] = 1    
print(my_dict)    