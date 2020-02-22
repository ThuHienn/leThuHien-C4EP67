# 1.
# even_number = []
# list = [5,1,8,92,7,30]
# for i in range(len(list)):
#     if list[i] % 2 == 1:
#         even_number.append(list[i])
# print("All even number:", ", ".join(map(str,even_number))) #Chưa tối ưu

# Cách 2:
# mylist = [5,1,8,92,7,30]
# result = filter(lambda x: x % 2 == 0, mylist)
# print("All even numbers:", ", ".join(map(str,result)))
