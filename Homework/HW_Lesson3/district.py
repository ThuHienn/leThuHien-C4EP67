tenQuan = ['ST', 'BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
danSo = [150300,247100,333300,266800,420900,318000]

# print("Chỉ số của quận có số dân lớn nhất",danSo.index(max(danSo)))
# print("Chỉ số của quận có số dân nhỏ nhất",danSo.index(min(danSo)))

# print(tenQuan[danSo.index(max(danSo))])
# print(tenQuan[danSo.index(min(danSo))])

dienTich = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
matDo = list(map(lambda x, y: x/y, danSo, dienTich))
matDoLamTron = []
for i in range(len(matDo)):
    matDoLamTron.append(round(matDo[i],2))
print(matDoLamTron)
print("Mật độ dân cư trung bình: ", round(sum(matDo)/len(tenQuan),2))