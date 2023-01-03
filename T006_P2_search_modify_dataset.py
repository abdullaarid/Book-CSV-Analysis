#Date: 07/12/2021 Version: 1.0
"""
team identifier: T006
Abdulla Arid (101217955)
Moataz Dabbour (100863820)
Imshaad Naaz (101215412)
Owen Renette (101223576)
"""
# Function 1, written by Abdulla
def print_dictionary_category(category:str,dataset:dict) -> int:
    """
    Returns the number of books in the category and prints all the books in the category
    >>> print_dictionary_category("Traditionale",books)
    The category Traditionale has no books

    >>> print_dictionary_category("Adventure",books)
    The category Traditional has 7 book(s). This is the list of books in the category Traditional:
    title: Sword of Destiny: Witcher 2: Tales of the Witcher
    author: Andrzej Sapkowski
    rating: 4.8
    publisher: Hachette UK
    page_count: 400
    language: English


    title: A Feast for Crows (A Song of Ice and Fire, Book 4)
    author: George R.R. Martin
    rating: 4.5
    publisher: HarperCollins UK
    page_count: 864
    language: English

    5 more books
    """
    BooksList = [] #adds all individual books to a list to count and index through
    for cat in dataset.keys():
        if cat == category: #only adds books from the wanted category
            BooksList += dataset[category]
            print("The category {0} has {1} book(s). This is the list of books in the category {0}:".format(category,len(BooksList)))
    for book in BooksList: #for each book in the list, print keys and values
        print("\n")
        for keys in book:
            print("{0}: {1}".format(keys,book.get(keys)))
    if category not in dataset.keys(): #if the wanted category is not a key in the original dictionary print
        print("The category {0} has no books".format(category))
        return 0
    return len(BooksList) #return the number of books in the category

# Function 2, written by Abdulla
def add_book(dataset:dict, info: tuple) -> dict:
    """
    Returns updated list and prints if wheather the book was added properly or not
    precondition is that rating is positive and less than or equal to 5

    >>> add_book(books,("The Hunger Games","Suzanne Collins","English", "Scholastic Press","Adventure",4.3, 374))
    The book has been added correctly

    >>> add_book(books,("1776","David McCullough","English", "Simon & Schuster","History",4.5, 386))
    There was an error adding the book
    """
    if len(info) == 7: #if the tuple contains all 7 values
        TITLE,AUTHOR,LANGUAGE,PUBLISHER,CATEGORY,RATING,PAGE_COUNT = info #sets these variables to the tuple values
        for cat in dataset.keys():
            if cat == CATEGORY: #if the category is the same
                if RATING== '': #if rating is empty string convert to 'N/A'
                    RATING = 'N/A'
                else: RATING = float(RATING) #else convert to string

                bookInfo = {"title":TITLE, "author":AUTHOR,"rating":RATING, "publisher":PUBLISHER, "page_count":int(PAGE_COUNT), "language":LANGUAGE}
                dataset[cat].append(bookInfo) #append the book info to the category in the dictionary
                print("The book has been added correctly")
                return dataset
        else:
            if RATING== '': #if rating is empty string convert to 'N/A'
                RATING = 'N/A'
            else: RATING = float(RATING) #else convert to string
            bookInfo = {"title":TITLE, "author":AUTHOR,"rating":RATING, "publisher":PUBLISHER, "page_count":int(PAGE_COUNT), "language":LANGUAGE}
            dataset.update({CATEGORY:[bookInfo]})
            print("The book has been added correctly")
            return dataset
    print("There was an error adding the book")
    return dataset
#print(add_book(load_dataset("Google_Books_Dataset.csv"),("The Hunger Games","Suzanne Collins","English", "Scholastic Press","new",4.3, 374)))
# Function 3, written by Abdulla
def remove_book(bookTitle:str,bookCategory:str,dataset:dict) -> dict:
    """
    Returns the updated dictionary and prints wheather the book was removed properly
    or if there was an error

    >>> remove_book("The Red Signal: An Agatha Christie Short Story","Traditional",books)
    The book has been removed correctly

    >>> remove_book("1776","History",books)
    There was an error removing the book
    """
    for cat in dataset.keys(): #searches for the category
        if cat == bookCategory:
            for book in dataset[bookCategory]: #look through each book in the dictionary categories
                if book.get("title") == bookTitle: #if the title of the current book is equal to the requested title
                        book.clear() #clear the keys and values in that book dataset
                if len(book) == 0: #if the length of the book dictionary is 0
                    dataset[bookCategory].pop(dataset[bookCategory].index(book)) #remove that dict from the category list
                    print("The book has been removed correctly")
                    return dataset
    print("There was an error removing the book")
    return dataset

