# Tạo một danh sách các đối tượng mặt hàng với thông tin tương ứng
products = [
    {"id": 1, "name": "Laptop", "price": 1000, "quantity": 5},
    {"id": 2, "name": "Monitor", "price": 600, "quantity": 10},
    {"id": 3, "name": "Keyboard", "price": 400, "quantity": 8},
    {"id": 4, "name": "Webcam", "price": 300, "quantity": 12},
    {"id": 5, "name": "Speaker", "price": 200, "quantity": 15}
]

# Tính tổng giá trị của toàn bộ kho hàng
total_value = 0
for product in products:
    total_value += product["price"] * product["quantity"]
print("Total value of the inventory:", total_value)

# In ra thông tin của các mặt hàng có giá trị lớn nhất và nhỏ nhất
def calculate_value(product):
    return product["price"] * product["quantity"]

max_value_product = max(products, key=calculate_value)
min_value_product = min(products, key=calculate_value)

print("Product with the highest value:")
print("ID:", max_value_product["id"])
print("Name:", max_value_product["name"])
print("Total Value:", max_value_product["price"] * max_value_product["quantity"])

print("Product with the lowest value:")
print("ID:", min_value_product["id"])
print("Name:", min_value_product["name"])
print("Total Value:", min_value_product["price"] * min_value_product["quantity"])

