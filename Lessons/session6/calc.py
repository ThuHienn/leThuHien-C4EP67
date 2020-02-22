#Đóng vai máy tính
# a = int(input('nhap so a'))
# operator = input('nhap phep tinh')
# b = int(input('nhap so b'))

def calc(a,b,operator):
    if operator == '+':
        # print(a+b) -> chỉ hiện ra màn hình mà không giải quyết các vấn đề logic
        # và không phải lúc nào cũng muốn chỉ in lên console (in lên web v.v.) 
        # => cho hàm làm một việc thôi/có một chức năng
        result = a + b #Cách 2: return a + b
    elif operator == '-':
        # print(a-b)
        result = a - b 
    elif operator == '*':
        # print(a*b)
        result = a * b
    elif operator == '/': #and b != 0:
        # print(a/b)
        result = a / b
    # else:
    #     print('m đùa t à')
    return result #nên để dưới cùng vì code sau return không chạy
# print(__name__) #chạy in ra "main" vì chạy từ file gốc
if __name__ == '__main__':
    a = calc(4,5,'+')
    print(a)
#function - hàm: chương trình con chạy bên trong 1 chương trình
# def plus(a,b):
#     plus_solution = a + b
#     return plus_solution
# def minus(a,b):
#     minus_solution = a - b
#     return minus_solution
# def multi(a,b):
# => DÀIIIIII


