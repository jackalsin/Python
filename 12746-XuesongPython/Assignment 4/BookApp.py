from BookClass import Book


def main():
    aCupOfJava = Book(1001, "A cup of Java", "Kumar", 44.14, 31)
    javaForDummy = Book(1002, "Java for dummies", "Tan Ah Teck", 34.12, 10)
    javaTutorial = Book(1003, "Java tutorial", "Pine Liu", 129.31, 100)

    printBookInfo(aCupOfJava)
    printBookInfo(javaForDummy)
    printBookInfo(javaTutorial)


def printBookInfo(book):
    info = "The book with title %s is written by %s" % (book.title, book.author)
    print info

if __name__ == '__main__':
    main()
