size = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hiep and these are my sheep's sizes\n",size)
print("\n")

print(f"Now my biggest sheep has size {max(size)}. Let's shear it")
size.insert(size.index(max(size)),8)
size.remove(max(size))
print(f"After shearing, here is my flock\n",size)
i = 1
while i in range(1,4):
    print(f"MONTH {i}")
    size = list(map(lambda x: x + 50, size))
    print("One month has passed, now here is my flock\n",size)
    if i == 3:
        break
    print(f"Now my biggest sheep has size {max(size)}. Let's shear it")
    size.insert(size.index(max(size)),8)
    size.remove(max(size))
    print(f"After shearing, here is my flock\n",size)
    print(end="\n")
    i += 1

print(f"\nMy flock has size in total: {sum(size)}\nI would get {sum(size)} * 2$ = {sum(size)*2}$")

    