#Example 1
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def get_details(self):
        return f"Book: {self.title} by {self.author}, ISBN: {self.isbn}"

class Magazine:
    def __init__(self, title, publisher, issue):
        self.title = title
        self.publisher = publisher
        self.issue = issue

    def get_details(self):
        return f"Magazine: {self.title}, Publisher: {self.publisher}, Issue: {self.issue}"

class DVD:
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration

    def get_details(self):
        return f"DVD: {self.title} directed by {self.director}, Duration: {self.duration} minutes"

# Example usage
book = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789")
print(book.get_details())

magazine = Magazine("National Geographic", "National Geographic Society", "April 2024")
print(magazine.get_details())

dvd = DVD("Inception", "Christopher Nolan", 148)
print(dvd.get_details())
