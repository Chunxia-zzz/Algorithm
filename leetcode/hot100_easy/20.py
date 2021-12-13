"""
有效的括号

解法思路：
匹配问题,我们一般使用栈
遍历字符串,我们把左括号压入栈中,当遇到右括号,和栈顶元素比较!
时间复杂度:O(n)
空间复杂度:O(n)

题目描述：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
 

示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
示例 4：

输入：s = "([)]"
输出：false
示例 5：

输入：s = "{[]}"
输出：true
 

提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成
"""


class Solution:
    def isValid(self, n: str) -> bool:
        if len(n) % 2 == 1:
            return False
        
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for i in n:
            if i in pairs:
                if not stack or stack[-1] != pairs[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        
        return not stack

if __name__ == '__main__':
    print(Solution().isValid("()[]{}"))