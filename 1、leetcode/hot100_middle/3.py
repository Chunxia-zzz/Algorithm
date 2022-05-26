'''
无重复字符的最长子串
解法：
1、滑动窗口
步骤一、定义空集合，定义左右指针来确定窗口



给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        lookup = set()
        n = len(s)
        right, ans = 0, 0
        #这里i是左指针，即滑动窗口左侧
        for i in range(n):
            #i是0的情况下，窗口左侧在字符串左边界，无法移除字符需要处理。其他情况都是移除上一个字符
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                lookup.remove(s[i - 1])
            while right < n and s[right] not in lookup:
                # 不断地移动右指针
                lookup.add(s[right])
                right += 1
            ans = max(ans, right - i)
        return ans


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("pwwkew"))
