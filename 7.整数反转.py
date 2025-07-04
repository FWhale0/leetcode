#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x > -10 and x < 10:
            return x

        sx = list(str(x))
        neg = False
        if sx[0] == '-':
            neg = True
            sx = sx[1:]

        sx.reverse()
        sx_rev = ''.join(sx)
        if len(sx_rev) > 10 or (len(sx_rev) == 10 and neg and sx_rev > "2147483648") or (len(sx_rev) == 10 and not neg and sx_rev > "2147483647"):
            sx_rev = '0'
        if neg:
            sx_rev = '-' + sx_rev

        x_rev = int(sx_rev)
        if x_rev < -2e31 or x_rev > 2e31 - 1:
            x_rev = 0
        print(x_rev, 2e31-1)
        return int(sx_rev)
# @lc code=end

