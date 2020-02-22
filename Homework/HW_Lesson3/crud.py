items = ["T-shirt", "Sweater"]
welcome = True
while welcome == True:
    ans = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    if ans.upper() == "R":
        print("Our items:", ", ".join(items))
        welcome == False
    elif ans.upper() == "C":
        items.append(input("Enter new item: "))
        print("Our items:", ", ".join(items))
        welcome == False
    elif ans.upper() == "U":
        u = int(input("Update position? "))
        newItem = input("New item? ")
        items.insert(u, newItem)
        print("Our items:", ", ".join(items))
        welcome == False
    elif ans.upper() == "D":
        popit = True
        while popit == True:
            d = int(input("Delete position? "))
            if d <= (len(items)-1):
                items.pop(d)
                print("Our items:", ", ".join(items))
                popit = False
            else:
                print(f"Position must be from 0 to {len(items)-1}")
            welcome == False
    else:
        if ans == "stop":
            break
        welcome = True   
        
