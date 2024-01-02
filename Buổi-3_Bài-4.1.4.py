mang = []
gia_tri_dau = int(input("Nhap so bat dau cua mang: "))
gia_tri_sau = int(input("Nhap so ket thuc cua mang: "))
for i in range (gia_tri_dau, gia_tri_sau +1):
    mang.append(i)
print()
print("Cac phan tu cua mang la: ", end="")
for i in range(len(mang)-1):
   print(mang[i],end=', ')
print(mang[len(mang)-1])
