class treenode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, info):
        if info == "name":
            value = self.data[0]
        elif info == "designation":
            value = self.data[1]
        elif info == "both":
            value = self.data[0] + " " + self.data[1]
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(info)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_management_tree():
    root = treenode(("Nilpul","CEO"))
    
    cto = treenode(("Chinmay","CTO"))
    infra = treenode(("Vishwa","Infrastructure Head"))
    infra.add_child(treenode(("Dhaval", "Cloud Manager")))
    infra.add_child(treenode(("Abhijit", "App Manager")))
    cto.add_child(treenode(("Aamir","Application Head")))

    hr = treenode(("Gels","HR Head"))
    hr.add_child(treenode(("Peter", "Recruitment Manager")))
    hr.add_child(treenode(("Waqas", "Policy Manager")))

    root.add_child(cto)
    cto.add_child(infra)
    root.add_child(hr)

    return root

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy