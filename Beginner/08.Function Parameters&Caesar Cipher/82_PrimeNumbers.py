#Write your code below this line 👇
import math 

def prime_checker(number):
    if number > 1 : 
        for i in range(2, int(math.sqrt(number)+1)):
            if number % i == 0 :
                return False
        return True 
    else : 
        return False 


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

if prime_checker(n): 
    print("It's a prime number.")
else : 
    print("It's not a prime number.")



