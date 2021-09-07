# Doubly Linked List:

class Node:

  def __init__(self, data, prev_node = None, next_node = None):
    self.data = data
    self.prev_node = prev_node
    self.next_node = next_node

  def __repr__(self) -> str:
    return "<Node data: %s>" % self.data

# end to class Node

class DoublyLinkedList:

  def __init__(self) -> None:
    self.head = None
    self.__count = 0

  def is_empty(self):
    return self.head is None

  def __len__(self):
    return self.__count
