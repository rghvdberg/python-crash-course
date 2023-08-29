def favorite_book(book: str):
    print(f"One of my favorite books is {book.title()}.")


book = input("Enter the name of a book: ")

favorite_book(str(book))
