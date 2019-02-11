'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
'''

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        strslen=len(strs)
        if strslen==0:
            return ""
        elif strslen==1:
            return strs[0]

        short=min(strs, key=len)
        strs.remove(short)
        for s in strs:
            shortlen=len(short)
            for i in range(shortlen):
                if short[i]==s[i]:
                    continue
                else:
                    if i==0:
                        return ""
                    else:
                        short=short[:i]
                        break
            return short

ss=["acc","aaa","aaba"]
s=Solution().longestCommonPrefix(ss)
print(s)

