"""
У Олега в банке есть n евро.
Он хочет снять всю сумму наличными. Номиналы еврокупюр равны 1, 5, 10, 20, 100.
Какое минимальное число купюр должен получить Олег после того, как снимет все деньги?
На вход программе поступает одно положительные целое число n.
"""
a = int(input())
b100 = a//100
b20 = (a%100)//20
b10 = (a%20)//10
b5 = (a%10)//5
b1 = (a%5)//1

print(b1+b5+ b10+ b20+ b100)