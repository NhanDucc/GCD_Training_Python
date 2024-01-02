file_path = "F:\\Number.txt"

# Đọc file và tính tổng dãy số
with open(file_path, "r") as file:
    lines = file.readlines()
    numbers = [int(line.strip()) for line in lines]
print("The data contained in the file:")
for i in numbers:
    print(i)
print(f"Sum of the number: {sum(numbers)}")

# Nhập vào số bất kỳ in ra số dòng trong file nếu k thấy trả về None
n = int(input("Enter a number to search: "))
number_line = None
for index, number in enumerate(numbers, start=1):
    if number == n:
        number_line = index
if number_line is not None:
    print(f"The number {n} is found at line {number_line}")
else: 
    print(f"Number {n} not found!")

# Ghi đè dãy số tương ứng với 1 số K nhập vào bàn phím. Ví dụ : k = 3 Giá trị đè bằng số cuối + 1 đến số cuôí + k
k = int(input("Enter number K: "))
last_num = numbers[-1]
new_numbers = list(range(last_num + 1, last_num + k + 1))
with open(file_path, "a") as file:
    for number in new_numbers:
        file.write("\n" + str(number))
with open(file_path, "r") as file:
    lines = file.readlines()
    numbers = [int(line.strip()) for line in lines]
print("New overwritten numbers:")
for i in numbers:
    print(i)