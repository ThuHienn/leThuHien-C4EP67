print('Giải phương trình bậc hai ax^2+bx+c (a khác 0)')

a = int(input('Nhập hệ số a khác 0: '))
b = int(input('Nhập hệ số b: '))
c = int(input('Nhập hệ số c: '))
denta = b**2-4*a*c

if denta <0:
    print('Phương trình vô nghiệm')
elif denta == 0:
    x = -b/(2*a)
    print(f'Phương trình có một nghiệm x = {x}')
else:
    x1 = (-b+ denta**0.5)/(2*a)
    x2 = (-b- denta**0.5)/(2*a)
    print(f'Phương trình có hai nghiệm x1 = {x1}, x2 = {x2}')
    # f = format, {biến}