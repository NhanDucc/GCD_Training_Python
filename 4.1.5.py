import math

n = int(input("Nhap so dau tien: "))
m = int(input("Nhap so cuoi cung: "))

snt = []
for i in range (n, m+1):
    if i < 2:
        d = 0
    else:
        d = 1
    for j in range (2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            d = 0 
            break
    if d == 1:
        snt.append(i)
print("Cac phan tu so nguyen to cua mang la: ", end="")
for i in range(len(snt)-1):
   print(snt[i],end=', ')
print(snt[len(snt)-1])