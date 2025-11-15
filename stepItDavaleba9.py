books = {
    "Paulo Coelho": ["Eleven Minutes", "The Alchemist"],
    "Dato Turashvili": ["Jeans' Generation"],
    "Steve Watson": ["Before I Go to Sleep"]
}

# 1
def addBook():
    BookAuthor = input("Input the name of the author you'd like to add: ")

    # თუ ავტორი უკვე არსებობს პროგრამა საშუალებას გვაძლევს რომ წიგნები ჩავუმატოთ.
    if BookAuthor in books:
        print(f"{BookAuthor} is already added in the dictionary.")
        addBookToExistingAuthor = input("Please enter the book you'd like to add for this auhtor: ")
        books[BookAuthor].append(addBookToExistingAuthor)

    # სხვა შემთხვევაში ქმნის ახალ ავტორს.
    else:
        BookName = input(f"Input the name of the book (Author {BookAuthor}) you'd like to add: ")
        books.update({BookAuthor: [BookName]})

# 2
def searchBookByAuthorName():
    authorName = input("Input the author you are trying to find: ")

    # ეძებს ავტორს და მის შესაფერის valueებს, წიგნებს.
    for bookKey, bookValue in books.items():
        if authorName.lower() == bookKey.lower():

            # თუ ავტორს 2ზე მეტი წიგნი აქვს იშვება  ქვემოთმოცემული
            if isinstance(bookValue, list):
                # აქ ყველა value ერთაინდება ერთ ცვლადად.
                bookList = ", ".join(bookValue)
                return f"{authorName} wrote the books called: {bookList}"
            
            # თუ ავტორს აქვს მხოლოდ 1 წიგნი მაშინ ეს დაიბეჭდება.
            else:
                return f"{bookKey} wrote the book called {bookValue}"
    # თუ ავტორი არ არსებობს მაშინ ეს დაიბეჭდება.
    return f"No books found under the name {authorName}"

# 3
def searchBookByBookName():
    bookName = input("Input the name of the book of the author you are trying to find: ")
    # აქ ზოგადად მოწმდება არის თუ არა წიგნი და თუ არის ვინ დაწერა.

    for bookKey, bookValue in books.items():
        if isinstance(bookValue, list):
            for eachbook in bookValue:
                if bookName.lower() in eachbook.lower():
                    return f"{eachbook} was written by {bookKey}"
                
    # თუ წიგნი არ არსებობს მაშინ ეს დაიბეჭდება.
    return f"No book called {bookName} was found in the dictionary"

while True:
    optionHelper = ""
    # option ცვლადი წყვეტს რა მოქმედება მოხდება.
    option = input("Please choose your next action. To see instructions, input 0: ")

    # სიტყვას აშორებს spaceებს
    for i in list(option):
        if i == " ":
            continue
        else:
            optionHelper = optionHelper + i

    # თუ option არის "quit", პროგრამა წყდება.
    if optionHelper.lower() == "quit":
        print("Ending program.")
        break

    # თუ დაპრინტვა უნდა იუზერს, მოწმდება წიგნები და ავტორები
    elif optionHelper.lower() == "print":
        for authorName, book in books.items():
            # ამოწმებს ლისთია თუ არა, რადგან 1ზე მეტი წიგნის ქონისას ლისთ ტიპის ხდება value
            if isinstance(book, list):
                for title in book:
                    print(f"{authorName} wrote the book: {title}")
            else:
                print(f"{authorName} wrote the book: {book}")
        continue
    
    # სანამ გაიშვება პროგრამა რომელიც რიცხვებით ამოწმებს, ნახულობს საერთოდ რიცხვად გადაყვანა შეიძლება თუ არა 
    try:
        option = int(option)
    except ValueError:
        print("Please chose a correct format/number.")
        continue

    # 0ზე გამოაქვს სანავიგაციო 'სისტემა'.
    if int(option) == 0:
        print("Select option number 1 by typing 1 to add a book.")
        print("Select option number 2 by typing 2 to search a book by it's author name.")
        print("Select option number 3 by typing 3 to search a book by it's name a book.")
        print("Type 'Quit' to the process.")
        print("Type 'Print' to print the book dictionary.")
    
    # 1დან 3ის ჩათვლით იშვება მოქმედებები.
    elif int(option) == 1:
        print("You have chosen to add books. Starting program...")
        addBook()
    elif int(option) == 2:
        print("You have chosen to search book by it's author's name. Starting program...")
        print(searchBookByAuthorName())
    elif int(option) == 3:
        print("You have chosen to search book by it's name. Starting program...")
        print(searchBookByBookName())
    else:
        print("Please chose a correct format/number.")
        continue