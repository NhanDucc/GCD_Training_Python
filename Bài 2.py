mang_1 = []
mang_2 = []
for i in range (5):
    mang_1.append(int(input(f'Nhập phần tử thứ {i} của danh sách 1: ')))
print()
for i in range (5):
    mang_2.append(int(input(f'Nhập phần tử thứ {i} của danh sách 2: ')))
print()

# Câu a
mang_giong = list(set(mang_1) & set(mang_2))
print(f'Danh sách các phần tử giống nhau là: {mang_giong}')
print(f'Tổng các số giống nhau trong 2 danh sách trên là: {sum(mang_giong)}')
print()

# Câu b
mang_khac = list(set(mang_1) ^ set(mang_2))
print(f'Danh sách các phần tử khác nhau là: {mang_khac}')
print(f'Tổng các số khác nhau trong 2 danh sách trên là: {sum(mang_khac)}')
print()

# Câu c
k = int(input('Nhập số K: '))
while k not in mang_giong:
    print('Số K không phải là số trùng lặp trong 2 danh sách trên')
    k = int(input('Nhập lại số K: '))
print('Số K là số trùng lặp trong 2 danh sách trên')