# Function 4, written by Owen
def get_books_by_rate(rate: int, dataset: dict) -> dict:
    """ Returns a dictonary with the key being the rate and the value being a
    list of dictonarys of book info with the corresponding rating when given
    the rate and the dataset that is being analyzed.
    Precondition: rate must be a positive integer
    >>> books = load_dataset('Google_Books_Dataset.csv')
    >>> rate_dict = get_books_by_rate(3, books)
    Title: How to Understand Business Finance: Edition 2
    Author: Bob Cinnamon
    Rating: 3.5
    Publisher: Kogan Page Publishers
    Page count: 176
    Language: English
    Generes: Business
    -----------------
    ...
    -----------------
    >>> rate_dict
    {'Books with Rate of 3': [{'title': 'How to Understand Business Finance:
    Edition 2', 'author': 'Bob Cinnamon', 'rating': 3.5, 'publisher': 'Kogan
    Page Publishers', 'page_count': 176, 'language': 'English', 'generes':
    'Business'}, {...}, ..., ]}
    """
    #With Rate as key, and book dictonaries of book info in a list as the value
    rate_to_books_dict = {}
    book_by_rate_list = []
    data = dataset

    for book_genere in data: #For each book genere dictionary in the dictionary of book information
        for book in data[book_genere]: #For each book in the respective genere
            if book['rating'] != 'N/A' and book['rating'] >= rate and book['rating'] < rate + 1: #If Rating for the book is avalible and within the input rate
                for catagory in book: #Prints out the Book information
                    print(catagory.capitalize().replace('_', ' '), ': ', book[catagory], sep='') #Prints 'Catagory':(book's info corresponding to that catagory)'
                print('Genere: ', book_genere, sep='') #Prints the Genere
                print('-----------------') #Visually seperates the book info from each book
                book_by_rate_list += [book] #Adds book info to the list of books for the genere
        if len(book_by_rate_list) != 0:
            rate_to_books_dict[book_genere] = book_by_rate_list #Adds dictonary of book data to list of book data for that genere
        #if len(book_by_rate_list) != 0: #If books existed for that Genere
        book_by_rate_list = [] #Resets the list before continuing to the next genere
    if len(rate_to_books_dict) == 0:
        print('There are no books of rate {0}'.format(rate))

# Function 5, written by Imshaad
def find_books_by_title(title: str, dataset: dict) -> bool:
    """
    Returns a boolean variable depending on whether the book's title exists in the
    dataset dictionary.
    Additonally prints whether the book has been found or not.

    >>>find_books_by_title('After Anna', books)
    The book has been found
    True
    >>>find_books_by_title('Thanks For The Memories', books)
    The book has NOT been found
    False

    """
    book_list = []#An empty list which will store all the books in dataset.
    title_list = [] #An empty list which will store the titles of all books in dataset.

    for category in dataset: #Iterates through each category.
        book_list += dataset.get(category) #Adds the books from dataset to book_list.

    for book in book_list: #Iterates through each book in book_list.
        book_title = book['title'] #Stores the book title of the current iteration in book_title.
        title_list.append(book_title) #Adds each book title to title_list.

    if title in title_list: #Checks if title is in title_list.
        print("The book has been found")
        return True
    else:
        print("The book has NOT been found")
        return False

# Function 6, written by Owen
def get_books_by_author(author_name: str, dataset: dict) -> list:
    """ Returns a list of the book titles for books that the author wrote when
    given the author_name and the dataset being analyzed.
    Precondition: Authors name must be typed in the correct casing
    >>> books = load_dataset('Google_Books_Dataset.csv')
    >>> author_books = get_books_by_author("Agatha Christie", books)
    1- The Mysterious Affair at Styles
    2- And Then There Were None
    3- The Red Signal: An Agatha Christie Short Story
    >>> author_books
    ['The Mysterious Affair at Styles', 'And Then There Were None', 'The Red
    Signal: An Agatha Christie Short Story']
    """
    book_list = []
    author_title_list = []
    book_num = 0

    for genere in dataset:
        book_list += dataset.get(genere) #Re-organisezes the data set into a list of dictonaries of book info

    print('The author "{0}" has published the following books:'.format(author_name))

    for book in book_list: #For each book in the complete list of books
        if book.get('author') == author_name: #If the author of the book matches the given author name
            if book['title'] not in author_title_list: #If the book is not in the book title list
                author_title_list.append(book['title']) #Adds it to a set of book titles by that author
                book_num += 1 #Adds 1 to the book number (starting at 0)
                print('{0}- {1}'.format(book_num, book['title'])) #Prints book number and title of corresponding book

    if len(author_title_list) == 0: #If there are no books by the author
        print(None) #Prints None in place of book info that would of been displayed
        return [] #Returns Empty list in place of where list of book titles would be

    return author_title_list #Returns the list of book title for the author
