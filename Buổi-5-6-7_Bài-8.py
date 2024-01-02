import random
file_path = "F:\demo.txt"

# Write random data
with open(file_path, "w") as file:
    for i in range (5):
        random_data = str(random.randint(1,10))
        file.write("\n" + random_data)

# Read contents
with open(file_path, "r") as file:
    content = file.read()
print(f"Random data in the file: {content}")

# Add additional text
additional_text = "This is additional text: Hello world!"
with open(file_path, "a") as file:
    file.write("\n" + additional_text)
with open(file_path, "r") as file:
    content = file.read()
print(f"Update contents: {content}")
