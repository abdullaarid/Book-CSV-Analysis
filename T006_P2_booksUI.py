#Date: 07/12/2021 Version: 1.0
"""
team identifier: T006
Abdulla Arid (101217955)
Moataz Dabbour (100863820)
Imshaad Naaz (101215412)
Owen Renette (101223576)
"""
from P5_T006_load_data import load_dataset
from T006_P3_sorting import sort_books_title, sort_books_category,sort_books_pageCount,sort_books_ascending_rate, sort_books_descending_rate,sort_books_publisher
from T006_P2_search_modify_dataset import add_book, remove_book, find_books_by_title,print_dictionary_category, get_author_categories, all_categories_for_book_title,get_books_by_rate, get_books_by_author, get_books_by_publisher, get_books_by_category, check_category_and_title, get_books_by_category_and_rate

#case 1, written by Moataz
def case1(dataset:dict,userInput:str) -> None:
    """
    Calls desired function using dataset as an argument
    precondition is rating entered is float and pages is int

    >>> UserInterface()
    dataset loaded
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

    : r
    Please enter the book title: After Anna
    Please enter the book genre: Fiction
    The book has been removed correctly
    """
    FUNC = {'L': [load_dataset ,'Please enter a file name: ', 0], \
    'A': [add_book , "Please enter book information starting with Title: " , "Author: ", "Language: ", "Publisher: ", "Category: ", "Rating: ", "Page Count (numerical): ", dataset, 7], \
    'R': [remove_book, 'Please enter the book title: ', 'Please enter the book genre: ', dataset, 2],\
    'F': [find_books_by_title, 'Please enter the book title: ', dataset, 1] }
    command = FUNC.get(userInput.upper())
    function = command[0]                                      # Assigning function
    num_of_inputs = command[-1]                                # Assigning number of user inputs/prompts.
    # 1 to 7 input functions #
    if num_of_inputs == 1:                                   # looks at 1 input FUNC
        function(input(command[1]), dataset)
    elif num_of_inputs == 2:                                   # looks at 2 input FUNC
        function(input(command[1]), input(command[2]), dataset)
    elif num_of_inputs == 7:
        book_tup = (str(input(command[1])) , str(input(command[2])), str(input(command[3])), str(input(command[4])), str(input(command[5])) , float(input(command[6])) , int(input(command[7])))
        function(dataset, book_tup)

#case 2, written by Owen
def case2(dataset:dict,userInput:str)-> None:
    """
    Calls desired function(print_dictionary_category,get_author_categories,all_categories_for_book_title) using dataset as an argument

    >>> UserInterface()
    dataset loaded
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

    : cb
    Enter a Book Title: After Anna
    The book title “After Anna” has the following categories:

            1- Adventure
            2- Fiction
            3- Mystery
            4- Thrillers

    The catagories associated with the book title "After Anna" are ['Adventure', 'Fiction', 'Mystery', 'Thrillers']
    """
    if userInput == 'NC':
        gen_name = input('Enter a Genere: ') # User inputs Genere name
        book_num = print_dictionary_category(gen_name, dataset) # Gets how many books are in the genere
        print('There are {0} books in the category "{1}"'.format(book_num, gen_name)) # Prints Infromation

    elif userInput == 'CA':
        author_name = input('Enter a Author Name: ') # User inputs author name
        author_generes = get_author_categories(author_name, dataset) # Gets generes associated with author
        print('The catagories associated with the author "{1}" are {0}'.format(author_generes, author_name)) # Prints Infromation

    elif userInput == 'CB':
        book_title = input('Enter a Book Title: ') # User inputs book title name
        booktitle_generes = all_categories_for_book_title(book_title, dataset) # Gets generes associated with the book title
        print('The catagories associated with the book title "{1}" are {0}'.format(booktitle_generes, book_title)) # Prints Infromation

#case 3, written by Imshaad
def case3(dataset:dict)-> None:
    """
    Calls desired get book function using dataset as an argument
    precondition is that rate entered is a positive int

    >>> UserInterface()
    dataset loaded
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

    : g
    Please enter another command from the following:
    R)ate   A)uthor   P)ublisher   C)ategory
    CT) Category and Title    CR) Category and Rate

    : r
    Please enter a rate (must be a positive integer): 4
    Title: Sword of Destiny: Witcher 2: Tales of the Witcher
    Author: Andrzej Sapkowski
    Rating: 4.8
    Publisher: Hachette UK
    Page count: 400
    Language: English
    Genere: Adventure
    -----------------
    Title: A Feast for Crows (A Song of Ice and Fire, Book 4)
    Author: George R.R. Martin
    Rating: 4.5
    Publisher: HarperCollins UK
    Page count: 864
    Language: English
    Genere: Adventure

    Next book
    """
    command8sub = 'Please enter another command from the following:\nR)ate   A)uthor   P)ublisher   C)ategory\nCT) Category and Title    CR) Category and Rate\n\n: ' #Sub commands 8 Interface text
    user_input = input(command8sub).upper() #Promts user to enter a command from the sub menu of command 8
    if user_input == 'R': #If user selects Rate
        rate = int(input('Please enter a rate (must be a positive integer): ')) #Prompts user to enter a rate in a specified format, which is then converted to an integer.
        get_books_by_rate(rate, dataset) #calls the function which will get books of the specified rate
    elif user_input == 'A':#If user selects Author
        author = input('Please enter the name of an author: ') #Prompts user to enter an author
        get_books_by_author(author, dataset) #calls the function which will get books of the specified author
    elif user_input == 'P':#If user selects Publisher
        publisher = input('Please enter the name of a publisher: ') #Prompts user to enter a publisher
        get_books_by_publisher(publisher, dataset)  #calls the function which will get books of the specified publisher
    elif user_input == 'C':#If user selects Category
        category = input('Please enter a category: ') #Prompts user to enter a category
        get_books_by_category(category, dataset) #calls the function which will get books of the specified category
    elif user_input == 'CT':#If user selects Category and Title
        category = input('Please enter a category: ') #Prompts user to enter a category
        title = input('Please enter a title of a book: ') #Prompts user to enter a book title
        check_category_and_title(category, title, dataset) #calls the function which checks that the specified title is in the specified category
    elif user_input == 'CR':#If user selects Category and Rate
        category = input('Please enter a category: ') #Prompts user to enter a category
        rate = int(input('Please enter a rate (must be a positive integer): ')) #Prompts user to enter a rate in a specified format, which is then converted to an integer.
        get_books_by_category_and_rate(category, rate, dataset) #calls the function which will get books of the specified category and rate
    else: print("No such command")

