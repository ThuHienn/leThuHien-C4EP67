# a.ii.
# list = []
# for i in range (21):
#     list.append(i)
#     print(list[i], end=" ") #Chưa tối ưu
# Cách khác:
# n = int(input("Enter a number: "))
# # for i in range (n):
# #     print(i, end=" ")

#b.i.
# n = int(input("Enter the total number of 1's and 0's: "))
# for i in range (n):
#     if i % 2 == 0:
#         print('1 ', end=" ")
#     else:
#         print('0 ', end=" ")

#c.i.
# list = []
# # for i in range(9):
# #     list.append(i+1)
# #     for j in range(1,10):
# #         print(j*list[i], end="\t")
# #     print(end="\n")

#c.ii.
# n = int(input("Enter a number: "))
# list = []
# for i in range(n):
#     list.append(i+1)
#     for j in range(1,n+1):
#         print(j*list[i], end="\t")
#     print(end="\n")

#d.ii.
n = int(input("Enter a number: "))
for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            if j % 2 == 0:
                print("1", end=" ")
            else:
                print("0", end=" ") 
        print(end="\n")
    else:
        for j in range(n):
            if j % 2 == 0:
                print("0", end=" ")
            else:
                print("1", end=" ") 
        print(end="\n")