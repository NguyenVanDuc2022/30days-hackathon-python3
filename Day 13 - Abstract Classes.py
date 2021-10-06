"""
Day 13 - Given a Book class and a Solution class, write a MyBook class that does the following:
Inherits from Book
Has a parameterized constructor taking these parameters
Implements the Book class' abstract display() method so it prints these lines
--- Nguyen Van Duc ---
"""
from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self): pass


class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price

    def display(self):
        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Price: " + str(self.price))


title = input("Enter title: ")
author = input("Enter author: ")
price = int(input("Enter price: "))
new_novel = MyBook(title, author, price)
new_novel.display()
