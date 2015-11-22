class BSTNode:
    """
    Implementation for the node of Binary Search Tree
    """
    def __init__(self, key, value, parent=None, left=None, right=None):
        """
        The class constructor

        @param key: the key of the node
        @param value: the value of the node
        @param parent: pointer to the parent node
        @param left: pointer to the left child
        @param right: pointer to the right child

        @return: null
        """
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()
    

class MyBST:
    """
    Implementation for Binary Search Trees
    """
    def __init__(self):
        self.root = None

    def find_recursive(self, node, key):
        """
        Search the key from node, recursively

        @param node: a BST Node
        @param key: a key value
        @return: the node with the key; Null if the key is not found
        """
        if None == node or key == node.key:
            return node
        elif key < node.key:
            return self.find_recursive(node.left, key)
        else:
            return self.find_recursive(node.right, key)

    def find_iterative(self, node, key):
        """
        Search the key from node, iteratively

        @param node: a BST Node
        @param key: a key value
        @return: the node with the key; Null if the key is not found
        """
        current_node = node
        while current_node:
            if key == current_node.key:
                return current_node
            
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def search(self, key):
        """
        Find the node with the key

        @param key: the target key
        @return: the node with the key; null if the key is not found
        """
        return self.find_iterative(self.root, key)


    def insert(self, key, value):
        """
        Insert the (key, value) to the BST

        @param key: the key to insert
        @param value: the value to insert
        @return: True if insert successfully; otherwise return False
        """
        if None == self.root:
            self.root = BSTNode(key, value)
            return True

        current_node = self.root
        while current_node:
            if key == current_node.key:
                print "The key does exist!"
                return False
            elif key < current_node.key:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = BSTNode(key, value, current_node)
                    return True
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = BSTNode(key, value, current_node)
                    return True

    def replace_node(self, node, new_node):
        """
        Replace the node by new_node, update in its parent node

        @param node: node to replace
        @param new_node: the new node
        @return: null
        """
        # special case: replace the root
        if node == self.root:
            self.root = new_node
            return
        parent = node.parent
        if parent.left and parent.left == node:
            parent.left = new_node
        elif parent.right and parent.right == node:
            parent.right = new_node
        else:
            print "Incorrect parent-children relation!"
            raise RuntimeError

    def remove_node(self, node):
        """
        Remove the node from the tree

        @param node: the node to remove
        @return: null
        """
        if node.left and node.right:    # the node has two children
            # Find its in-order successor
            successor = node.right
            while successor.left:
                successor = successor.left
            # Copy the node
            node.key = successor.key
            node.value = successor.value
            # Remove the successor
            self.remove_node(successor)
        elif node.left:     # the node only has a left child
            self.replace_node(node, node.left)
        elif node.right:    # the node only has a right child
            self.replace_node(node, node.right)
        else:               # the node has no children
            self.replace_node(node, None)

    def delete(self, key):
        """
        Delete the node with the key

        @param key: a key value
        @return: True if the node is deleted successfully; otherwise return False
        """
        node = self.search(key)
        if node:
            self.remove_node(node)

'''
def traverse_in_order(node, callback_function):
    """
    Function to traverse the tree from the node, in a recursive way.
    For each visiting node, we call the callback_function on the node.

    @param node: the BST node
    @param callback_function: the callback function for visiting the node
    @return: null
    """
    if node is None:
        return
    traverse_in_order(node.left, callback_function)
    callback_function(node)
    traverse_in_order(node.right, callback_function)


def sort_by_BST(values):
    """
    Sort the given list of values using BST

    @param values: a list of values
    @return: a sorted list
    """
    result = []
    bst = MyBST()
    # Insert the values as key into the BST
    for v in values:
        bst.insert(v,0)
    # Traverse the bst with the callback function that inserts the key of each node into result
    traverse_in_order(bst.root, lambda n: result.append(n.key))
    return result

sort_by_BST(10)
'''
inputs = [];
binaryTree = MyBST()

while(True):
    userInputs = raw_input()
    if(userInputs == "END"):
        break;
    inputs.append(userInputs)
    
for i in range(len(inputs)):
    binaryTree.insert(i+1,inputs[i]);
    
print binaryTree.search(4);
    
