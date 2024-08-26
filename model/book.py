class Book:
    def __init__(self,id,title):
        self.id = id
        self.title = title
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title})"