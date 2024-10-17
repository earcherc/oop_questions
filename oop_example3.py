# Handle operations of a large public library with multiple branches

# Reqs
# Manage books
# Handle library members
# Process checkouts, returns, reservations
# Manage multiple library branches w dif inventories
# Implement a search function for items across all branches
# Track item availability and due dates
# Generate reports for popular items, overdue items, member activity

# Ok so it seems like we definitely will have a few classes
# I'm wondering how we should handle inventories, because we need a total store but also a locality
# I guess the main inventory should be centralised, we just use a attribute to discern where its from

# What functions will a library manage
# Adding a branch
# Inventory management
    # Moving book between branches
    # Adding book
    # Removing book
# Generating reports

class Library:
    def __init__(self, name):
        self.name = name
        self.branches = [] 
        self.inventory = {}
        self.members = {} 

# What functions will a branch manage
# Member signs up through a branch
# Inventory management
    # Book checkout
    # Book return

class Branch:
    def __init__(self, id, name, parent):
        self.id = id
        self.name = name
        self.library = parent

# What functions will a member conduct
# Or is it more of a data store?

class Member:
    counter = 0
    
    def __init__(self, name, branch):
        Member.counter += 1
        self.id = Member.counter
        self.name = name
        self.branch = branch
        self.history = {}
        self.checkouts = {}

    def checkout(self, book_id):
        pass

class Book:
    counter = 0

    def __init__(self, title, branch, *authors):
        Book.counter += 1
        self.id = Book.counter
        self.title = title
        self.branch = branch
        self.authors = list(authors)
        self.available = True
        self.borrower = None
