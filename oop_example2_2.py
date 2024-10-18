class FileSystemNode:
    def __init__(self, name, is_dir = False, parent = None):
        self.name = name
        self.is_dir = is_dir
        self.children = {} if is_dir else None
        self.content = "" if not is_dir else None
        self.parent = parent

class FileSystem:
    def __init__(self):
        self.root = FileSystemNode("/", True)
        self.curr_dir = self.root

    def mkdir(self, name):
        if name in self.curr_dir.children:
            print(f"mkdir: dir: {name} already exists")
        else:
            self.curr_dir.children[name] = FileSystemNode(name, True, self.curr_dir)

    def touch(self, name):
        if name in self.curr_dir.children:
            print(f"touch: file: {name} already exists")
        else:
            self.curr_dir.children[name] = FileSystemNode(name, False, self.curr_dir)

    def cd(self, path):
        if path == "/":
            self.curr_dir = self.root
        elif path == "..":
            if self.curr_dir.parent:
                self.curr_dir = self.curr_dir.parent
            else:
                print(f"cd: current dir has no parent")
        elif path in self.curr_dir.children:
            if self.curr_dir.children[path].is_dir:
                self.curr_dir = self.curr_dir.children[path]
            else: 
                print("Not a dir")
        else:
            print("No child path found")

    def ls(self):
        for name in self.curr_dir.children:
            print(name)
    
    def rm(self, name, recurisve=False):
        if name not in self.curr_dir.children:
            print(f"rm: {name} no file or dir in children")
            return
        
        node = self.curr_dir.children[name]
        if node.is_dir and not recurisve:
            print(f"rm: {name}: is a directory")
            return
        
        if node.is_dir and recurisve:
            self._rm_recursive(node)

        del self.curr_dir.children[name]
    
    def _rm_recurisve(self, node):
        for child_name, child_node in list(node.children.items()):
            if child_node.is_dir:
                self._rm_recurisve(child_node)
            del node.children[child_name]

    def pwd(self):
        path = []
        current = self.curr_dir
        while current != self.root:
            path.append(current.name)
            current = current.parent

        path.append("/")
        return "/" + "/".join(reversed(path[:-1]))
    
    