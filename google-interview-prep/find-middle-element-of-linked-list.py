'''
Find the middle element of a linked list

Our challenge is to now find the middle node in a linked list.
We don't initially know the length of a linked list, all we have is a single node which acts as the head of the linked list and which we can access all other nodes by traversing through each nodes "next" property.
We can continuously loop through each node until we get to a node that has a "next" property of null, which means we have reached the last node.

https://coderbyte.com/algorithm/linked-list-middle-element
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print_list(self):
        print('List:')
        current = self.root
        while current is not None:
            print(current.data, '-> ', end='')
            current = current.next

    '''
    Traverse all the list nodes and count how many elements there are in total.
    Then traverse it again this time stopping at the total/2 node.
    '''
    def get_middle_element_1(self):
        current = self.root
        length = 0

        # walk until the end of the list to find it's length
        while current is not None:
            length += 1
            current = current.next

        current = self.root
        # walk until the middle of the list length
        for i in range(1, length//2):
            current = current.next

        return current.data

    '''
    Traverse the list using two pointers:
    one that will traverse the linked list one node at a time,
    and the other pointer will traverse two nodes at a time.
    This way when the faster pointer reaches the end of the linked list,
    the slower pointer will be halfway there.
    '''
    def get_middle_element_2(self):
        fastPointer = self.root.next
        slowPointer = self.root

        # the fast pointer walks two nodes at a time and the slow just one
        while fastPointer.next is not None and fastPointer.next.next is not None:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next

        return slowPointer.data


list = LinkedList()

for x in range(1, 11):
    list.insert_at_end(x)

list.print_list()

print('\n\nMiddle list element:', list.get_middle_element_1())

print('\n\nMiddle list element:', list.get_middle_element_2())
