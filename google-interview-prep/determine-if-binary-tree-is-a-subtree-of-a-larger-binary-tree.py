'''''''''''''''''''''''
           26
         /    \
        /      \
       10      30
      /  \
     4   15
    /
   3
'''''''''''''''''''''''

'''''''''''''''''''''''
           10
          /  \
         4   15
        /
       3
'''''''''''''''''''''''


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insertion(self, key):
        node = Node(key)

        if self.root is None:
            self.root = node
        else:
            current = self.root

            while current is not None:
                if key > current.key:
                    if current.right is None:
                        current.right = node
                        break
                    else:
                        current = current.right
                else:
                    if current.left is None:
                        current.left = node
                        break
                    else:
                        current = current.left

    def inorder_single(self, root):
        if root is not None:
            self.inorder_single(root.left)
            self.inorder_array.append(root.key)
            self.inorder_single(root.right)

    def inorder(self):
        self.inorder_array = []
        self.inorder_single(self.root)
        return self.inorder_array


def is_subtree(tree1, tree2):
    return all(elem in tree1.inorder() for elem in tree2.inorder())


if __name__ == '__main__':
    tree1 = Tree()
    tree1.insertion(26)
    tree1.insertion(10)
    tree1.insertion(4)
    tree1.insertion(3)
    tree1.insertion(15)
    tree1.insertion(30)

    tree2 = Tree()
    tree2.insertion(10)
    tree2.insertion(4)
    tree2.insertion(3)
    tree2.insertion(15)

    is_subtree(tree1, tree2)
