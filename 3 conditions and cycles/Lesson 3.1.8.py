"""
Вы пользуетесь общественным транспортом?
Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером (иногда и с незначащими нулями),
где сумма первых трех цифр равна сумме последних трех.
Т.е. билеты с номерами 385916 и 2011 – счастливые, т.к. 3+8+5=9+1+6 и 0+0+2=0+1+1.
Вам требуется написать программу, которая проверяет счастливость билета.

Программа получает на вход одно целое число N (0 ≤ N < 106) и должна вывести «YES»,
если билет с номером N счастливый и «NO» в противном случае.
"""

stInp = input()
if len(stInp) <6:
    stInp=stInp.rjust(6, "0")

stList = list(map(int, stInp))

a= (stList[0:3])
b= (stList[:-4:-1])

if len(stList) ==6:
    if sum(a) == sum(b):
        print('YES')
    else:
        print("NO")