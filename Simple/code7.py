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

    def fanwei(self,x):
        if -2**31<=x<=2**31-1:
            return True
        else:
            return False

    def get_num(self,x):
        a=list(str(x))
        num=0
        for i in range(len(a)-1,-1,-1):
            num=num+(10**i)*int(a[i])
        return num

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            x=abs(x)
            num=-self.get_num(x)
            if self.fanwei(num):
                return num
            else:
                return 0
        elif x==0:
            return 0
        else:
            num=self.get_num(x)
            if self.fanwei(num):
                return num
            else:
                return 0



s=Solution().reverse(120)
print(s)