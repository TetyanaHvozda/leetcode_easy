# Definition for singly-linked list node.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution class that contains the hasCycle function
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


# Function to create a linked list from a list of values and add a cycle
def create_linked_list_with_cycle(values, pos):
    if not values:
        return None

    # Create the head node
    head = ListNode(values[0])
    current = head
    cycle_entry = None  # This will be the node where the cycle starts
    nodes = [head]

    # Create the rest of the linked list
    for i in range(1, len(values)):
        new_node = ListNode(values[i])
        current.next = new_node
        current = new_node
        nodes.append(new_node)

    # Create a cycle if pos is not -1
    if pos != -1:
        cycle_entry = nodes[pos]  # Node where the cycle starts
        current.next = cycle_entry  # Create the cycle

    return head


# Test case 1
values = [3, 2, 0, -4]
pos = 1  # Cycle starts at index 1
head = create_linked_list_with_cycle(values, pos)

# Create a Solution object
solution = Solution()

# Run the hasCycle function and print the result
result = solution.hasCycle(head)
print(result)