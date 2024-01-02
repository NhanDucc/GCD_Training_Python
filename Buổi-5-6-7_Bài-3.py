n = int(input('Nhập số phần tử của danh sách: '))
ds_du = []
ds = []

for i in range (1,n+1):
    ds_du.append(i)
nhap_str = input('Nhập danh sách: ')
tach_str = nhap_str.split()
for so_str in tach_str:
    so = int(so_str)
    ds.append(so)
print(f'Danh sách đã nhập là: {ds}')
ds_khuyet = list(set(ds_du) ^ set(ds))

print(f"Các số bị khuyết là: ", end = "")
for i in range(len(ds_khuyet) - 1):
   print(ds_khuyet[i], end = ', ')
print(ds_khuyet[len(ds_khuyet) - 1])
