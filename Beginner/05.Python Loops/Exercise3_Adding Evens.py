#Write your code below this row 👇

even_sum = 0 
for i in range(2,101,2):
    even_sum += i 
print(even_sum)

even_sum2 = 0 
for i in range(2, 101):
    if i % 2 == 0 :
        even_sum2 += i 
print(even_sum2)

