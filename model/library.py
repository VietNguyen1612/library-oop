from model.book import Book
from model.student import Student


class Library:
    def __init__(self):
        self.books = []
        self.students = []
    
    def add_book(self,book):
        self.books.append(book)
        print(book.title+' added')
    
    def add_student(self,student):
        self.students.append(student)
        print(student.name+' added')
    
    def find_student(self,student_id):
        for student in self.students:
            if(student_id == student.id):
                return student
        print('Student does not exist')
        return None
    
    def find_book(self,book_id):
        for book in self.books:
            if(book_id == book.id):
                return book
        print('Book does not exist')
        return None
    
    def show_books(self):
        print ("{:<4} {:<12} {:<15}".format('ID','Title','Status'))
        for item in self.books:
            item_status = 'borrowed' if item.is_borrowed == True else 'avaiable'
            print ("{:<4} {:<12} {:<15}".format(item.id,item.title,item_status))

    def show_students(self):
        print ("{:<5} {:<5} {:<15} {:<15}".format('ID','Age','Name', 'Books'))
        for item in self.students:
            borrowed_books = ''
            for book in item.borrowed_books:
                if(borrowed_books == ''):
                    borrowed_books = book.title
                else: 
                    borrowed_books = borrowed_books + ", " + book.title
            if(borrowed_books == ''):
                borrowed_books = 'none'
            print ("{:<5} {:<5} {:<15} {:<15}".format(item.id,item.age,item.name,borrowed_books))

    def save_book_to_file(self):
        file = open('./books.txt','w')
        for book in self.books:
            file.write(f"{book.id},{book.title},{book.is_borrowed}\n")


    def load_book_from_files(self):
        try:
            file = open('./books.txt', 'r')
            for line in file:
                id, title, is_borrowed = line.strip().split(',')
                book = Book(id,title)
                book.is_borrowed = is_borrowed == 'True'
                self.books.append(book)
        except FileNotFoundError:
            print("No existing books found")