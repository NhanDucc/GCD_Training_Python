mang = []
n = int(input("Nhap so phan tu so thuc cua mang: "))
for i in range(n):
    mang.append(int(input(f"Nhap phan tu thu {i}: ")))
print()
print("Cac phan tu cua mang la: ", end="")
for i in range(len(mang)-1):
   print(mang[i],end=', ')
print(mang[len(mang)-1])
