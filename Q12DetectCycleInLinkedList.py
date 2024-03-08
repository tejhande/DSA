class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Detect a cycle in a linked list
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Test the function
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node1  # Creating a cycle

result = has_cycle(node1)
print(result)
