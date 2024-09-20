# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        pass


def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "/n")
        node = node.next


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


if __name__ == "__main__":
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])

    solution = Solution()
    merged_list = solution.mergeTwoLists(list1, list2)

    print("Merged Linked List:")
    print_list(merged_list)
