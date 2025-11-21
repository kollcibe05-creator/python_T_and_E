#!/usr/bin/env python3

student_details = {
    "first_name" : "Titus",
    "last_name": "Juma",
    "address":{ "city" : "Nairobi",
    "zip-code" : "21000",
    },
    "friends" : ["one", "two", "three"]

}
print(student_details["address"]["city"])
print(student_details["friends"])
print(student_details)
print(student_details.get("address", "Nop"))

print(int.__base__)