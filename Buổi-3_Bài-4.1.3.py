mang = []
n = int(input("Nhap so phan tu nguyen am cua mang: "))
for i in range (-n, 0):
    mang.append(i)
print()
print("Cac phan tu cua mang la: ", end="")
for i in range(len(mang)-1):
   print(mang[i],end=', ')
print(mang[len(mang)-1])
