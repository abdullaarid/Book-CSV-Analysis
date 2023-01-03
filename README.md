# Data Analyzer - Version 1.0 - 2021-12-08
## ECOR1042 - Team 006

### General Usage Notes
- This project parses a .CSV file downloaded from google books library and provides tools for a user to manage the data.
Tools a user can use include sorting by different criteria, data look-up, find the number of books in a category, find the categories for a published author, or book.

- The user must enter an integer or float when asked, there is no error checking for input types.

### Required Resources:
For users on Windows 10:
- User must have Python Version 3.7 or higher installed. Can be found online [here](https://www.python.org/downloads/)
- Google Books API export to CSV. Learn more online [here](https://developers.google.com/books/docs/v1/using)

### Installation:
- Install ZIP file "T006_data_analyzer" and extract to pc
- Move the database .CSV file into the same directory the ZIP was unpacked. (Optional as Google_Books_Dataset.csv can be used and is provided in the ZIP file)
- Run "T006_P2_booksUI.py" in a Python editor such as Wing 101
- The UI will start in the shell, start with Command Line 1 "Load File" by pressing "L"

T006_load_data contains:
- P5_T006_load_data.py
- T006_P2_search_modify_dataset.py
- T006_P3_sorting.py
- T006_P2_booksUI.py
- Google_Books_Dataset.csv

**ALL FILES MUST BE STORED IN THE SAME FOLDER**
### Usage:
Example 1 (Loading dataset):
```Python
1- Command line L)oad file
2- Command line A)dd book
3- Command line R)emove book
4- Command Line F)ind book by title
5- Command Line NC) Number of books in a category
6- Command Line CA) Categories for an author
7- Command Line CB) Categories for a book title
8- Command Line G)et book
         R)ate   A)uthor   P)ublisher   C)ategory
         CT) Category and Title    CR) Category and Rate
9- Command Line S)ort book
         T)itle    R)ate    P)ublisher    C)ategory    PA)ageCount
10- Command line Q)uit

: L
please enter the datatset to load (name.csv): Google_Books_Dataset.csv
Data loaded.
```

Example 2 (Adding book):
```Python
1- Command line L)oad file
2- Command line A)dd book
3- Command line R)emove book
4- Command Line F)ind book by title
5- Command Line NC) Number of books in a category
6- Command Line CA) Categories for an author
7- Command Line CB) Categories for a book title
8- Command Line G)et book
         R)ate   A)uthor   P)ublisher   C)ategory
         CT) Category and Title    CR) Category and Rate
9- Command Line S)ort book
         T)itle    R)ate    P)ublisher    C)ategory    PA)ageCount
10- Command line Q)uit

: A
Please enter book information starting with Title: New book
Author: T006
Language: English
Publisher: ECOR 1042
Category: New category
Rating: 5.0
Page Count (numerical): 198
The book has been added correctly
```

Example 3 (Number of books in a category):
```Python
1- Command line L)oad file
2- Command line A)dd book
3- Command line R)emove book
4- Command Line F)ind book by title
5- Command Line NC) Number of books in a category
6- Command Line CA) Categories for an author
7- Command Line CB) Categories for a book title
8- Command Line G)et book
         R)ate   A)uthor   P)ublisher   C)ategory
         CT) Category and Title    CR) Category and Rate
9- Command Line S)ort book
         T)itle    R)ate    P)ublisher    C)ategory    PA)ageCount
10- Command line Q)uit

: NC
Enter a Genere: New category
The category New category has 1 book(s). This is the list of books in the category New category:


title: New book
author: T006
rating: 5.0
publisher: ECOR 1042
page_count: 198
language: English
There are 1 books in the category "New category"
```
Example 4 (Sorting by title):
```Python
1- Command line L)oad file
2- Command line A)dd book
3- Command line R)emove book
4- Command Line F)ind book by title
5- Command Line NC) Number of books in a category
6- Command Line CA) Categories for an author
7- Command Line CB) Categories for a book title
8- Command Line G)et book
         R)ate   A)uthor   P)ublisher   C)ategory
         CT) Category and Title    CR) Category and Rate
9- Command Line S)ort book
         T)itle    R)ate    P)ublisher    C)ategory    PA)ageCount
10- Command line Q)uit

: S
T)itle    R)ate    P)ublisher    C)ategory    PA)ageCount

: T
Title: A Feast for Crows (A Song of Ice and Fire, Book 4)
Title: A Feast for Crows (A Song of Ice and Fire, Book 4)
Title: A Feast for Crows (A Song of Ice and Fire, Book 4)
Title: A Feast for Crows (A Song of Ice and Fire, Book 4)
Title: A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
...
```

Example 5 (Quitting):
```Python
1- Command line L)oad file
2- Command line A)dd book
3- Command line R)emove book
4- Command Line F)ind book by title
5- Command Line NC) Number of books in a category
6- Command Line CA) Categories for an author
7- Command Line CB) Categories for a book title
8- Command Line G)et book
         R)ate   A)uthor   P)ublisher   C)ategory
         CT) Category and Title    CR) Category and Rate
9- Command Line S)ort book
         T)itle    R)ate    P)ublisher    C)ategory    PA)ageCount
10- Command line Q)uit

: Q
Goodbye
```

### For any questions, comments, or concerns, contact:
- [Abdulla Arid](mailto:ABDULLAARID@cmail.carleton.ca)

### Credits:
Functions written by Abdulla Arid:
- T006_P2_search_modify_dataset.py - print_dictionary_category, add_book, remove_book
- T006_P3_sorting.py - sort_books_publisher, sort_books_category
- T006_P2_booksUI.py - Command 'S'

Functions written by Moataz Dabbour:
- T006_P2_search_modify_dataset.py - get_books_by_category, get_books_by_category_and_rate, get_author_categories
- T006_P3_sorting.py - sort_books_ascending_rate, sort_books_descending_rate
- T006_P2_booksUI.py - Commands 'L','A','R', and 'F'

Functions written by Imshaad Naaz:
- T006_P2_search_modify_dataset.py - find_books_by_title, check_category_and_title, all_categories_for_book_title
- T006_P3_sorting.py - sort_books_title
- T006_P2_booksUI.py - Command 'G'

Functions written by Owen Renette:
- T006_P2_search_modify_dataset.py - get_books_by_rate, get_books_by_author, get_books_by_publisher
- T006_P3_sorting.py - sort_books_pageCount
- T006_P2_booksUI.py - Commands 'NC','CA','CB', and 'Q'

### License

Copyright (c) 2021, T006 1042 Data Management

This software was created under academic conditions, no licensing or trademarks applicable.
