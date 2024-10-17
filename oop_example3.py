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

class Library:
    def __init__(self, name, branches=3):
        self.name = name
        self.branches = [Branch(i, self) for i in range(branches)]    
        self.inventory = {}
        self.members = {}
    

class Branch:
    def __init__(self, id, parent):
        self.id = id
        self.library = parent

class Member:
    counter = 0
    
    def __init__(self, name):
        Member.counter += 1
        self.id = Member.counter
        self.name = name
        

class Book:
    pass


