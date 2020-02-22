from turtle import *
# *: tất cả; speed: chỉ một hàm speed
# mainloop(): giữ nguyên hiện trạng sau khi chạy chương trình (không đóng cửa sổ)
speed(-1)
shape("turtle")
color("blue")
# forward(200)
# rt(90)
# forward(200)
# rt(90)
# forward(200)
# rt(90)
# forward(200)
# rt(90)

for i in range(100):
    for j in range(4):
        forward (200)
        lt(90)
    lt(4)

mainloop()