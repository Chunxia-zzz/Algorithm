"""
有效的括号
思路：
匹配问题,我们一般使用栈/list
遍历字符串,我们把左括号压入栈中,当遇到右括号,和栈顶元素比较!
时间复杂度:O(n)
空间复杂度:O(n)



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
#数据结构栈，其实用到的是python中的list。append方法在列表末尾加元素，pop方法在列表末尾移除元素，
# list[-1]取的是list最末尾的元素

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for i in s :
            if i not in pairs:
                stack.append(i)
            if i in pairs:
                if not stack or stack[-1] != pairs[i]:
                # or not 语法错误，需要将not stack条件放在前面判断
                # if stack[-1]!=pairs[i] or not stack:
                    return False
                else:
                    stack.pop()
        #not+空列表 = True            
        return not stack     

if __name__ == '__main__':
    print(Solution().isValid("()[]{}"))
