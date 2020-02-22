from turtle import *
shape("turtle")
color("red")
lt(60)
for i in range(4):
    rt(30)
    forward(200)
    rt(60)
    forward(200)
    rt(120)
    forward(200)
    rt(60)
    forward(200)
mainloop()

# j=0
# X=3
# for z in range(4):
#     if j % 2 == 0:
#         color("blue")
#         for i in range(X):
#             fd(100)
#             lt(360/X)
#         j+=1
#         X+=1
#     else:
#         color("red")
#         for i in range(X):
#             fd(100)
#             lt(360/X)
#         j+=1
#         X+=1
# mainloop()