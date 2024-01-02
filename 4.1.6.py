chan = []

n = int(input("Nhap so dau tien: "))
m = int(input("Nhap so cuoi cung: "))

for i in range (n, m + 1):
    if i % 2 == 0 and i < 20:
        chan.append(i)
print("Cac phan tu so chan va nho hown 20 cua mang la: ", end="")
for i in range(len(chan)-1):
   print(chan[i],end=', ')
print(chan[len(chan)-1])     
