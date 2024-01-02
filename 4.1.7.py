import math

mang = []
n = int(input("Nhap so phan tu cua mang: "))
for i in range(n):
    gia_tri = int(input(f"Nhap phan tu thu {i}: "))
    mang.append(gia_tri)

mang_2 = [] 
k = int(input("Nhap so nguyen K: "))
for i in mang:
    if i < 2:
        d = 0
    else:
        d = 1
    for j in range (2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            d = 0 
            break
    if d == 1 and i < k:
        mang_2.append(i)
        
print(f"Cac phan tu so nguyen to nho hon {k} cua mang la: ", end="")
for i in range(len(mang_2)-1):
   print(mang_2[i],end=', ')
print(mang_2[len(mang_2)-1])