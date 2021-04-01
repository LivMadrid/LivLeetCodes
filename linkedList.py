# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next 

class Solution:
    def reverse_list(self, head: ListNode):
    #start with the head 
        new_list = []
        current = head 

        while current is not None: 
            new_list.append(current.val) 
            current = current.next 

        reverse_head = None
        current = None

        for val in reversed(new_list):
            if current == None:
              current = ListNode(val)
              reverse_head = current
            else:
              node = ListNode(val)
              current.next = node
              current = node

        return reverse_head
   
         
            
node1 = ListNode(3)
node2 = ListNode(2, node1)
node3 = ListNode(1, node2)

solution = Solution()
reverse_head = solution.reverse_list(node3)
# while reverse_head is not None:
#   print(reverse_head.val)
#   reverse_head = reverse_head.next


# Success
# Details 
# Runtime: 40 ms, faster than 31.53% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 16.4 MB, less than 22.75% of Python3 online submissions for Reverse Linked List.
# Next challenges:
# Reverse Linked List II
# Binary Tree Upside Down
# Palindrome Linked List
# Show off your acceptance:
# Time Submitted
# Status
# Runtime
# Memory
# Language
# 04/01/2021 09:47	Accepted	40 ms	16.4 MB	python3
