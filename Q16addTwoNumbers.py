class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Add two numbers represented by linked lists
def add_two_numbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        sum_val = carry
        if l1:
            sum_val += l1.val
            l1 = l1.next
        if l2:
            sum_val += l2.val
            l2 = l2.next
        
        carry = sum_val // 10
        sum_val %= 10
        
        current.next = ListNode(sum_val)
        current = current.next
    
    return dummy.next

# Utility function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Test the function
# Creating two linked lists representing numbers
num1_node1 = ListNode(2)
num1_node2 = ListNode(4)
num1_node3 = ListNode(3)
num1_node1.next = num1_node2
num1_node2.next = num1_node3

num2_node1 = ListNode(5)
num2_node2 = ListNode(6)
num2_node3 = ListNode(4)
num2_node1.next = num2_node2
num2_node2.next = num2_node3

print("Number 1:")
print_linked_list(num1_node1)
print("Number 2:")
print_linked_list(num2_node1)

result_head = add_two_numbers(num1_node1, num2_node1)

print("Sum of the two numbers:")
print_linked_list(result_head)
