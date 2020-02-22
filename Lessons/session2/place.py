# List/ array/ mảng ['value', 'value',...] đằng sau: index 0, 1 -> List có 3 phần tử
# 4 thao tác với List: Create, Read, Update, Delete

places = ['Đại sứ quán','Bệnh viện', 'Bãi biển'] #Initialize

print(places) #Read

new_place = input('enter new place plzzz')
places.append(new_place) #Create
replace_index = places.index('Bệnh viện')
places[replace_index] = 'Tiểu sứ quán' #Update
places.pop() #Delete by index pop() xóa phần tử cuối cùng
places.remove('Đại sứ quán') #Delete by value
temp = places[0]
places[0] = places[1]
places[1] = temp
for i in range(len(places)):
    print(places[i])

