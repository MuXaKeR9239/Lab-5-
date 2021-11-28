class MyLibrary:
    def __init__(self):
        self.books = []
    def add_book(self, author, title, year, genre):
        self.books.append((author, title, year, genre))
    def remove_book(self, book):
        self.books.remove(book)
    def search_author(self, author):
        books = []
        for book in self.books:
            if book[0] == author:
                books.append(book)
        return books
    def search_year(self, year):
        books = []
        for book in self.books:
            if book[2] == year:
                books.append(book)
        return books
    def search_genre(self, genre):
        books = []
        for book in self.books:
            if book[3] == genre:
                books.append(book)
        return books

lib = MyLibrary()
lib.add_book(
    "Анджей Сапковський",
    "Відьмак",
    "1990",
    "Роман"
)
lib.add_book(
    "Дмитро Глуховський",
    "Метро 2033",
    "2005",
    "Роман"
)
lib.add_book(
    "Стівен Кінг",
    "Сяйво",
    "1977",
    "Роман"
)

books = lib.search_author("Анджей Сапковський")
book = books[0]

print("Кількість книг автора " + book[0] + ": ", len(books))
print("Автор книги", book[0])
print("Титульна сторінка книги" , book[1])

lib.remove_book(book)
books = lib.search_author(book[0])
print("Нова кількість книг автора " + book[0] + ": ", len(books))
