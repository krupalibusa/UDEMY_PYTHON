# Example 2
class LibraryItem:
    def __init__(self, title):
        self.title = title

    def get_details(self):
        raise NotImplementedError("Subclasses should implement this method")

class Book(LibraryItem):
    def __init__(self, title, author, isbn):
        super().__init__(title)
        self.author = author
        self.isbn = isbn

    def get_details(self):
        return f"Book: {self.title} by {self.author}, ISBN: {self.isbn}"

class Magazine(LibraryItem):
    def __init__(self, title, publisher, issue):
        super().__init__(title)
        self.publisher = publisher
        self.issue = issue

    def get_details(self):
        return f"Magazine: {self.title}, Publisher: {self.publisher}, Issue: {self.issue}"

class DVD(LibraryItem):
    def __init__(self, title, director, duration):
        super().__init__(title)
        self.director = director
        self.duration = duration

    def get_details(self):
        return f"DVD: {self.title} directed by {self.director}, Duration: {self.duration} minutes"

# Example usage
items = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789"),
    Magazine("National Geographic", "National Geographic Society", "April 2024"),
    DVD("Inception", "Christopher Nolan", 148)
]

for item in items:
    print(item.get_details())
