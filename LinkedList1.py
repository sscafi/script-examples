"""
Linked List Implementation

This script implements a singly linked list data structure in Python.
It provides methods for inserting elements at the beginning, end, and at a specific index,
printing the linked list, inserting multiple values, getting the length of the linked list,
and removing elements at a specific index.

🛠️ Usage:
Instantiate a LinkedList object and use its methods to manipulate the linked list.

"""

class Node:
    def __init__(self, data=None, next=None) -> None:
        """
        Node class for creating nodes of a linked list.

        Args:
        - data: Data to be stored in the node.
        - next: Reference to the next node in the linked list.
        """
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        """
        LinkedList class for implementing a singly linked list.

        Attributes:
        - head: Reference to the head node of the linked list.
        """
        self.head = None

    def insert_at_beginning(self, data):
        """
        Inserts a new node with data at the beginning of the linked list.

        Args:
        - data: Data to be stored in the new node.
        """
        node = Node(data, self.head)
        self.head = node

    def print(self):
        """
        Prints the elements of the linked list in order.
        """
        if self.head is None:
            print('Linked List is Empty')
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' -> '
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        """
        Inserts a new node with data at the end of the linked list.

        Args:
        - data: Data to be stored in the new node.
        """
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        """
        Inserts multiple values into the linked list.

        Args:
        - data_list: List of data values to be inserted into the linked list.
        """
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        """
        Returns the number of nodes in the linked list.
        
        Returns:
        - count: Number of nodes in the linked list.
        """
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        """
        Removes the node at the specified index from the linked list.

        Args:
        - index: Index of the node to be removed.
        """
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
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

    def insert_at(self, index, data):
        """
        Inserts a new node with data at the specified index in the linked list.

        Args:
        - index: Index where the new node should be inserted.
        - data: Data to be stored in the new node.
        """
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        if index == self.get_length():
            self.insert_at_end(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1

if __name__ == '__main__':
    # Example usage
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(23)
    ll.insert_at_end(69)
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    
    print("Linked List:")
    ll.print()
    
    ll.insert_at(4, "cowboys")
    print("Linked List after insertion:")
    ll.print()
   
    # Uncomment to print the length of the linked list
    # print("Length:", ll.get_length())
