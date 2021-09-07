# Singly Linked List:

class Node:

  """
    An object for storing a single node in a linked list

    Attributes:
        data: Data stored in node
        next_node: Reference to next node in linked list
    """

  def __init__(self, data, next_node = None):
    self.data = data
    self.next_node = next_node
    
  def __repr__(self):
    return "<Node data: %s>" % self.data
    
# end to Class Node.

class SinglyLinkedList:

  """
    Linear data structure that stores values in nodes. The list maintains a reference to the first node, also called head. Each node points to the next node in the list

    Attributes:
        head: The head node of the list
    """

  def __init__(self):
    self.head = None
    self.__count = 0

    # Maintaining a count attribute allows for len() # to be implemented in constant time.

  def is_empty(self):

    """
    Determines if the linked list is empty Takes O(1) time
    """

    return self.head is None

  def __len__(self):

    """
        Returns the length of the linked list Takes O(1) time
    """

    return self.__count