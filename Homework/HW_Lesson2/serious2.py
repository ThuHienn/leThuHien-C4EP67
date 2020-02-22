z = 1
n = int(input('Nhập số bất kỳ: '))
for i in range (n):
    z = z*(i+1)
    i += 1
print(f'{n}! = {z}')