"""
Программа получает на вход три натуральных числа A, B и C через пробел.
Вам необходимо вывести "YES" в том случае, если A + B = C и вывести NO в противном случае.
"""

startList = list(map(int, input().split()))
a=startList[0]
b=startList[1]
c=startList[2]
if (a+b)==c:
    print('YES')
else:
    print('NO')