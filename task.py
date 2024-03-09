

class Book:
   def __init__(self, title:str, category:str, author:str):
      self.title = title
      self.category = category
      self.author = author
   def __str__(self):
      return f"Title: {self.title} by {self.author}, category:{self.category}"

class Shelf:
   def __init__(self):
      self.books = []
      self.categories =set()
   def organize_books (self, books:list):
      for book in books:
         self.books.append(book)
         self.categories.add(book.category)
   def sort_books_by_title (self):
      self.books.sort(key=lambda x: x.title)
   def __str__(self):
      shelf_books_by_category=""
      for category in self.categories:
         shelf_books_by_category +=f"Category:{category}\n"
         category_books = [book for book in self.books if book.category == category]
         for book in category_books:
            shelf_books_by_category += f"book:{book}\n"
      return shelf_books_by_category         

def create_books():
   from faker import Faker
   fake = Faker()
   books =[]
   for list in range(10):
      title = fake.catch_phrase()
      category = fake.word()
      author = fake.name()
      books.append(Book(title,category,author))
   return books

def create_shelf_in_room ():
   room =[]
   for x in range(1):
      shelf = Shelf()
      room.append(shelf)
   books_create = create_books()
   for shelf in room:
      shelf.organize_books(books_create)
   for shelf in room:
      shelf.sort_books_by_title()
      print(shelf)

create_shelf_in_room ()