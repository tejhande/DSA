class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Detect if a linked list has a loop
def has_loop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Test the function
# Creating a linked list with a loop
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  # Creating a loop

result = has_loop(node1)
print(result)
