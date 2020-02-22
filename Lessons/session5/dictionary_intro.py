# person = ['Đức', 96, 'Hà Nội', 'Sơn La', 'dev', False, True]

# person = {
#     'name': 'Đức', #bên trái dấu ':': key, thường str phải có ' ', không trùng nhau
#     'yob': 96,     #bên phải dấu ':': value, không giới hạn, không index
#     'adress': 'Hà Nội', #ngăn cách nhau bởi dấu phẩy
#     'adress': '...' #không báo lỗi nhưng lấy giá trị dưới cùng => không để key trùng vì khó khăn trong truy cập
# }
# # print(person['yob'])

# person['gender'] = 'Male' #Create
# person['adress'] = 'Đà Lạt' #Update

# del person['yob']
# # print(person['job']) => lỗi
# print('job' in person) #trả kq kiểu boolean -> False
# if 'name' in person:
#     print(person['name'])
# #READ ALL
# # truyen = {
# #     'ten': 'Bộ quần áo mới của Hoàng đế',
# #     'tacGia': 'Hans Christopher Andersen',
# #     'theLoai': 'truyện cổ tích'
# # }
# # print(truyen['theLoai'])
# # key = 'name' / key = input()
# # print(person[key])
# for key, value in person.items(): #tắt: k,v
#     print(key, value)
run = True
teencode = {
    'vk': 'vợ',
    'ck': 'chồng',
    'ny': 'người yêu'
}
while run: #== True => thừa #Lỗi: sau khi bổ sung nghĩa hệ thống không cập nhật -> Sai vị trí đặt while -> gán lại teencode
    lookup = input('Nhập từ bạn teencode cần tra (gõ "thoát" để dừng chương trình): ')
    if lookup == 'thoát':
        break
    if lookup in teencode:
        print(teencode[lookup])
    else:
        add = int(input(f'Hệ thống của chúng tôi hiện chưa cập nhật. Bạn có muốn bổ sung nghĩa cho {lookup} không?\nCó = 1, Không = 0: '))
        if add == 1:
            teencode[lookup] = input(f'Nghĩa của {lookup} là: ')
            print(f'Hệ thống đã cập nhật "{lookup}" với nghĩa "{teencode[lookup]}"')
            print(teencode)
        else:
            run = True
            
