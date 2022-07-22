#Password Generator Project
import random

from numpy import number
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# nr_letters = 4 
# nr_symbols = 2 
# nr_numbers = 2 

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
Eazy_pwd = ""
for i in range(nr_letters): 
    Eazy_pwd += random.choice(letters)

for i in range(nr_symbols):
    Eazy_pwd += random.choice(symbols)

for i in range(nr_numbers): 
    Eazy_pwd += random.choice(numbers)

print(Eazy_pwd)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
Hard_pwd = []
''' 
- 방법1) 갯수대로 뽑고 난 다음에 랜덤하게 정렬하는 방법 => shuffle()
- 2) 전체길이에서 letter, symbol, number 갯수만큼 처음부터 랜덤하게 뽑을수 있나.. 흠..
'''
for i in range(nr_letters): 
    Hard_pwd.append(random.choice(letters)) 

for i in range(nr_symbols):
    Hard_pwd.append(random.choice(symbols))

for i in range(nr_numbers):
    Hard_pwd.append(random.choice(numbers))

random.shuffle(Hard_pwd)
print("".join(Hard_pwd))    # 리스트를 문자형으로 


# 문자열 시퀀스 자료형 아님 ? The shuffle() method takes a sequence, like a list, and reorganize the order of the items.
# https://toypanda.tistory.com/23 # append시 NoneType 
# print(Hard_pwd)             # 왜 None 타입이지? -> 셔플하고난 다음에 Hard_pwd를 출력해야하는구나 
