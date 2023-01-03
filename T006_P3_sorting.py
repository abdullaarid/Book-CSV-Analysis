#Date: 07/12/2021 Version: 1.0
"""
team identifier: T006
Abdulla Arid (101217955)
Moataz Dabbour (100863820)
Imshaad Naaz (101215412)
Owen Renette (101223576)
"""

def to_list(dataset: dict) -> list:
    """ Return a list of dictionaries of books from 'dataset', adds genres as keys with respective values, converts all 'N/A' ratings to 0

    >>> books = load_dataset('google_books_dataset.csv')
    >>> convert_to_list(books)
    [{'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'page_count': 400, 'language': 'English', 'genre': 'Adventure'},
    {'title': 'A Feast for Crows (A Song of Ice and Fire, Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 864, 'language': 'English', 'genre': 'Adventure'},
    {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'page_count': 416, 'language': 'English', 'genre': 'Adventure'},
    {...}, ... ]

    """
    booklist = []                                # Final list to be returned.

    for cat in dataset:                          # For every genre:
        for book in dataset[cat]:                # For every book:
            if book['rating'] != 'N/A':          # if rating available:
                booklist += [{"title":book["title"],"author":book["author"],"rating":float(book["rating"]), "publisher":book["publisher"], "page_count":int(book["page_count"]), "generes":cat,"language":book["language"]}] # Append the book to the list.
            elif book['rating'] == 'N/A':        # if rating not available:
                booklist += [{"title":book["title"],"author":book["author"],"rating":0.0, "publisher":book["publisher"], "page_count":book["page_count"], "generes":cat,"language":book["language"]}]       # Replace with 0.0
    return booklist


def bub_sort(lst: list[dict], rank_1: str, rank_2: str, order: str) -> list[dict]:
    ''' return a sorted (using the Bubble Sort Algorithm) list based on a 'lst's dictionary 'rank_1' values, 'rank_2' when 'rank_1' is equal.
    Use 'A' for ascending or 'D' for descending 'order'.
    Use ' ' in 'rank_2' for single rank sorting.
    >>> bub_sort(list, 'rating' ' ' 'D')
    [{'title': 'No One Is Too Small to Make a Difference', 'author': 'Greta Thunberg', 'rating': 5.0, 'publisher': 'Penguin', 'page_count': 112, 'language': 'English', 'genre': 'Biography'}, {...},
    {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'page_count': 226, 'language': 'English', 'genre': 'Fiction'}, {...}, ...]

    >>> bub_sort(list, 'title' ' ' 'A')
    [{'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin',
    'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 4544, 'genre': 'Adventure', 'language': 'English'}, {...},
    {'title': 'Once Missed (A Riley Paige Mysteryâ€”Book 16)', 'author': 'Blake Pierce', 'rating': 4.4, 'publisher': 'Blake Pierce', 'page_count': 250, 'genre': 'Mystery', 'language': 'English'}, {...} ...]

    '''
    length = len(lst)
    if order == 'A':
        for pass_num in range(length):
            num_of_swaps = 0
            for indx in range(0, length - pass_num - 1):
                if  lst[indx][rank_1] > lst[indx + 1][rank_1]:                     # If rating was was higher than the one after it:
                    lst[indx], lst[indx + 1] = lst[indx + 1], lst[indx]            # Swap.
                    num_of_swaps += 1                                              # Update the number of swaps for this pass
                if type(lst[indx].get(rank_2)) != type(None):
                    if lst[indx][rank_1] == lst[indx + 1][rank_1] and lst[indx].get(rank_2) > lst[indx + 1].get(rank_2):
                        lst[indx], lst[indx + 1] = lst[indx + 1], lst[indx]
                        num_of_swaps += 1
            if num_of_swaps == 0:                                                  # No swaps means list is in order, this helps reduce steps if list was already semi-sorted.
                return lst

    if order == 'D':
        for pass_num in range(length):
            num_of_swaps = 0
            for indx in range(0, length - pass_num - 1):
                if lst[indx][rank_1] < lst[indx + 1][rank_1]:                      # If rating was was lower than the one after it:
                    lst[indx], lst[indx + 1] = lst[indx + 1], lst[indx]            # Swap.
                    num_of_swaps += 1                                              # Update the number of swaps for this pass
                if type(lst[indx].get(rank_2)) != type(None):
                    if lst[indx][rank_1] == lst[indx + 1][rank_1] and lst[indx].get(rank_2) < lst[indx + 1].get(rank_2):
                        lst[indx], lst[indx + 1] = lst[indx + 1], lst[indx]
                        num_of_swaps += 1
            if num_of_swaps == 0:                                                  # No swaps means list is in order, this helps reduce steps if list was already semi-sorted.
                return lst
