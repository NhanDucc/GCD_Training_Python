n = int(input("Nhap so phan tu: "))
ds = []
for i in range (n):
    ds.append(int(input(f"Nhap phan tu thu {i}: ")))  
    # append: nhap vao tu dau 
    
so_duong = 0
tong_so_duong = 0
tong = 0

for t in ds:
    if t > 0:
        so_duong += 1
        tong_so_duong += t
    tong += t
    tbc = round(tong / n)
    # co the dung ham sum(ds) / n de tinh tbc

max = max(ds)
# dsa =[]
# dsa = ds - dsa max ??????? -> ham remove -> ds.remove(max)
# print(dsa)
# max = ds[0]
# for k in sa:
#     if k > max:
#         max = k
       
max_2 = ds[0]
for k in ds:
    if k > max_2 and k != max:
        max_2 = k

print()
print("Cau a:")    
print(f"So hang duong trong danh sach la: {so_duong}")
print(f"Tong cac so hang duong trong danh sach: {tong_so_duong}")
print()

print("Cau b:")    
print(f"Trung binh cong cua ca danh sach: {tbc}")
print()

print("Cau c:")    
x = int(input("Nhap so can tim: "))   
for i in ds:
    if x == i:
        d = 1
    else:
        d = 0
if d == 1:
    print(f"Vi tri cua {x} la: {ds.index(x)}")
else:
    print(f"Khong ton tai {x} trong mang")
print()

print("Cau d:")    
print(f"Phan tu lon thu hai cua danh sach la: {max_2}")
print()
