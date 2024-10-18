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

# What functions will a member conduct
# Show overdue books
# Show rented books
# Extend rental
# Show history
# Generate recommendations

class Member:
    counter = 0
    
    def __init__(self, name, branch):
        self.id = Member.counter
        Member.counter += 1
        self.name = name
        self.branch = branch
        self.history = {}
        self.checkouts = {}

    def checkout(self, book_id):
        pass

# What functions will a book perform
# Show active page
# Turn page

class Book:
    counter = 0

    def __init__(self, title, branch, *authors):
        self.id = Book.counter
        Book.counter += 1
        self.title = title
        self.branch = branch
        self.authors = list(authors)
        self.available = True
        self.borrower = None

# What functions will a library manage
# Adding a branch
# Inventory management
    # Moving book between branches
    # Adding book
    # Removing book
# Generating reports

class Library:
    def __init__(self, name: str):
        self.name = name
        self.branches = [] 
        self.inventory = {}
        self.members = {} 
    
    def add_branch(self, name: str):
        branch: Branch = Branch(name, self)
        self.branches.append(branch)
        return branch.id
    
    def list_branches(self):
        for branch in self.branches:
            print(branch, end="\n")

    def add_book(self, book: Book):
        if book.id in self.inventory:
            print(f"Book: {book.title} is already in the inventory")
            return
        
        self.inventory[book.id] = book

    def remove_book(self, id):
        if id not in self.inventory:
            print(f"Book: {self.inventory[id].title} is not in the inventory")
            return


# What functions will a branch manage
# Member signs up through a branch
# Inventory management
    # Book checkout
    # Book return
# Generate overdue list
    # Harass member

class Branch:
    count = 0

    def __init__(self, name, parent):
        self.id = Branch.count
        Branch.count += 1
        self.name = name
        self.library = parent
