
#Phép tính a + b = c
# import random #cách 2: 
from random import randint #,... -> không cần "random." trong "random.randint()"
from calc import calc # #calc1:tênfilecode lấy được luôn vì cùng thư mục, nếu ngoài phải thêm tên thư mục "session6.calc" calc2:tên hàm

a = calc(1,2,'+')
print(a)
# import os
# #Lựa chọn + Tính điểm
# score = 0
# play = True
# while play == True:
#     a = random.randint(0,9)
#     b = random.randint(0,9)
#     c = a + b + random.randint(-1,1)
#     os.system('cls')
#     print(f'Điểm: {score}\n{a} + {b} = {c}')
#     ans = input('1. ĐÚNG\t2. SAI\n')
#     if ans == '1': #tư duy hơi ngược :< => phải kiểm tra kq đúng/sai xong mới so sánh lựa chọn của người chơi!!
#         if a + b == c:
#             score += 1
#         else:
#             score = 0
#     elif ans == '2':
#         if a + b == c:
#             score = 0
#         else: 
#             score += 1
#     if ans == 'stop':
#             break






