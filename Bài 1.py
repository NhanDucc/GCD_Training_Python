import math

integer = []

# Nhập vào một danh sách gồm N số nguyên từ người dùng.
n = int(input("Enter the number of integers: "))
for i in range (1, n+1):
    integer.append(int(input(f"Enter the integer {i}: ")))

# Sắp xếp danh sách theo thứ tự giảm dần
sorted_integer = sorted(integer, reverse=True)
print(f"List of integers after sorted in descending order: {sorted_integer}")

# Tìm và in ra các số nguyên tố trong danh sách
prime_list = []
for i in integer:
    if i < 2:
        d = 0
    else:
        d = 1
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            d = 0
            break
    if d == 1:
        prime_list.append(i)
print(f"The prime number(s) in the list: {prime_list}")

# Tạo một danh sách mới chứa các số là bội của 3 từ danh sách ban đầu và in danh sách mới
multi_3 = []
for i in integer:
    if i % 3 == 0:
        multi_3.append(i)
print(f"Numbers that are multiples of 3 in the list: {multi_3}")