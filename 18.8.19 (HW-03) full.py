a=int(input('Количество билетов: '))  # amount
age=list(map(int, input('Укажите возраст посетителей через пробел: ').split())) #
# p1=0 # price_1 - бесплатная категория до 18 лет
p2=990 # price_2
p3=1390 # price_3
s=0.1 # sale
f=0 # full price
t=0 # total
c=0 # cointer
if a==len(age):
    if min(age)>0 and max(age)<100:
        for i in age:
            c+=1
            if 18<=i<25:
                f+=p2
            elif i>=25:
                f+=p3
        if c>3:
            t=f-(f*s)
        else:
            t=f
        print()
        print('Билетов -', c, 'шт')
        print('Полная цена -', f,'Руб')
        print('Сумма к оплате -', int(t),'Руб')
    else:
        print('Некорректно указан возраст. Повторите ввод')
else:
    print('Неверное количество билетов. Повторите ввод')