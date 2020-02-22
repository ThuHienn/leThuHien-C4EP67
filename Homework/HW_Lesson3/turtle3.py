# from turtle import *
# colors = ['red', 'blue', 'brown', 'yellow', 'grey']
# x = 3
# for i in range(5):
#     color(colors[i])
#     for j in range(x):
#         forward(100)
#         lt(360/x)
#     x += 1
# mainloop()

from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(5):
    begin_fill()
    color(colors[i])
    for j in range (4):
        if j % 2 == 0:
            forward(50)
        else:
            forward(100)
        lt(90)
    end_fill()
    forward(50)    

mainloop()


