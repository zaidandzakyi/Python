#LIBRARY
books = []

def menu():
    print("\n======================")
    print("|     Library app    |".upper())
    print("|====================|")
    print("| [1] Show Books     |")
    print("| [2] Add Book       |")
    print("| [3] Edit Book      |")
    print("| [4] Delete Book    |")
    print("| [5] Quit           |")
    print("======================\n")

    user_choose = input(">> Input Number : ")
    if user_choose == '1':
        show()
    elif user_choose == '2':
        add()
    elif user_choose == '3':
        edit()
    elif user_choose == '4':
        delete()
    elif user_choose == '5':
        print ("--- Program End ---")
        quit()
    else :
        print("!! Wrong Number !!")

def show():
    index = 0
    if len(books) <= 0:
        print("\n>>> Library Still Empty ")
    else :
        print("\n/============\\")
        print("| my library |".upper())
        print("\\============/")
        for book2 in books:
            print(str(index) + ") " + book2)
            index += 1
        print("\n")

def add(): 
    bookName = input(">> Input Book Name : ")
    books.append(bookName)
    print(">>> Book successfully added :) ")


def edit():
    if len(books) <= 0:
        print("\n>>> Library Still Empty ")
        menu()
    else:
        show()
        try:
            index = int(input(">> Input the index : "))
            oldBook = books[index]
            newBook = input(">> New book name : ")
            books[index] = newBook
            print(">>> " + oldBook + ' had been changed to ' + newBook)
        except ValueError:
            print("!! Input the index !!")
            edit()
        except IndexError:
            print("!! Wrong Index !!")
            edit()

def delete():
    if len(books) <= 0:
        print("\n>>> Library Still Empty ")
        menu()
    else:
        show()
        try:
            index = int(input(">> Input The Index : "))
            bookName = books[index]
            del books[index]
            print(">>> " + bookName + " had been deleted")
        except ValueError:
            print("!! Input the index !!")
            delete()
        except IndexError:
            print("!! Wrong Index !!")
            delete()

while True :
    menu()