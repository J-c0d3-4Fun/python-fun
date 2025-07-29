class Node:
    """
    An object for storing a single node of a linked list.
    Models tow attributes - data and teh link to the next node in the list"""
    data = None #instance variablw of the class Node
    next_node = None

    def __init__(self,data): # constructor 
        self.data = data

    def __repr__(self):
        
        return "<NODE data: %s>" % self.data
    

class LinkedList:
    """
    Singly linked list
    """
    def __init__(self):
        self.head = None

    def is_empty(self): # Making a method of the LinkedList Class
        return self.head == None
    
    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) Time
        """
        current = self.head
        count = 0

        while current:
            count += 1  # += increments by value
            current = current.next_node

        return count
    
    def add(self, data):
        """
        Adds a new Node containing data at the head of the list
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Returns the node or `None` if not found
        Takes O(n) time
        """

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion takes O(1) time but finding thr node at teh insetion point takes O(n) time.
        
        Takes overall O(n) time
        """
        if index == 0:
            self.add(data) # calling the add module, this adds data to the Head of the list

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                postion -= 1
        
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes node containing data that matches the key
        Returns the node or None if the key doesn't exist
        Takes O(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and not found: # looks for if the current is None (has a value = True, no value equals False) and if found is False
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current


    def node_at_index(self, index):
        if index == 0:
            return self.head
        
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1
            return current


    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return  '-> '.join(nodes)
