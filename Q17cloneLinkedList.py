class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

# Clone a linked list with next and random pointer
def clone_linked_list(head):
    if not head:
        return None
    
    # Step 1: Create a copy of each node and insert it next to the original node
    current = head
    while current:
        copy_node = Node(current.val)
        copy_node.next = current.next
        current.next = copy_node
        current = copy_node.next
    
    # Step 2: Set random pointers for the copied nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next
    
    # Step 3: Separate the original and copied linked lists
    original_head = head
    copied_head = head.next
    copied_current = copied_head
    
    while original_head:
        original_head.next = original_head.next.next
        original_head = original_head.next
        
        if copied_current.next:
            copied_current.next = copied_current.next.next
            copied_current = copied_current.next
    
    return copied_head

# Utility function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        random_val = current.random.val if current.random else None
        print(f"({current.val}, {random_val})", end=" -> ")
        current = current.next
    print("None")

# Test the function
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node1.random = node3
node2.random = node5
node4.random = node2

print("Original linked list:")
print_linked_list(node1)

cloned_head = clone_linked_list(node1)

print("Cloned linked list:")
print_linked_list(cloned_head)
