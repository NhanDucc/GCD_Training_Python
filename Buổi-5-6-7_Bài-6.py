# a
def input_book_info():
    book_id = int(input("Enter book ID: "))
    book_name = input("Enter book name: ")
    author = input("Enter author name: ")
    quantity = int(input("Enter quantity: "))
    return {'book_id': book_id, 'book_name': book_name, 'author': author, 'quantity': quantity}

def print_book_infor(book):
    print(f"Book ID: {book['book_id']}")
    print(f"Book Name: {book['book_name']}")
    print(f"Author: {book['author']}")
    print(f"Quantity: {book['quantity']}")

# b
def find_book_by_name(library, book_name):
    book_found_by_name = []
    for book in library:
        if book['book_name'] == book_name:
            book_found_by_name.append(book)
    return book_found_by_name

# c
def count_total(library):
    total = 0
    for book in library:
        total += book['quantity']
    return total   

# d
def find_book_by_author(library, author):
    book_found_by_author = []
    for book in library:
        if book['author'] == author:
            book_found_by_author.append(book)
    return book_found_by_author


# a
library = []
print("Enter the information for 10 books: ")
for i in range (10):
    print(f"Enter the information for book {i+1}: ")
    book_infor = input_book_info()
    library.append(book_infor)
    if i == 9:
        print("Maximun number of books. Cannot add more!")
        break
print()

# b
print("Enter name of the book you are looking for: ")
book_to_find_by_name = input()
book_find_by_name = find_book_by_name(library, book_to_find_by_name)
if book_find_by_name:
    print("Book information found: ")
    for book in book_find_by_name:
        print_book_infor(book)
        print()
else:
    print("Book not found")
print()

# c
total_book = count_total(library)
print(f"Total number of books in the libraly: {total_book}")
print()

# d
print("Enter name of author you are looking for: ")
book_to_find_by_author = input()
book_find_by_author = find_book_by_author(library, book_to_find_by_author)
if book_find_by_author:
    print(f"Book by author: {book_to_find_by_author}")
    for book in book_find_by_author:
        print_book_infor(book)
        print()
else:
    print(f"No book found by author {book_to_find_by_author}")
