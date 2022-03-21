#linked list implementation in Python

#class for Node
class Node:
  def __init__(self,data = None,next = None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self,head=None):
    self.head = head
  
  def insert_at_beginning(self,data):
    node = Node(data,self.head)
    self.head = node
  
  def insert_at_end(self,data):
    if self.head is None:
      self.head = Node(self.head,data)
      return
    itr = self.head
    while itr:
      itr = itr.next
    itr.next = Node(data,None)
  
  def get_length(self):
    count = 0
    if self.head is None:
      return count 
    itr = self.head
    while itr:
      count += 1
      itr = itr.next
    return count
  
  def remove_at_beginning(self):
    if self.head.next is not None:
      self.head = self.head.next
  
  def remove_at_end(self):
    if self.head == None:
      return
    itr = self.head
    while itr.next.next != None:
      itr = itr.next
    itr.next = None
  
  def insert_after_value(self,data_after,data_to_insert):
    itr = self.head
    while itr.data != data_after:
      itr = itr.next
    node = Node(data_to_insert,itr.next)
    itr.next = node
  
  def search(self,data):
    itr = self.head
    while itr:
      if itr.data == data:
        return True
      itr = itr.next
    return False

  def remove_by_value(self, data):
    # Remove first node that contains data
    itr = self.head
    if itr.data == data:
      self.head = itr.next
      return
    if self.search(data):
      itr = self.head
      while itr.next.data != data:
        itr = itr.next
      itr.next = itr.next.next
    else:
      print("Value doesn't exist in the linked list")
      
  def insert_at(self,index,data):
    if index < 0 or index > self.get_length():
      raise Exception("Invalid index")
    count = 0
    itr = self.head
    while itr:
      if count == index-1:
        node = Node(data,itr.next)
        itr.next = node
        break
      itr = itr.next
      count += 1
  
  def remove_at(self,index):
    if index < 0 or index > self.get_length():
      raise Exception('Invalid index')
    if index == 0:
      self.head = self.head.next
      return
    count = 0
    itr = self.head
    while itr:
      if count == index - 1:
        itr.next = itr.next.next
        break
      
      itr = itr.next
      count += 1
 
       
