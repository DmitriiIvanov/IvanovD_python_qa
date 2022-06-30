"""
Классическая задача для начинающих.
Ваша программа должна считать одно натуральное число, после чего вывести:
“Fizz”, если это число делится на 3;
“Buzz”, если это число делится на 5;
“FizzBuzz”, если выполнены оба предыдущих условия;
само это число в остальных случаях.
"""

num = int(input())
if num%3 == 0 and num%5 == 0:
    print("FizzBuzz")
elif num%3 == 0:
    print("Fizz")
elif num%5 == 0:
    print("Buzz")
else:
    print(num)