library = {
    "name": "CodeClan Library",
    "books": [
        {
            "author": "George RR Martin",
            "title": "A Song of Ice and Fire"
        },
        {
            "author": "J R. R. Tolkien",
            "title": "The Hobbit"
        },
        {
            "author": "Paul Barry",
            "title": "Head-First Python"
        },
        {
            "author": "Allen B. Downey",
            "title": "Think Python: How to Think Like a Computer Scientist"
        },
        {
            "author": "Eric Matthes",
            "title": "Python Crash Course"
        }
    ]
}

# TODO - Print welcome statement incuding library name

print("WELCOME TO THE CODECLAN LIBRARY")

option = ""
while option != "q":
    print("Options:")
    print("1 - List all books")
    print("2 - Search for a book by title")
    print("3 - Add a book")
    print("4 - Remove a book")
    print("5 - Update a book")
    print("q - Quit")
    option = input("What would you like to do? \n") # what is \n ?

    if option == "1":
        print("Listing all books...")
        for book in library["books"]:
            print(book["author"])
            print(book["title"] )
            print("")
        # TODO - List all books 

    if option == "2":
        print("Searching for a book by title...")
        # user input
        search = input("Search a title: \n")
        # TODO - Search for a book by title
        book_found = None
        for book in library["books"]:
            if search == book["title"]:
                # print("book found")
                book_found = book
            #print(book_found)    
        if book_found == None:
            print("book not found")
        else:
            print(f"{book_found['title']} by {book_found['author']}")
        
    if option == "3":
        # TODO - Add a book
        # make it user choice
        print("Adding a book...")
        title = input("Add a title: \n")
        author = input("Add an author: \n")
        library["books"].append({
            "title": title,
            "author": author
        })
        print(f"{title} by {author} added to the library.")
        # print(library)
        

    if option == "4":
        # user input :
        # title 
        # author of the book
        # search (loop) 
        # find the user chosen book
        # remove chosen book
        # update list
        print("Remove a book...")
        title = input("Choose the book title you want to take out: \n")
        # TODO - Search for a book by title
        book_found = None
        for book in library["books"]:
            if title == book["title"]:
                # print("book found")
                book_found = book
            #print(book_found)
        if book_found == None:
            print("book not found")
        else:
            print(f"{book_found['title']} by {book_found['author']} was removed.")
            library["books"].remove(book_found)
        # TODO - Remove a book
        # similar like step 2


        # this the extension part have a go !optional!
    if option == "5":
        print("Updating a book...")
        # TODO - Update a book

