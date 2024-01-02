import math
a = int(input("Nhap do dai canh a: "))
b = int(input("Nhap do dai canh b: "))
c = int(input("Nhap do dai canh c: "))
if (a+b>c) and (a+c>b) and (b+c>a):
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"Chu vi cua tam giac la: {2*p}")
    print(f"Dien tich cua tam giac la: {s}")
else:
    print("Day khong phai do dai ba canh tam giac")