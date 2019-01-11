class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def add(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.size += 1

    def print_list(self):
        current = self.head

        while current is not None:
            print(current.get_data(), end=" ")
            current = current.get_next()

    def size_of(self):
        return self.size

    def search(self, data):
        current = self.head
        found = False

        while current is not None and not found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, data):
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
            self.size -= 1
        else:
            print("List item does not exist")

    def remove_duplicates(self):
        node1 = self.head
        duplicates = False

        while node1 is not None and node1.get_next() is not None:
            node2 = node1
            while node2.get_next() is not None:
                if node1.get_data() == node2.get_next().get_data():
                    node2.set_next(node2.get_next().get_next())
                    duplicates = True
                else:
                    node2 = node2.get_next()
            node1 = node1.get_next()
        if duplicates is False:
            print("\nNo duplicates found")
