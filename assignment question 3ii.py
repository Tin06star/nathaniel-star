class book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
            print(f"title: {self.title}")
            print(f"author: {self.author}")
            print(f"price: ${self.price}")
            print("-" * 20)

book1 = book("python basics", "John Smith", 29.99)
book2 = book("data structures", " Jane Doe", 45.50)

book1.display_details()
book2.display_details()
