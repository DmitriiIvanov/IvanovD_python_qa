"""
Однажды, посетив магазин канцелярских товаров, Вася купил X карандашей, Y ручек и Z фломастеров.
 Известно, что цена ручки на 2 рубля больше цены карандаша и на 7 рублей меньше цены фломастера.
 Также известно, что стоимость карандаша составляет 3 рубля.
 Требуется определить общую стоимость покупки.
"""
pencil,pen,felt_tip_pen = map(int,input().split())
pencil_price = (pencil // pencil)*3
pen_price = pencil_price+2
felt_tip_pen_price = pen_price+7

print(pencil*pencil_price + pen*pen_price + felt_tip_pen*felt_tip_pen_price)