class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Find the middle of a linked list
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

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

middle_node = find_middle(node1)
print("Middle of the linked list:", middle_node.val)
