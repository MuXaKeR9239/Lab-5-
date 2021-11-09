class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

class Library:
    books = []
    def addBook(self, book):
        self.books.append(book)
    
    def removeBook(self, book):
        self.books.remove(book)

    def searchByAuthor(self, author):
        books = []
        for book in self.books:
            if book.author == author:
                books.append(book)
        return books
    
    def searchByYear(self, year):
        books = []
        for book in self.books:
            if book.year == year:
                books.append(book)
        return books

    def searchByGenre(self, genre):
        books = []
        for book in self.books:
            if book.genre == genre:
                books.append(book)
        return books

def main():
    library = Library()

    library.addBook(Book('Анджей Сапковський', 'Відьмак', '1990', 'Роман'))
    library.addBook(Book('Дмитро Глуховський', 'Метро 2033', '2005', 'Роман'))
    library.addBook(Book('Стівен Кінг', 'Сяйво', '1977', 'Роман'))

    author = 'Анджей Сапковський'
    books = library.searchByAuthor (author)
    if len(books) == 0:
        return
    book = books[0]

    print('Кількість книг автора'+ author, len(books))
    print('Автор книги', author)
    print('Титульна сторінка книги' , book.title)

    library.removeBook(book)
    books = library.searchByAuthor(author)
    print('Нова кількість книг автора' + author, len(books))

if __name__ == '__main__':
    main()    