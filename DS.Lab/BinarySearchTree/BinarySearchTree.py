import time


class record:
    def __init__(self,name,number):
        self.name = name
        self.number = number




class Node:
    def __init__(self, item):
        self.key = item
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:  # This happens when our tree was empty
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def search(self, k):
        x = self.root
        while x is not None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def inorder_print(self, root):
        if root is not None:
            self.inorder_print(root.left)
            print(root.key, end=" ")
            self.inorder_print(root.right)


class BinarySearchTree_number:
    def __init__(self):
        self.root = None

    def insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key.number < x.key.number:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:  # This happens when our tree was empty
            self.root = z
        elif z.key.number < y.key.number:
            y.left = z
        else:
            y.right = z

    def search(self, k):
        x = self.root
        while x is not None and k != x.key.number:
            if k < x.key.name:
                x = x.left
            else:
                x = x.right
        return x

    def inorder_print(self, root):
        if root is not None:
            self.inorder_print(root.left)
            print(root.key, end=" ")
            self.inorder_print(root.right)


if __name__ == '__main__':
    # bst = BinarySearchTree()
    # bst.insert(Node(2))
    # bst.insert(Node(5))
    # bst.insert(Node(15))
    # bst.insert(Node(12))
    # bst.insert(Node(9))
    # bst.insert(Node(17))
    # bst.insert(Node(13))
    # bst.insert(Node(19))
    # bst.insert(Node(18))
    # bst.inorder_print(bst.root)
    # print()
    #
    # print("Searching for key 15...")
    # search_result = bst.search(15)
    # if search_result is not None:
    #     print('Key 15 found!')
    # else:
    #     print('Key 15 not found!')
    #
    # print("Searching for key 18...")
    # search_result = bst.search(18)
    # if search_result is not None:
    #     print('Key 18 found!')
    # else:
    #     print('Key 18 not found!')
    #
    # print("Searching for key 3...")
    # search_result = bst.search(3)
    # if search_result is not None:
    #     print('Key 3 found!')
    # else:
    #     print('Key 3 not found!')
    #
    # print("Searching for key 5...")
    # search_result = bst.search(5)
    # if search_result is not None:
    #     print('Key 5 found!')
    # else:
    #     print('Key 5 not found!')
    #
    # print("Searching for key 7...")
    # search_result = bst.search(7)
    # if search_result is not None:
    #     print('Key 7 found!')
    # else:
    #     print('Key 7 not found!')




    DB = BinarySearchTree_number()
    try:
        with open('db.txt', 'r') as input_file:
            start = time.time()
            for line in input_file:
                string, num = line.split()
                rec = record(string,num)
                DB.insert(Node(rec))
            end = time.time()
            print(f"Time to insert to the list: {end - start}s")
    except FileNotFoundError:
        print("Failed to open the file.")

    try:
        with open('query_string.txt', 'r') as query_file:
            start = time.time()
            for line in query_file:
                string = line
                DB.search(string)
            end = time.time()
            print(f"Time to search string the list: {end - start}s")
    except FileNotFoundError:
        print("Failed to open the file.")

    try:
        with open('Not_db_string.txt', 'r') as query_file:
            start = time.time()
            for line in query_file:
                string = line
                DB.search(string)
            end = time.time()
            print(f"Time to search not in the db numbers in the list: {end - start}s")
    except FileNotFoundError:
        print("Failed to open the file.")