#function 1, written by Imshaad
def sort_books_title(dataset: dict) -> list:
    """
    Returns a list with the book data stored as a dictionary book where the books
    are sorted alphabetically by title. Also prints the data.

    >>>from T006_P1_load_data import load_dataset
    >>>book1 = load_dataset("test_example1.csv")
    >>>sort_books_title(book1)
    Title: After Anna
    Title: Antiques Roadkill: A Trash 'n' Treasures Mystery
    ....Next Book Details....
    Title: The Painted Man (The Demon Cycle, Book 1)

    [{'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'page_count': 416, 'genre': 'Fiction', 'language': 'English'}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 288, 'genre': 'Fiction', 'language': 'English'}, {...}, {...Next Book...}, {...}, {'title': 'The Painted Man (The Demon Cycle, Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 544, 'genre': 'Fiction', 'language': 'English'}]

    >>>book2 = load_dataset("test_example2.csv")
    >>>sort_books_title(book2)
    Title: And Then There Were None
    Title: Boy Erased: A Memoir
    ....Next Book Details....
    Title: Total Control

    [{'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'page_count': 224, 'genre': 'Fiction', 'language': 'English'}, {'title': 'Boy Erased: A Memoir', 'author': 'Garrard Conley', 'rating': 4.0, 'publisher': 'Penguin', 'page_count': 352, 'genre': 'Biography', 'language': 'English'},  {...}, {...Next Book...}, {...},{'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'page_count': 624, 'genre': 'Thrillers', 'language': 'English'}]

    """
    booklist = to_list(dataset)                   # Converting to list.
    bub_sort(booklist, 'title', ' ' ,'A')         # Sorting.

    for book in booklist:
        print("Title: {}".format(book.get("title")))
    print()
    return booklist
#function 2, written by Moataz
def sort_books_ascending_rate(dataset: dict) -> list[dict]:
    """ Return a list of dictionaries of the books in 'dataset' sorted by rating in ascending order. Titles without a rating are displayed first

    >>> books = load_dataset('google_books_dataset.csv')
    >>> sort_books_ascending_rate(books)
    Title: Business Strategy (The Brian Tracy Success Library) - Rating: N/A
    	______
    ...
    	______

    Title: Antiques Roadkill: A Trash 'n' Treasures Mystery - Rating: 3.3
    	______
    ...
    	______

    [{'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 0.0, 'publisher': 'AMACOM', 'page_count': 112, 'language': 'English', 'genre': 'Business'}, {...},
    {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 288, 'language': 'English', 'genre': 'Detective'},
    {...} , ... ]

    """

    booklist = to_list(dataset)                    # Converting to list.
    bub_sort(booklist, 'rating', ' ' ,'A')         # Sorting.

    for book in booklist:                          # For each book:
        if book.get('rating') != 0.0:              # Only print non-zero ratings.
            print(f'Rating: {book.get("rating")} - Title: {book.get("title")}')
        else:
            print(f'Rating: N/A - Title: {book.get("title")}')
    print()
    return booklist

#function 3, written by Moataz
def sort_books_descending_rate(dataset: dict) -> list:
    """ Return a list of dictionaries of the books in 'dataset' sorted by rating in descending order.

    >>> books = load_dataset('google_books_dataset.csv')
    >>> sort_books_descending_rate(books)
    Title: No One Is Too Small to Make a Difference - Rating: 5.0
            ______
    ...
            ______

    Title: Antiques Con -Rating: 4.8
            ______
    ...
            ______

    [{'title': 'No One Is Too Small to Make a Difference', 'author': 'Greta Thunberg', 'rating': 5.0, 'publisher': 'Penguin', 'page_count': 112, 'language': 'English', 'genre': 'Biography'}, {...},
    {'title': 'Antiques Con', 'author': 'Barbara Allan', 'rating': 4.8, 'publisher': 'Kensington Books', 'page_count': 288, 'language': 'English', 'genre': 'Fiction'},
    {...} , ... ]

    """

    booklist = to_list(dataset)                     # Converting to list.
    bub_sort(booklist, 'rating', ' ' , 'D')         # Sorting.

    for book in booklist:                           # For each book:
        if book.get('rating') != 0.0:               # Only print non-zero ratings.
            print(f'Rating: {book.get("rating")} - Title: {book.get("title")}')
        else:
            print(f'Rating: N/A - Title: {book.get("title")}')
    print()
    return booklist

