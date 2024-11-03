# Definition for singly linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution class with a method to reverse the linked list.
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


# Helper function to create a linked list from a list of values.
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Helper function to print the linked list.
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# Test the reverseList function
if __name__ == "__main__":
    # Create a linked list from a list of values
    values = [1, 2, 3, 4, 5]
    head = create_linked_list(values)

    print("Original Linked List:")
    print_linked_list(head)

    # Reverse the linked list
    solution = Solution()
    reversed_head = solution.reverseList(head)

    print("Reversed Linked List:")
    print_linked_list(reversed_head)
