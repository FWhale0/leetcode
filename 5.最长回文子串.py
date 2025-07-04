#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pal = ""

        i = 0
        while i < len(s):
            pal = s[i]
            i_ = i + 1
            while i_ < len(s) and s[i_] == s[i]:
                pal += s[i_]
                i_ += 1
            p1, p2 = i-1, i_
            while p1 >= 0 and p2 < len(s) and s[p1] == s[p2]:
                pal = s[p1] + pal + s[p2]
                p1, p2 = p1-1, p2+1
            max_pal = pal if len(pal) > len(max_pal) else max_pal
            i = i_

        return max_pal
        
# @lc code=end