#function 4, written by Abdulla
def sort_books_publisher(dataset:dict) -> list:
    """
    Returns a list of books each in a list ordered by alphabetical order of publishers
    >>> sort_books_publisher(load_dataset("test_unsorted1.csv"))
    Publisher: AMACOM Title: Marketing (The Brian Tracy Success Library)
    Publisher: Hachette UK Title: Sword of Destiny: Witcher 2: Tales of the Witcher
    Publisher: Hachette UK Title: The Guardians: The explosive new thriller from international bestseller John Grisham
    Publisher: Harper Collins Title: Little Girl Lost: A Lucy Black Thriller
    more books
    >>> print(sort_books_publisher(load_dataset("test_unsorted1.csv")))
    [{'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'page_count': 112, 'generes': 'Economics', 'language': 'English'}, {another book}]

    >>> sort_books_publisher(load_dataset("test_unsorted2.csv"))
    Publisher: AMACOM Title: Business Strategy (The Brian Tracy Success Library)
    Publisher: AMACOM Title: Management (The Brian Tracy Success Library)
    Publisher: Ballantine Books Title: Mrs. Pollifax Unveiled
    Publisher: Hachette UK Title: The Tower of the Swallow: Witcher 6
    >>> print(sort_books_publisher(load_dataset("test_unsorted2.csv")))
    [{'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'page_count': 112, 'generes': 'Business', 'language': 'English'}, {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'page_count': 112, 'generes': 'Economics', 'language': 'English'}, {another book}]
    """
    booklist = to_list(dataset)
    bub_sort(booklist, 'publisher', 'title' ,'A')

    for book in booklist:
        print("Publisher: {} - Title: {}".format(book.get("publisher"),book.get("title")))
    print()
    return booklist

#function 5, written by Owen
def sort_books_pageCount(dataset: dict) -> list[dict]:
    """Returns a list of book data stored as a dictonary - sorted by page count
    in ascending order - when given the dataset
    >>> sort = sort_books_pageCount(books)
    Page Count: 14 - Title: Summary: Think and Grow Rich
    ...
    Page Count: 4544 - Title: A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
    >>> sort
    [{'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'rating': 'N/A', 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'page_count': 14, 'generes': 'Business', 'language': 'English'}, ... {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 4544, 'generes': 'Fiction', 'language': 'English'}]
    """
    booklist = to_list(dataset)                      # Converting to list.
    bub_sort(booklist, 'page_count', 'title' ,'A')   # Sorting.

    for book in booklist:
        print('Page Count: {0} - Title: {1}'.format(book['page_count'], book['title'])) # Prints the book data
    print()
    return booklist #Returns sorted list


#function 6, written by Abdulla
def sort_books_category(dataset:dict) -> list:
    """
    Returns a list of books each in a list ordered by alphabetical order of categories
    >>> sort_books_category(load_dataset("test_unsorted1.csv"))
    Category: Comics Title: Deadpool Kills the Marvel Universe
    Category: Economics Title: How To Win Friends and Influence People
    Category: Economics Title: Marketing (The Brian Tracy Success Library)
    Category: Fiction Title: After Anna
    >>> print(sort_books_category(load_dataset("test_unsorted1.csv")))
    [{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'page_count': 96, 'generes': 'Comics', 'language': 'English'}, {another book}]

    >>> sort_books_category(load_dataset("test_unsorted2.csv"))
    Category: Biography Title: Boy Erased: A Memoir
    Category: Business Title: Business Strategy (The Brian Tracy Success Library)
    Category: Business Title: The Infinite Game
    Category: Classics Title: The Memoirs of Sherlock Holmes
    >>> print(sort_books_category(load_dataset("test_unsorted2.csv")))
    {'title': 'Boy Erased: A Memoir', 'author': 'Garrard Conley', 'rating': 4.0, 'publisher': 'Penguin', 'page_count': 352, 'generes': 'Biography', 'language': 'English'}, {another book}]
    """

    booklist = to_list(dataset)                    # Converting to list.
    bub_sort(booklist, 'generes', 'title' ,'A')    # Sorting.

    for book in booklist:
        print("Category: {} - Title: {}".format(book.get("generes"),book.get("title")))
    print()
    return booklist
