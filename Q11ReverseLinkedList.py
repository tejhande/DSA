# Q10 answer = a) "world hello"
# Twitter:-- @DSA_Python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Reverse a linked list
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Utility function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Test the function
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

print("Original linked list:")
print_linked_list(node1)

reversed_head = reverse_linked_list(node1)

print("Reversed linked list:")
print_linked_list(reversed_head)

# What is the output of the following code?
# a) 1 -> 2 -> 3 -> None followed by 3 -> 2 -> 1 -> None
# b) 3 -> 2 -> 1 -> None followed by 1 -> 2 -> 3 -> None
# c) 1 -> 2 -> 3 -> None followed by None
# d) None followed by 3 -> 2 -> 1 -> None