def place_on_shelf(shelf, amount):
    for book in range(amount):
        name_book = input("Название книги "+str(book+1)+":").strip()
        author = input("Автор книги: ").strip()
        book_format = {
            "Name": name_book,
            "Author": author
        }
        shelf_format = f"Shelf_{shelf} : {book_format}"

        with open("Library.txt", "a") as library:
            library.write(shelf_format+"\n")
    return f"{amount} книги добавлены на полку {shelf}."


def read_file_library():
    with open("Library.txt", "r") as library:
        return library.read()


def main():
    shelf_number = input("На какую полку записать книгу: ").strip()
    books = int(input("Сколько книг нужно поставить: "))
    print(place_on_shelf(shelf_number, books))
    print(read_file_library())


if __name__ == "__main__":
    main()
