#Review
    # - Because help us organize programs into chunks that match how we think about the problem.
    # - def NAME( PARAMETERS ):
    #       STATEMENTS
    # - To call a function, use the function name followed by parenthesis
    # - A function that returns a value is called a fruitful function which returns a value after the implementation of the function.
    # The return function is used when we pass user defined function and its statement is followed an expression.
    # - Inside the function, the values that are passed get assigned to variables called parameters.
    # We use them because most functions require arguments: the arguments provide for generalization. 
    # - From FILE import FUNCTION
# Turtle exercise
#1.
# def hello():
#     for i in range(3):
#         print("Hello world")
# hello()

# #2.
# def sum2(a,b):
#     print(a+b)
# sum2(1,2)

#3.
# def draw_square(length,square_color):
#     from turtle import fd,lt,color
#     color(square_color)
#     for x in range (4):
#         fd(length)
#         lt(90)
    
# #4.
# from turtle import *
# for i in range(30):
#     draw_square(i * 5, 'red')
#     left(17)
#     penup()
#     forward(i * 2)
#     pendown()
# mainloop()

#5.
# def draw_star(x,y,length):
#     from turtle import goto,fd,rt,pu,pd
#     pu()
#     goto(x,y)
#     pd()
#     for i in range(5):
#         fd(length)
#         rt(144)
    
#6
# from turtle import *
# speed(0)
# color('blue')
# for i in range(100):
#     import random
#     x = random.randint(-300, 300)
#     y = random.randint(-300, 300)
#     length = random.randint(3, 10)
#     draw_star(x, y, length)
# mainloop()

# #7
# def remove_dollar_sign(s):
#     return s.replace("$","")

# #8    
# string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
# if string_with_no_dollars == "80% percent of life is to show up":
#     print("Your function is correct")
# else:
#     print("Oops, there's a bug")

# #9
# def get_even_list(l):
#     for number in l:
#         if number % 2 != 0:
#             l.remove(number)
#     return l

# #10
# even_list = get_even_list([1,2,5,-10,9,6])
# if set(even_list) == set([2,-10,6]):
#     print("Your function is correct")
# else:
#     print("Ooops, bugs detected")

#11
# def is_inside(x_point,y_point,x_rec,y_rec,width,height):
#     if x_point > x_rec and x_point < (x_rec + width):
#         if y_point > y_rec and y_point < (y_rec + height):
#             return True
#         else:
#             return False
#     else:
#         return False

# a = is_inside(100,120,140,60,100,200)
# b = is_inside(200,120,140,60,100,200)
# print(a)

# # #12
# if a == False:
#     print('Your function is correct')
# else:
#     print("Oops, bugs detected")       
