class Node:
    def __init__(self, data):
        """
        Initializes a node object. Sets its data value. Sets the next pointer to None.
        """

        self.data = data
        self.next = None

    def get_data(self):
        """
        Returns the data value of node.
        """

        return self.data

    def get_next(self):
        """
        Returns the next pointer of node.
        """

        return self.next

    def set_data(self, new_data):
        """
        Sets the node's data.
        """

        self.data = new_data

    def set_next(self, new_next):
        """
        Sets the node's next pointer.
        """

        self.next = new_next


class LinkedList:
    def __init__(self):
        """
        Initializes the list with the head variable set to None and size
        variable to 0.
        """

        self.head = None
        self.size_of = 0

    def is_empty(self):
        """
        Does a boolean check on the head node. If head is None, the list is
        empty and False is returned. Otherwise, True is returned.
        """

        return self.head is None

    def add(self, data):
        """
        Adds a new node to the list. Creates a new node from the Node class. Then
        the new node is set as the head variable, and the old head variable is moved
        down one spot. Also, size variable is increased by 1.
        """

        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.size_of += 1

    def print_list(self):
        """
        Prints each node's data value as it traverses through list.
        """

        current = self.head

        while current is not None:
            print(current.get_data(), end=" ")
            current = current.get_next()

    def size(self):
        """
        Returns size of list.
        """

        return self.size_of

    def search(self, data):
        """
        Returns a boolean value based on whether or not the specified node data value
        is found or not, as it traverses through the list.
        """

        current = self.head
        found = False

        while current is not None and not found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, data):
        """
        Removes the node that is specified in the data parameter.
        """

        current = self.head
        previous = None
        found = False

        if self.search(data):
            while not found:
                if current.get_data() == data:
                    found = True
                else:
                    previous = current
                    current = current.get_next()

            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
            self.size_of -= 1
        else:
            print("List item does not exist")

    def remove_duplicates(self):
        """
        Removes any duplicate nodes that exist in an unordered fashion.
        """

        node1 = self.head
        duplicates = False

        while node1 is not None and node1.get_next() is not None:
            node2 = node1
            while node2.get_next() is not None:
                if node1.get_data() == node2.get_next().get_data():
                    node2.set_next(node2.get_next().get_next())
                    duplicates = True
                    self.size_of -= 1
                else:
                    node2 = node2.get_next()
            node1 = node1.get_next()
        if not duplicates:
            print("\nNo duplicates found")

    def clear(self):
        """
        Removes all nodes in list.
        """

        current = self.head
        next_node = None

        if self.head:
            while current is not None:
                next_node = current.get_next()
                current = None
                self.size_of -= 1
                current = next_node
