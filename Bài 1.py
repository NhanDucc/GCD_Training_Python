import math

def tim_snt(n):
    if n <= 1:
        return False
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def nhap_phan_tu(mang, x, y):
    if y < 0 or y > len(mang):
        print('Vị trí cần thêm không hợp lệ')
        return None
    else:
        return mang[:y] + [x] + mang[y:]
# Câu a
n = int(input('Nhập số phần tử của danh sách: '))
mang = []
for i in range (n):
    mang.append(int(input(f'Nhập phần tử thứ {i} của danh sách: ')))
print()

# Câu b
mang_snt = []
for i in mang:
    if tim_snt(i):
        mang_snt.append(i)
print(f'Danh sách số nguyên tố của danh sách trên là: {mang_snt}')
for i in mang_snt:
    tong_snt = sum(mang_snt)
print(f'Tổng các số nguyên tố có trong danh sách là: {tong_snt}')
print()

# Câu c
k = int(input("Nhập số K: "))
while k not in mang:
    print(f'Không tìm thấy phần tử có giá trị bằng K trong danh sách.')
    k = int(input("Vui lòng nhập lại số K: "))
thu_tu = mang.index(k)
print(f'Thứ tự của phần tử có giá trị K trong danh sách là: {thu_tu}')
print()

# Câu d  
x = int(input('Nhập số cần thêm vào danh sách: '))
y = int(input('Vị trí cần thêm vào mảng: '))
mang_moi = nhap_phan_tu(mang, x, y)
print(f'Danh sách sau khi thêm phần tử {x} vào vị trí {y} là: {mang_moi}')