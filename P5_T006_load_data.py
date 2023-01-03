#Date: 07/12/2021 Version: 1.0
"""
team identifier: T006
Abdulla Arid (101217955)
Moataz Dabbour (100863820)
Imshaad Naaz (101215412)
Owen Renette (101223576)
"""
from csv import reader
def load_dataset(file_name: str) -> dict:
    """ Return a main dictionary with genres as keys, and a list of dictionaries of books as values.
    Conditions: 'file_name' must be .CSV

    >>> load_dataset('Google_Books_Dataset.csv')

    {'Adventure': [{'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'page_count': 400, 'language': 'English'},
    {next book},{last book}],'Biography': [{'title': 'Boy Erased: A Memoir', 'author': 'Garrard Conley', 'rating': 4.0, 'publisher': 'Penguin', 'page_count': 352, 'language': 'English'},{next book}], 'next genre':[{books}]}
    """
    main_list = [] # Books list
    book_dictionary = {} # Final dictionary to return
    indv_book = {}
    genre_set = set() # Set of genres
    # Open csv file and read from it
    local_file = open(file_name)
    csv_file = reader(local_file)
    header_list = next(csv_file) # Header list - first line/row in the CSV

    for row in csv_file: # Iterates through the csv file
        main_list.append(row) # Combining all books into a list
    local_file.close() # Closing temp file.

    for book in main_list: # Extracting genres into a set → then a list
        genre_set.add(book[6])
    main_genre_list = list(genre_set)
    main_genre_list.sort() # Alphabetical sorting

    for genre in main_genre_list: # Updating the main dict to have genres as keys
        book_collection = [] # List containing all books for that genre
        for book in main_list: # Iterating over each book
            if book[6] == genre: # Book is equal to the current genre, add to book_collection list
                if book[3]== '': # If the rating is empty show as N/A
                    book[3] = 'N/A'
                else: book[3] = float(book[3]) # Set rating to float if not empty
                indv_book = {header_list[1]:book[1], header_list[2]:book[2],header_list[3]:book[3], header_list[4]:book[4], header_list[5]:int(book[5]), header_list[7]:book[7]}
                if indv_book not in book_collection:#only adds to the book collection if it is not already in it
                    book_collection.append(indv_book)
        book_dictionary.update({genre:book_collection}) # Add all books with same genre to that genre key


    return book_dictionary # Return a main dictionary with genres as keys, and a list of dictionaries of books as values
