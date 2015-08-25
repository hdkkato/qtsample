
# def search(node, key):
#     while node:
#         if key in node.data: return True
#         else: node = node.children
#     return False

def search(node, key):
    if key in node: return True
    return False

def map2list(func, node):
    if isinstance(node, list):
        return list(map(lambda x: map2node(func, x), node))
    else:
        return func(node)

def map2node(func, node):
    if isinstance(node, Node):
        if not node.children:
            return 'leaf'
        return list(map(lambda x: map2node(func, x), node.children))
    else:
        return func(node)


class Node:
    """docstring for Node"""
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.children = []

    def addChild(self, data):
        node = Node(data, self)
        self.children.append(node)
        return node

    def row(self):
        if self.parent:
            return self.parent.children.index(self)
        else:
            return 0


class Tree:
    """docstring for Tree"""
    def __init__(self):
        self.root = Node('Root')
        current = self.root.addChild(['Node'])
        current.addChild(['Sub Node']).addChild(['Leaf'])
        current.addChild(['Sub Node2'])
        self.root.addChild(['Leaf'])




def main():
    tree = Tree()
    search_node = lambda x: search(x, key='Leaf')
    res = map2node(search_node, tree.root)

    # my_list = ['Root', ['Tree', 'Tree2', ['Leaf']], ['Node'], [['Leaf']]]
    # my_list = [1,[21,22],3,[41,[421,422],43,44],5]
    # search_node = lambda x: search(x, key='Leaf')
    # res = map2node(search_node, my_list)
    print(res)

if __name__ == '__main__':
    main()