# #!/usr/bin/env python3
import math
# import sys

# name = sys.argv[1]
# if __name__ == "__main__":
#     print(f"The name is {name}")


# import os
# if __name__ == "__main__":
#     os.system("ls -l")



def enough(cap, on, wait):
    # Your code here
    # cap ~ number it can hold                   56         space = 12 
    # on ~ number of people on the bus           44
    
    # wait ~ number of people waiting            14  
    
    space = cap - on     
    if wait <= space:
        return 0
    else:
        return  wait - space

number = 5        
print(number% 100)    # works


#aug = number ot f people in or leaving
#p - target
def nb_year(p0, percent, aug, p):
    #population po   ~ 1000
    #increase - rate = 2.5% per year
    # additional population = 50 per year
    #target  - 2000

    # target - po = 
    #2.5% * population +  ( 50 )
    # p1 = 
    year = 0
    percentage = percent/100
    while p0< p:
        p0 = int(p0 + percentage * p0 + aug)
        year += 1
    return  year  

                                        ###You must import math
# print(int(math.sqrt(9)))

num = 9
if num <= 1:
    print("Oops")        

else:
    for i in range (2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            print(False)
        else:
            print( True)    

# print(math.sqrt(17))

# import math

def is_prime_basic(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False  # Divisible by another number, not prime
    return True  # No divisors found, it's prime

print(is_prime_basic(7))
# gprm
        
    
    # your code