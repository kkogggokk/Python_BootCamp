# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
total = 0   # 키 전체를 저장할 변수 선언
cnt = 0     # 사람 명수를 세는 변수 선언 

for height in student_heights:
    total += height 
    cnt += 1 

print(round(total/cnt))

