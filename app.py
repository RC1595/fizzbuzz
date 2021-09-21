number = [3, 5, 15, 60, 37, 48, 61, 88, 95, 70, 235, 540, 125, 444, 655]

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0: 
        print("Fizz")
    else:
        print(number)

fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(15)
fizz_buzz(60)
fizz_buzz(37)
fizz_buzz(48)
fizz_buzz(61)
fizz_buzz(88)
fizz_buzz(95)
fizz_buzz(70)
fizz_buzz(235)
fizz_buzz(540)
fizz_buzz(125)
fizz_buzz(444)
fizz_buzz(655)

