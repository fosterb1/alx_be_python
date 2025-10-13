#!/usr/bin/python3
"""
Book class demonstrating Python magic methods:
__init__, __del__, __str__, and __repr__
"""

class Book:
    """A class representing a book with title, author, and year."""

    def __init__(self, title, author, year):
        """Initialize the Book instance with title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Return a readable string representation of the Book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an official string representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Print a message when the Book object is deleted."""
        print(f"Deleting {self.title}")
