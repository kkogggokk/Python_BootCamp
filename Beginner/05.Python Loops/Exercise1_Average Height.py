# π¨ Don't change the code below π
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# π¨ Don't change the code above π

#Write your code below this row π
total = 0   # ν€ μ μ²΄λ₯Ό μ μ₯ν  λ³μ μ μΈ
cnt = 0     # μ¬λ λͺμλ₯Ό μΈλ λ³μ μ μΈ 

for height in student_heights:
    total += height 
    cnt += 1 

print(round(total/cnt))

