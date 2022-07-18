#Write your code below this row 👇
'''
- 1부터 100사이의 숫자를 프린트 하는 프로그램을 작성
- 3의 배수이면 Fizz
- 5의 배수이면 Buzz 
- 15의 배수이면 FizzBuzz 
'''

for i in range(1, 16):
    if i % 15 == 0 : # 15인경우 3, 5의 배수 모두 포함되기 때문에 조건문을 먼저 걸어두자.
        print("FizzBuzz")
    elif i % 3 == 0 : 
        print("Fizz")
    elif i % 5 == 0 : 
        print("Buzz")
    else : 
        print(i)