# class MyArray:
#     def __init__(self):
#         self.dictionary = {}
#         self.length = 0

#     def push(self, value):
#         self.dictionary[self.length] = value
#         self.length += 1
#     def pop(self):
#         if self.length == 0:
#             return None
#         self.length -= 1
#         return self.dictionary.pop(self.length)          
#     pass

# arr = MyArray()   

# arr.push(1)
# arr.push(2)

# print(arr.dictionary)
# print(arr.length)

# print(arr.pop())




#####First Dupicate value
# list_ = [1, 2, 2, 3,3, 4, 4, 4, 4]
 
# def first_repeated_value(list):
#     for i in range(0, len(list)):
#         for j in range(i+ 1, len(list)):
#             if list[i] == list[j]:
#                 return list[i]
#     return None    

# print(first_repeated_value(list_))

# def first_repeated_value(list):
#     list_set = set()

#     for i in range (0, len(list)):
#         if list[i] in list_set:
#             return list[i]
#         list_set.add(list[i])
#     return None    

# # print(first_repeated_value(list_))    


# # list_1 = ["Collins", "Kibet", "Collo", "Collins"]

# list_1 = [2,2,2, 3]

# # dic = {}
# # for name  in list_1:
# #     dic[name] = dic.get(name, 0) + 1

# # for key, value in dic.items():
# #     if value == 1:
# #         print(key)


# # print(dic)


# stringified = (list_1).split(" ")

# print(stringified)




#stack

def reverse_string(string):
    stack = []

    for char in string:
        stack.append(char)
    reversed = ""
    while stack:
        reversed += stack.pop()
    return reversed   

# print(reverse_string("Collo"))

# def evaluate_keystrokes(string):
#     i = len(string) - 1
#     result = ""
#     skip = 0

#     while i>= 0:
#         if string[i] == "<":
#             skip += 1
#             i -= 1
#         else:
#             if skip > 0:
#                 i -= skip
#                 skip = 0
#             else:
#                 result = string[i] + result        
#     return result


# print(evaluate_keystrokes("abcd<<<fg<h"))

def evaluate_keystrokes(string):
    stack = []
    for char in string:
        if char == "<":
            if len(stack) != 0:
                stack.pop()
        else:
            stack.append(char) 
    result = ''
    while stack:
        result = stack.pop() + result
    return result
    
# print(evaluate_keystrokes("abcd<<<fg<h"))


# singly linked data structure

class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self, head = None):
        self.head = head    
    def append(self,node):
        if self.head == None:
            self.head = node 
            return
        last_node = self.head  
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = node

# To build our singly linked lists,,,,,
list_ = LinkedList()
list_.append(Node("Bulldog"))
list_.append(Node("Chihuahua"))
list_.append(Node("German Shepherd"))



## Doubly linked lists


## The other class isn't affected
def DoublyLinkedList:
    def __init__(self, head= None, tail = None):
        self.head = head
        self.tail = tail
    def append(self, Node):
        if self.head == None:
            self.head = head
            self.tail = node
        node.prev_node = self.tail
        self.tail.next_node = node
        self.tail = node        