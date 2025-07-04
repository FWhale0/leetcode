#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        sc = ""
        p = 0
        while p < len(s):
            sc += s[p]
            p += (numRows - 1) * 2
        
        for i in range(1, numRows-1):
            p = i
            while p < len(s):
                sc += s[p]
                if p + (numRows - 1 - i) * 2 < len(s):
                    sc += s[p + (numRows - 1 - i) * 2]
                p += (numRows - 1) * 2
            
        p = numRows - 1
        while p < len(s):
            sc += s[p]
            p += (numRows - 1) * 2

        return sc
        
# @lc code=end

