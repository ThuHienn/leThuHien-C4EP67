#Khai báo - init fuction ~ có một cái máy xay sinh tố
def in_ra(content): #"in_ra" là tên hàm, thường là động từ #def: define, parameter/argument: biến, tham số đầu vào
    print(content) 
#Gọi hàm - call function ~ sử dụng máy xay và quyết định nguyên liệu đầu vào tùy ý => kết quả dựa vào/tương ứng với nguyên liệu đầu vào
in_ra('hello')
#Khác với biến: 
# Biến: khai báo và đặt giá trị -> gọi ra -> in ra giá trị
# Hàm: khai báo không biết giá trị -> gọi ra và đặt giá trị -> in ra giá trị

def greeting(name, age):
    print(f'hi, my name is {name}, iam {age} years old')

def add(a, b):
    print(a+b)

greeting('Duc', 100)
greeting('hitler', 999)

# total = add(2,1)
#     print(total) -> in ra None

# def add(a,b):
#     total = a + b

# add(2,1)
# print(total) -> lỗi không tìm thấy total

#variable scope:
#VD: biến khai biến trong chương trình con (def) là đồ vật của chủ nhà, chỉ chủ nhà được dùng ~ chỉ chạy trong chương trình con(trong vùng tab)
#biến khai biến trong chương trình ngoài là đồ công cộng của huyện, ai cũng có thể dùng được ~ gọi và sử dụng được trong cả chương trình con và ngoài
def add(a,b):
    total = a + b
    return total #vứt total ra ngoài chương trình con nhưng phải tạo 1 biến để hứng và giữ lại không sẽ vứt ra và biến mất (~ không in ra được/không tìm thấy)
   #thuộc loại hàm có trả về (fruit_full function), có return, cần gán vào một biến để lấy giá trị/kết quả VD: hàm input = mẹ bảo đi chợ phải mang đồ về cho mẹ
   # khác hàm print = mẹ bảo đi làm bài tập, không đưa kq hành động ngay cho mẹ
a = add(2,1)
    