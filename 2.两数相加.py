#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_, l2_ = l1, l2
        forward = 0
        while True:
            sum = l1_.val + l2_.val + forward
            l1_.val = sum % 10
            forward = sum // 10
            if l1_.next is None and l2_.next is None:
                if forward:
                    l1_.next = ListNode(1)
                return l1
            if l1_.next is None and l2_.next is not None:
                l1_.next = l2_.next
                l1_ = l1_.next
                l2_ = ListNode(0)
                continue
            if l1_.next is not None and l2_.next is None:
                l1_ = l1_.next
                l2_ = ListNode(0)
                if not forward:
                    return l1
                continue
            l1_ = l1_.next
            l2_ = l2_.next
# @lc code=end

