from random import randint, choice
from calc import calc
a = randint(0,9)
b = randint(0,1)
operators_poll = ['+','-','*','/','+','+','+'] #thêm nhiều dấu + để tăng tỉ lệ ra dấu hoặc code để ra dấu theo 1 tỷ lệ
# operator[randint(0,4)] #Cach2
operator = choice(operators_poll)
result = calc(a,b,operator)
random_num = randint(-1,1)
display_result = result + random_num

print(f'{a} {operator} {b} = {display_result}')
choice = input('T/F')
if random_num == 0:
    if choice == 'T':
        print('yayyy')
    else:
        print('sai cmnr')

# Cách 2: if random_num == 0 and choice == 'T and...and...or... => Rối mắt => Hạn chế
#     print('yayyy')