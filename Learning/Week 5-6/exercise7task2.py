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

    def print_tree(self, level):
        if self.get_level() < (level + 1):
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data)
            if self.children:
                for child in self.children:
                    child.print_tree(level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_global_tree():
    world = treenode("Global")
    
    india = treenode("India")

    gujarat = treenode("Gujarat")
    gujarat.add_child(treenode("Ahmedabad"))
    gujarat.add_child(treenode("Baroda"))

    karnataka = treenode("Karnataka")
    karnataka.add_child(treenode("Bangluru"))
    karnataka.add_child(treenode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)
    world.add_child(india)

    usa = treenode("USA")

    california = treenode("California")
    california.add_child(treenode("San Francisco"))
    california.add_child(treenode("Palo Alto"))
    california.add_child(treenode("Mountain View"))

    newjersey = treenode("New Jersey")
    newjersey.add_child(treenode("Princeton"))
    newjersey.add_child(treenode("Trenton"))

    usa.add_child(california)
    usa.add_child(newjersey)
    world.add_child(usa)

    return world

if __name__ == '__main__':
    root_node = build_global_tree()
    root_node.print_tree(1)
    root_node.print_tree(2)
    root_node.print_tree(3)