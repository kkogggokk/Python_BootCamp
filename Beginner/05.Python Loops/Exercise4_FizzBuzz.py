#Write your code below this row ๐
'''
- 1๋ถํฐ 100์ฌ์ด์ ์ซ์๋ฅผ ํ๋ฆฐํธ ํ๋ ํ๋ก๊ทธ๋จ์ ์์ฑ
- 3์ ๋ฐฐ์์ด๋ฉด Fizz
- 5์ ๋ฐฐ์์ด๋ฉด Buzz 
- 15์ ๋ฐฐ์์ด๋ฉด FizzBuzz 
'''

for i in range(1, 16):
    if i % 15 == 0 : # 15์ธ๊ฒฝ์ฐ 3, 5์ ๋ฐฐ์ ๋ชจ๋ ํฌํจ๋๊ธฐ ๋๋ฌธ์ ์กฐ๊ฑด๋ฌธ์ ๋จผ์  ๊ฑธ์ด๋์.
        print("FizzBuzz")
    elif i % 3 == 0 : 
        print("Fizz")
    elif i % 5 == 0 : 
        print("Buzz")
    else : 
        print(i)