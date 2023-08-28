# Contest358, Q2

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        parent = None
        cur_node = head
        while cur_node:
            if cur_node.val * 2 > 9:
                parent_add_num = (cur_node.val * 2) // 10
                if parent:
                    parent.val += parent_add_num
                else:
                    parent = ListNode(parent_add_num, cur_node)
                    head = parent
                cur_node.val = (cur_node.val * 2) % 10
            else:
                cur_node.val *= 2
            parent = cur_node
            cur_node = cur_node.next

        return head


if __name__ == "__main__":
    test = Solution()
    print(test.doubleIt(head=[1, 8, 9]))
    print(test.doubleIt(head=[9, 9, 9]))
    # print(test.doubleIt(head = [9,9,9]))
