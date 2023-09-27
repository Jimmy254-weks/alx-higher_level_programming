class Node:
    """This class represents a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node with data and an optional next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the Node, ensuring it's an integer."""
        if not isinstance(value, int):
            raise TypeError("Data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get or set the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node of the Node, ensuring it's a Node object or None."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("Next node must be a Node object or None")
        self.__next_node = value


class SinglyLinkedList:
    """This class represents a singly-linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList with an empty head."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the SinglyLinkedList at the correct ordered numerical position.

        Args:
            value (int): The value to insert.
        """
        new = Node(value)

        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(values)
