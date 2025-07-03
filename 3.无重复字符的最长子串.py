#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        p1, p2 = 0, 1
        max_length = 1
        letters = set(s[p1])
        while p2 < len(s):
            if s[p2] in letters:
                max_length = max(max_length, len(letters))
                while s[p1] != s[p2]:
                    letters.remove(s[p1])
                    p1 += 1
                p1 += 1
            letters.add(s[p2])
            p2 += 1

        return max(max_length, len(letters))
# @lc code=end

