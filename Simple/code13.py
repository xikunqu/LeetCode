'''
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
'''

class Solution:

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        """
        sum=0
        convert={'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        for i in range(len(s)-1):
            if convert[s[i]]<convert[s[i+1]]:
                sum=sum-convert[s[i]]
            else:
                sum=sum+convert[s[i]]
        sum=sum+convert[s[-1]]
        return sum


    def intToRoman(self,x):
        """
        :type x: int
        :rtype: str

        """
        numslist=[]
        while (x>0):
            b=x%10
            numslist.append(b)
            x=x//10

        luoma=''
        for i,num in enumerate(numslist):
            if i==0:
                if num<4:
                    luoma=luoma +num*'I'
                elif num==4:
                    luoma=luoma +'VI'
                elif num==5:
                    luoma=luoma +'V'
                elif 5<num<9:
                    luoma=luoma +(num-5)*'I'+'V'
                elif num==9:
                    luoma=luoma +'XI'
            elif i==1:
                if num<4:
                    luoma=luoma +num*'X'
                elif num==4:
                    luoma=luoma +'LX'
                elif num==5:
                    luoma=luoma +'L'
                elif 5<num<9:
                    luoma=luoma +(num-5)*'X'+'L'
                elif num==9:
                    luoma=luoma +'CX'
            elif i==2:
                if num<4:
                    luoma=luoma +num*'C'
                elif num==4:
                    luoma=luoma +'DC'
                elif num==5:
                   luoma=luoma +'D'
                elif 5<num<9:
                    luoma=luoma +(num-5)*'C'+'D'
                elif num==9:
                    luoma=luoma +'MC'
            elif i==3:
                if num<=3:
                    luoma=luoma +num*'M'
                else:
                    return False
            else:
                return False
        return luoma[::-1]

