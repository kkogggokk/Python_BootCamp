# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = round(weight / height ** 2)

if BMI < 18.5 : # underweight
    print(f"Your BMI is {BMI}, you are underweight.")

elif BMI < 25 : # normal weight
    print(f"Your BMI is {BMI}, you have a normal weight.")

elif BMI < 30 : # overweight
    print(f"Your BMI is {BMI}, you are slightly overweight.")

elif BMI < 35 : # obese
    print(f"Your BMI is {BMI}, you are obese.")

else : # clinically obese
    print(f"Your BMI is {BMI}, you are clinically obese.")
     
# print(f"Your BMI is {BMI}, you are {result}.")