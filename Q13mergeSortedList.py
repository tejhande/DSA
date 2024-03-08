class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Merge two sorted linked lists
def merge_sorted_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    current.next = l1 or l2
    
    return dummy.next

# Utility function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Test the function
# Creating two sorted linked lists
l1_node1 = ListNode(1)
l1_node2 = ListNode(3)
l1_node3 = ListNode(5)
l1_node1.next = l1_node2
l1_node2.next = l1_node3

l2_node1 = ListNode(2)
l2_node2 = ListNode(4)
l2_node3 = ListNode(6)
l2_node1.next = l2_node2
l2_node2.next = l2_node3

print("List 1:")
print_linked_list(l1_node1)
print("List 2:")
print_linked_list(l2_node1)

merged_head = merge_sorted_lists(l1_node1, l2_node1)

print("Merged List:")
print_linked_list(merged_head)
