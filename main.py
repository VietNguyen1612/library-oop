from model.student import Student
from model.book import Book
from model.library import Library

def menu():
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Add Student")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Students")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    return choice

def add_student_data(library: Library):
    library.add_student(Student('001',20,'Dave'))
    library.add_student(Student('002',22,'John'))
    return library

def main():
    library = Library()
    library = add_student_data(library)
    library.load_book_from_files()
    while True:
        choice = menu()
        if choice == '1':
            print('* * * * *')
            id = input('Input book id: ')
            title = input('Input book title: ')
            library.add_book(Book(id,title))
            library.save_book_to_file()
            print('* * * * *\n')
        elif choice == '2': 
            print('* * * * *')
            id = input('Input student id: ')
            name = input('Input student name: ')
            age = input('Input student age: ')
            library.add_student(Student(id,age,name))
            print('* * * * *\n')
        elif choice == '3': 
            print('* * * * *')
            student_id = input('Input student id: ') 
            student = library.find_student(student_id)
            book_id = input('Input book id: ')
            book = library.find_book(book_id)
            student.borrow_book(book)
            library.save_book_to_file()
            print('* * * * *\n')
        elif choice == '4': 
            print('* * * * *')
            student_id = input('Input student id: ') 
            student = library.find_student(student_id)
            book_id = input('Input book id: ')
            book = library.find_book(book_id)
            student.return_book(book)
            library.save_book_to_file()
            print('* * * * *\n')
        elif choice == '5': 
            print('* * * * *')
            library.show_books()
            print('* * * * *\n')
        elif choice == '6': 
            print('* * * * *')
            library.show_students()
            print('* * * * *\n')
        elif choice == '7':
            print('* * * * *')
            print ('Exit')
            break
        else:
            print('invalid choice')

main()