# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# BMI = int(int(weight) / (float(height) * float(height)))
# BMI = int(int(weight) / float(height) ** 2)

import math 
BMI = int(int(weight) / math.pow(float(height), 2))

print(BMI)








