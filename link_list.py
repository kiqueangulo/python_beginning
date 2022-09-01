class Node:
    def __init__(self, data = None, reference = None):
        self.data = data
        self.reference = reference

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def print_linked_list(self):
        if self.head is None:
            print('The linked list is empty')
        else:
            current_node = self.head

            while current_node is not None:
                print(current_node.data, end = ' ')
                current_node = current_node.reference
            print()
    
    def add_to_start(self, data):
        new_node = Node(data)
        new_node.reference = self.head
        self.head = new_node
    
    def add_to_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head

        while last_node.reference is not None:
            last_node = last_node.reference
        
        last_node.reference = new_node
    
    def add_after(self, data, ref):
        if self.head is None:
            print('The linked list is empty.\n Use either add_to_start or add_to_end methods instead.')
            return
        
        new_node = Node(data)
        prev_node = self.head
        current_node = prev_node.reference

        while prev_node.data != ref:
            if current_node is None:
                print(f'{ref} is not an element of this the list')
                return

            prev_node = prev_node.reference
            current_node = current_node.reference
        
        prev_node.reference = new_node
        new_node.reference = current_node
    
    def remove(self, ref):
        if self.head is None:
            print('Nothing to remove, the linked list is empty.')
            return
        
        prev_node = None
        current_node = self.head

        while current_node.data != ref:
            prev_node = current_node
            current_node = current_node.reference

            if current_node is None:
                print(f'{ref} is not an element of this the list')
                return
        
        prev_node.reference = current_node.reference
        


node1 = Node()

linked_list1 = LinkedList()

linked_list1.add_to_start(82)
linked_list1.add_to_start(15)

linked_list1.add_to_end(12)
linked_list1.add_to_end(19)

linked_list1.add_after(5, 15)
linked_list1.add_after(6, 17)

linked_list1.print_linked_list()

linked_list1.remove(23)
linked_list1.remove(82)

linked_list1.print_linked_list()