# Function 7, written by Owen
def get_books_by_publisher(publisher: str, dataset: dict) -> list:
    """ Returns a list of the book titles for books associated with the
    publisher when given the publisher and the dataset being analyzed.
    Precondititon: publisher must be spelled with the correct casing
    >>> books = load_dataset('Google_Books_Dataset.csv')
    >>> publisher_books = get_books_by_publisher("AMACOM", books)
    1- Business Strategy (The Brian Tracy Success Library)
    2- Personal Success (The Brian Tracy Success Library)
    3- The Essentials of Finance and Accounting for Nonfinancial Managers
    4- Marketing (The Brian Tracy Success Library)
    5- Management (The Brian Tracy Success Library)
    >>> publisher_books
    ['Business Strategy (The Brian Tracy Success Library)',
    'Personal Success (The Brian Tracy Success Library)',
    'The Essentials of Finance and Accounting for Nonfinancial Managers',
    'Marketing (The Brian Tracy Success Library)',
    'Management (The Brian Tracy Success Library)']
    """
    book_list = []
    publisher_title_list = []
    book_num = 0

    for genere in dataset:
        book_list += dataset.get(genere) #Re-organisezes the data set into a list of dictonaries of book info

    print('The publisher "{0}" has published the following books:'.format(publisher))

    for book in book_list: #For each book in the complete list of books
        if book.get('publisher') == publisher: #If the publisher of the book matches the given publisher name
            if book['title'] not in publisher_title_list: #If the book is not in the book title list
                publisher_title_list.append(book['title']) #Adds it to a set of book titles by that publisher
                book_num += 1 #Adds 1 to the book number (starting at 0)
                print('{0}- {1}'.format(book_num, book['title'])) #Prints book number and title of corresponding book

    if len(publisher_title_list) == 0: #If there are no books by the publisher
        print(None) #Prints None in place of book info that would of been displayed
        return [] #Returns Empty list in place of where list of book titles would be

    return publisher_title_list #Returns the list of book title for the publisher

# Function 8, written by Imshaad
def check_category_and_title(category: str, title: str, dataset: dict) -> bool:
    """
    Returns a boolean value depending on whether the book's title exists in the
    dataset dictionary for the given category.
    Additionally prints whether the given category contains the book's title or not.

    >>>check_category_and_title("Mystery","Antiques Chop", books)
    The category "Mystery" has the book title "Antiques Chop".
    True
    >>>check_category_and_title("Adventure","The Black Box", books)
    The category "Adventure" does not have the book title "The Black Box".
    False

    """
    category_book_list = dataset.get(category) #Stores all the books of the given category into a list.
    if category_book_list == None:
        category_book_list = []
    category_title_list = [] #An empty list which will store the titles of all books of the given category in category_book_list.

    for book in category_book_list: #Iterates through each book in category_book_list and adds the title of each book in title_list.
        book_title = book['title'] #Stores the book title of the current iteration in book_title.
        category_title_list.append(book_title) #Adds each book title to category_title_list.

    if title in category_title_list: #Checks if title is in category_title_list.
        print('The category "{}" has the book title "{}".'.format(category, title))
        return True
    else:
        print('The category "{}" does not have the book title "{}".'.format(category, title))
        return False

# Function 9, written by Imshaad
def all_categories_for_book_title(title: str, dataset: dict) -> list:
    """
    Returns a list of categories for the given title.
    Additionally prints the book title with its categories.

    >>>all_categories_for_book_title("Sword of Destiny: Witcher 2: Tales of the Witcher", books)
    The book title “Sword of Destiny: Witcher 2: Tales of the Witcher” has the following categories:

            1- Adventure
            2- Fiction
            3- Mythical Creatures

    ['Adventure', 'Fiction', 'Mythical Creatures']

    >>>all_categories_for_book_title("We", books)
    The book title “We” has the following categories:

            1- Fantasy
	    2- Fiction

    ['Fantasy', 'Fiction']

    """
    category_list = [] #This list will store all the categories for the given book title.
    for category in dataset: #Iterates through each category in dataset.
        book_category_list = dataset.get(category) #Stores all the books of the category in iteration into a list.
        title_category_list = [] #An empty list which will store the title of all books in the category in iteration.
        for book in book_category_list: #Iterates through each book in book_category_list.
            book_title = book['title'] #Stores the book title of the current iteration in book_title.
            title_category_list.append(book_title) #Adds each book title to title_category_list.
            if title in title_category_list: #Checks if title is in title_category_list.
                if category not in category_list: #Checks if category is not in category_list.
                    category_list.append(category) #Adds category to category_list if condition is True.

    print('The book title “{}” has the following categories:'.format(title))
    print()
    for i in range(len(category_list)):
        print("\t{}- {}".format(i+1, category_list[i]))
    print()

    return category_list

