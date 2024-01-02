n = int(input("Nhap so phan tu cua mang: "))
# co mot mang truoc va chuyen mang thanh mang full 0

mang = [0] * n
for i in range(len(mang)-1):
   print(mang[i],end=', ')
print(mang[len(mang)-1])
