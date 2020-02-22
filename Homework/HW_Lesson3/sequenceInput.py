mylist = list(filter(str.isdigit, input("Enter a list of numbers, separated by ',': ")))
newList = []
for i in range(len(mylist)):
    newList.append(int(mylist[i]))
evenNumber = filter(lambda x: x % 2 == 0, newList)
print("All even numbers:", ", ".join(map(str,evenNumber)))