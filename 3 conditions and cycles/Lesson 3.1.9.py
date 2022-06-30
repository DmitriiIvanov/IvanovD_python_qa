"""
Напишите программу, которая на вход получает координаты двух клеток шахматной доски и выводит сообщение о том,
являются ли эти клетки одного цвета. Столбцы на шахматной доске обозначаются английскими строчными буквами.
Программа должна выводить YES, когда клетки одного цвета, NO - разного.
Гарантируется, что значение колонок это латинские буквы abcdefgh, а строки это символы цифр от 1-8
"""

cell1 = input()
let1=cell1[0]
num1=int(cell1[1])
if ord(let1)%2!=0 and num1 %2!=0 or ord(let1)%2==0 and num1 %2==0:
    color_cell1 = 1
else:
    color_cell1 = 2

cell2 = input()
let2=cell2[0]
num2=int(cell2[1])
if ord(let2)%2!=0 and num2 %2!=0 or ord(let2)%2==0 and num2 %2==0:
    color_cell2 = 1
else:
    color_cell2 = 2
if color_cell1 == color_cell2:
    print("YES")
else:
    print("NO")