# Function 10, written by Moataz
def get_books_by_category(category: str, dataset: dict) -> list:
    """ Return a list of book titles based on a particular 'category' | searches in 'dataset'
    Prints a numerized summary of the books' titles.

    >>> get_books_by_category('Fiction', books)
    The category "Fiction" has the following books:
    1 - Antiques Roadkill: A Trash 'n' Treasures Mystery
    2 - The Painted Man (The Demon Cycle, Book 1)
    3 - Edgedancer: From the Stormlight Archive
    ...
    ...
    ["Antiques Roadkill: A Trash 'n' Treasures Mystery", 'The Painted Man (The Demon Cycle, Book 1)', 'Edgedancer: From the Stormlight Archive', '...' , '...' , '...' ]

    >>> get_books_by_category('classicS', books)
    The category "Classics" has the following books:
    1 - The Memoirs of Sherlock Holmes
    2 - The Mysterious Affair at Styles
    ['The Memoirs of Sherlock Holmes', 'The Mysterious Affair at Styles']

    """
    books_by_genre_list = dataset.get(category.strip()) # Sort the books into a list by genre/category.
    book_title_list = []
    book_count = 1

    if books_by_genre_list == None: return None

    print(f'The category "{category}" has the following books:')

    for book in books_by_genre_list: # Iterate over each book in category.
        print(f'{book_count} - {book.get("title")}')
        book_title_list.append(book.get("title")) # Add book title to return list.
        book_count += 1

    return book_title_list

# Function 11, written by Moataz
def get_books_by_category_and_rate(category: str, rate: int, dataset: dict) -> list:
    """ Return a list of book titles based on a particular 'category' with a rating between 'rating' inclusive, and 'rating + 1' exclusive | Searches in 'dataset'
    Prints a numerized summary of the books' titles.

    >>> get_books_by_category_and_rate('fiction ',3 ,books)
    The category "Fiction" and rating 3 has the following books:
    1 - Antiques Roadkill: A Trash 'n' Treasures Mystery
    2 - Bring Me Back
    3 - Mrs. Pollifax Unveiled
    ["Antiques Roadkill: A Trash 'n' Treasures Mystery", 'Bring Me Back', 'Mrs. Pollifax Unveiled']

    >>> get_books_by_category_and_rate('fiction ',5 ,books)
    The category "Fiction" and rating 5 has the following books:
    1 - Final Option: 'The best one yet'
    2 - The Red Signal: An Agatha Christie Short Story
    ["Final Option: 'The best one yet'", 'The Red Signal: An Agatha Christie Short Story']

    """
    books_by_genre_list = dataset.get(category.strip()) # Sort the books into a list by genre/catergory.
    book_title_list = []
    book_count = 1

    if books_by_genre_list == None: return None

    print(f'The category "{category}" and rating {rate} has the following books:')

    for book in books_by_genre_list: # Iterate over each book in category.
        if type(book.get("rating")) != str and (rate <= book.get("rating") < rate + 1): # if the rating exits AND the rating matches the argument.
            print(f'{book_count} - {book.get("title")}')
            book_title_list.append(book.get("title")) # Add book title to return list.
            book_count += 1

    return book_title_list

# Function 12, written by Moataz
def get_author_categories(author: str, dataset: dict) -> list:
    """ Return a list of categories associated with an 'author' | Searches in 'dataset'
    Prints a numerized summary of the author's categories/genres.
    Conditions: Authors name must be typed in full with proper casing | Can search with last name.

    >>> get_author_categories('king ', books)
    The author Stephen King has published books under the following categories:
    1 - Fiction
    2 - Thrillers
    ['Fiction', 'Thrillers']

    >>> get_author_categories('martin ', books)
    The author George R.R. Martin has published books under the following categories:
    1 - Adventure
    2 - Epic
    3 - Fiction
    4 - Fantasy
    ['Adventure', 'Epic', 'Fiction', 'Fantasy']

    >>> get_author_categories('Laura Levine' , books)
    The author Laura Levine has published books under the following categories:
    1 - Detective
    2 - Fiction
    ['Detective', 'Fiction']

    """
    category_list = dataset.keys() # Sort available genres/categories into a list.
    final_category_list = []
    author_name = author


    for category in category_list: # Iterate through genres/categories.
        book_by_genre_list = dataset.get(category) # Sort all books in that genre/category into a list.
        for book in book_by_genre_list:
            if book.get('author') == author_name.strip() or book.get('author').endswith(author.strip()): # strip argument, compare it with the book's author OR compare it with book's author's last name.
                if category not in final_category_list:
                    final_category_list.append(category) # Add category into set.
                    author_name = book.get('author') # Update author name in case last name was used as an argument.

    print(f'The author {author_name} has published books under the following categories:')

    for category in final_category_list:
        print(f'{final_category_list.index(category) + 1} - {category}')

    return final_category_list
