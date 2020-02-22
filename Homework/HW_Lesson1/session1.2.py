print("Nhập độ dài 3 cạnh của tam giác: ")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
p = 1/2*(a+b+c)
S = (p*(p-a)*(p-b)*(p-c))**0.5
print("Diện tích tam giác là: ",S)