class Node:
    def __init__(self, value: object):
        self._value: object = value
        self._next: None | Node = None

    def value(self):
        return self._value

    def next(self):
        return self._next

# List of nodes
class LinkedList:
    def __init__(self, values:list[object]=[]):
        self._head: None | Node = None
        self._count: int = 0

        for v in values:
            self.push(v)

    def __len__(self):
        # Return the number of nodes in the list
        return self._count
    
    def __iter__(self):
        # Generator function
        node = self._head
        while node is not None:
            yield node.value()
            node = node.next()

    def head(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value: object):
        # If the head is None, then make the new node the head
        if not self._head:
            self._head = Node(value)
        # If there is a head, then make the new node the head and the old head the next node
        else:
            new_node = Node(value)
            new_node._next = self._head
            self._head = new_node
        # Increment the count
        self._count += 1

    def pop(self):
        # If the head is None, the list is empty
        if not self._head:
            raise EmptyListException("The list is empty.")
        # Set the head to the next node
        else:
            node = self._head
            self._head = node.next()
        # Decrement the count
        self._count -= 1

        return node.value()

    def reversed(self):
        # Type casting self to list gives a list of values in reverse order due to LIFO, then type cast back to LinkedList
        return LinkedList(list(self))


class EmptyListException(Exception):
    """Exception raised when list is empty.

    message (str) - explanation of the error
    """
    def __init__(self, message):
        self.message = message
