# # Kiểm soát vòng lặp: Cách 1
# count = 0
# while count < 3:
#     print('loop...')
#     count = count + 1
# Cách 2
loop = True
count = 0
while loop:
    print('loop')
    if count == 4:
        loop = False
    count = count + 1 