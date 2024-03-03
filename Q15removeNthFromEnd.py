# Q14 answer = a) 3
# Twitter:-- @DSA_Python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Remove Nth node from the end of a linked list
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow = fast = dummy
    
    for _ in range(n + 1):
        fast = fast.next
        
    while fast:
        slow = slow.next
        fast = fast.next
        
    slow.next = slow.next.next
    
    return dummy.next

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
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original linked list:")
print_linked_list(node1)

n = 2
updated_head = remove_nth_from_end(node1, n)
print(f"Linked list after removing {n}th node from the end:")
print_linked_list(updated_head)

# What is the output of the following code?
# a) 1 -> 2 -> 3 -> 5 -> None
# b) 1 -> 2 -> 4 -> 5 -> None
# c) 1 -> 3 -> 4 -> 5 -> None
# d) 2 -> 3 -> 4 -> 5 -> None