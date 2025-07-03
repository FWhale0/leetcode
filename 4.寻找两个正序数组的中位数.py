#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if nums1 == []:
            if len(nums2) % 2 == 1:
                return nums2[int((len(nums2)-1)/2)]
            else:
                return (nums2[int(len(nums2)/2-1)] + nums2[int(len(nums2)/2)]) / 2
        if nums2 == []:
            if len(nums1) % 2 == 1:
                return nums1[int((len(nums1)-1)/2)]
            else:
                return (nums1[int(len(nums1)/2-1)] + nums1[int(len(nums1)/2)]) / 2
            

        mid_loc = (len(nums1) + len(nums2) + 1) / 2
        mean = True if mid_loc % 1 > 0 else False
        p1 = p2 = -1
        mid_num = min(nums1[0], nums2[0])
        while p1 + p2 + 3 <= mid_loc:
            if p2 >= len(nums2)-1 or (p1 < len(nums1)-1 and nums1[p1+1] <= nums2[p2+1]):
                p1 += 1
                mid_num = nums1[p1]
            else:
                p2 += 1
                mid_num = nums2[p2]
        if mean:
            if p2 >= len(nums2)-1 or (p1 < len(nums1)-1 and nums1[p1+1] <= nums2[p2+1]):
                return (mid_num + nums1[p1+1]) / 2
            else:
                return (mid_num + nums2[p2+1]) / 2
        else:
            return mid_num

# @lc code=end

