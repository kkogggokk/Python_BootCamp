# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
result = None 

if year % 4 == 0 : 
    if year % 100 == 0 : 
        if year % 400 == 0 : 
            # print("Leap year.")
            result = True 
        else : 
            # print("Not leap year.")
            result = False
    else : 
        # print("Leap year.")
        result = True 
else : 
    # print("Not leap year.")
    result = False 

if result : 
    print("Leap year.")
else : 
    print("Not leap year.")