#case 4, written by Abdulla
def case4(dataset:dict)-> None:
    """
    prints books by a desired sorting (title,rate,publisher,category,pagecount) with dataset as argument
    precondition is that when entering a dataset, it is valid and in the same folder.

    >>> UserInterface()
    dataset loaded
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

    : s

    T)itle    R)ate    P)ublisher    C)ategory    PA)ageCount

    : T

    Title: A Feast for Crows (A Song of Ice and Fire, Book 4)
    Title: A Feast for Crows (A Song of Ice and Fire, Book 4)
    next book
    """
    sub9 = "T)itle    R)ate    P)ublisher    C)ategory    PA)ageCount \n\n: " #submenu 9 text
    sub9Input = input(sub9).upper() #shows the submenu and prompts a selection
    if sub9Input == 'T': #if user selects title it calls the sort by title function with the loaded dataset
        sort_books_title(dataset)
    elif sub9Input == 'R': #if user selects order by rate
        sub9Input = input("Ascending or Descending('A' or 'D')?: ").upper() #prompts user to enter 'A' for ascending rate or 'D' for descending rate
        if sub9Input == 'A': #if user selects ascending order calls that function
            print("Ascending rate")
            sort_books_ascending_rate(dataset)
        elif sub9Input == 'D': #if user selects descending order calls that function
            print("Descending rate")
            sort_books_descending_rate(dataset)
        elif sub9Input == 'Q': #if user selects Q to quit, the program returns to main menu
            print("No such command")
        else: print("No such command") #if none of the options are selected informs the user that it will return to main menu
    elif sub9Input == 'P': #if user selects sort by publisher, calls that function
        sort_books_publisher(dataset)
    elif sub9Input == 'C': #if user selects sort by category, calls that function
        sort_books_category(dataset)
    elif sub9Input == 'PA': #if user selects sort by page count, calls that function
        sort_books_pageCount(dataset)
    else: print("No such command")



def userInterface()->None:
    """
    Returns None
    precondition is that when entering a dataset, it is valid and in the same folder.
    >>> UserInterface()
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

    Please enter the datatset to load (name.csv): Google_Books_Dataset.csv
    Data loaded
    """
    ui = """\n1- Command line L)oad file\n2- Command line A)dd book \n3- Command line R)emove book\n4- Command Line F)ind book by title\n5- Command Line NC) Number of books in a category\n6- Command Line CA) Categories for an author\n7- Command Line CB) Categories for a book title\n8- Command Line G)et book\n\t R)ate   A)uthor   P)ublisher   C)ategory\n\t CT) Category and Title    CR) Category and Rate\n9- Command Line S)ort book\n\t T)itle    R)ate    P)ublisher    C)ategory    PA)ageCount\n10- Command line Q)uit\n\n: """
    userInput = True #initializes userInput
    dataLoaded = False #no dataest has been loaded
    while userInput != 'Q':
        userInput = input(ui).upper() #shows the main menu and prompts the option and capitalizes it
        if userInput == 'L': #if a user attempts ot load a dataset
            dataset = load_dataset(input("please enter the datatset to load (name.csv): ")) #asks the user to enter a dataset in the proper format
            dataLoaded = True #sets the dataLoaded as True so that other commands can be run
            print('Data loaded.')
        elif userInput == 'A':
            if dataLoaded == False:
                print("No file loaded")
            else:
                case1(dataset, userInput)
        elif userInput == 'R':
            if dataLoaded == False:
                print("No file loaded")
            else:
                case1(dataset, userInput)
        elif userInput == 'F':
            if dataLoaded == False:
                print("No file loaded")
            else:
                case1(dataset, userInput)
        elif userInput == 'NC':
            if dataLoaded == False:
                print("No file loaded")
            else:
                case2(dataset, userInput)
        elif userInput == 'CA':
            if dataLoaded == False:
                print("No file loaded")
            else:
                case2(dataset, userInput)
        elif userInput == 'CB':
            if dataLoaded == False:
                print("No file loaded")
            else:
                case2(dataset, userInput)
        elif userInput == 'G':
            if dataLoaded == False:
                print("No file loaded")
            else:
                case3(dataset)
        elif userInput == 'S':
            if dataLoaded == False:
                print("No file loaded")
            else:
                case4(dataset)
        elif userInput == 'Q':
            print("Goodbye")
        else: print("No such command")


userInterface()
