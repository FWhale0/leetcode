#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for loc, num in enumerate(nums):
            if num in num_dict:
                num_dict[num].append(loc)
            else:
                num_dict[num] = [loc]
        for i in num_dict:
            if target-i in num_dict and target-i != i:
                return [num_dict[i][0], num_dict[target-i][0]]
            if target-i in num_dict and target-i == i:
                if len(num_dict[i]) == 1:
                    continue
                else:
                    return[num_dict[i][0], num_dict[target-i][1]]
# @lc code=end

