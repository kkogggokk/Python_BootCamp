#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? ")[1:])  # $같이 입력받을 시 처리 
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# each_pay = round((total_bill / people) * (1.0 + tip / 100),2) 
# print(f"Each person should pay: ${each_pay}")

each_pay = (total_bill / people) * (1.0 + tip / 100)
print("Each person should pay: ${:.2f}".format(each_pay))