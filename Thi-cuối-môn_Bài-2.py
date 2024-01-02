file_path_1 = "F:\input.txt"
file_path_2 = "F:\output.txt"

# Đọc nội dung của tập tin
with open(file_path_1, "r") as file:
    contents = file.read()
print(f"The content in 'input.txt': {contents}")

# Đếm số lượng từ duy nhất (không tính trùng lặp) xuất hiện trong tập tin
words = contents.split()
unique_words = set(words)
print(f"Number of unique words in the file: {len(unique_words)}")

# Tạo một tập tin mới có tên "output.txt" và ghi lại các từ đã đếm theo thứ tự từ điển
sorted_words = sorted(unique_words)
with open(file_path_2, "w") as file:
    for word in sorted_words:
        file.write(word + "\n")
print("Unique words have been written to 'output.txt'")
with open(file_path_2, "r") as file:
    contents = file.read()
print(f"The content in 'input.txt': {contents}")
