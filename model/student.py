class Student: 

    def __init__(self,id,age,name):
        self.id = id
        self.age = age
        self.name = name
        self.borrowed_books = set({})

    def borrow_book(self,book):
            if(book.is_borrowed == True and book not in self.borrowed_books):
                print('Book is borrowed') 
                return
            self.borrowed_books.add(book)
            book.is_borrowed = True
            print(self.name + ' borrowed successfully')

    def return_book(self,book):
        
            if((book.is_borrowed == True and book not in self.borrowed_books) or book.is_borrowed == False):
                print(self.name + ' hasn\'t borrowed this book') 
                return
            self.borrowed_books.remove(book)
            book.is_borrowed = False
            print(self.name + ' returned successfully')
    
    def __str__(self):
        return f"Member: {self.name}, age: {self.age}"