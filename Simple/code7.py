'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2 31,  2 31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

'''

class Solution:

    def get_num(self,x):
        a=str(x)
        num=a[::-1]
        return int(num)

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            x=abs(x)
            num=-self.get_num(x)
        else:
            num=self.get_num(x)

        if  -2**31<=num<=2**31-1:
            return num
        else:
            return 0



s=Solution().reverse(-120)
print(s)
