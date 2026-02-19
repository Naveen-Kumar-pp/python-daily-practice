def add_book():
    book = input("Book name: ")
    with open("library.txt", "a") as f:
        f.write(book + "\n")

def view_books():
    with open("library.txt", "r") as f:
        print(f.read())

add_book()
view_books()
