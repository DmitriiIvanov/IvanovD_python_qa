"""
На вход поступают три целых числа - стороны треугольника.
Необходимо вывести True, если данные стороны образуют прямоугольный треугольник, в противном случае - False.
Для написания программы необходимо вспомнить теорему Пифагора
Сделать задачу необходимо без использования условного оператора.
"""
a, b, c = list(map(int,input(). split()))
print(a*a==(b*b+c*c) or b*b==(c*c+a*a) or c*c==(b*b+a*a))