start= list(map(int, input().split()))
a = start[0]
b = start[1]

Text1 = f"""Разрешение экрана: {a} x {b}."""
Text2 = f"""Общее количество пикселей = {a*b}."""
print(Text1)
print(Text2)