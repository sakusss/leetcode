class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s==''or s[0]=='0': return 0
        n=len(s)
        res=[1 for i in range(n+1)]
        for i in range(2,n+1):
            if int(s[i-2:i])==10 or int(s[i-2:i])==20 :
                res[i]=res[i-2]
            elif 11<= int(s[i-2:i]) <=26 and s[i-1]!='0':
                res[i]= res[i-1] + res[i-2]
            elif s[i-1]!='0':
                res[i]=res[i-1]
            else:
                return 0
        
        return res[n]
        
       ##一般求‘多少’的问题我们考虑DP，时间复杂度O(N),空间复杂度O（1）
       ## 主要难度在分类上，要把全体空间完全划分，不要漏掉情况
       ##。这里可以把范围分成几个区间：
（1）00：res[i]=0（无法解析，没有可行解析方式）；
（2）10, 20：res[i]=res[i-2]（只有第二种情况成立）；
（3）11-19, 21-26：res[i]=res[i-1]+res[i-2]（两种情况都可行）；
（4）01-09, 27-99：res[i]=res[i-1]（只有第一种情况可行）；
递推式就是按照上面的规则来得到，接下来我们只要进行一遍扫描，然后依次得到维护量就可以了，算法的时间复杂度是O(n)。
空间上可以看出我们每次只需要前两位的历史信息，所以只需要维护三个变量然后迭代赋值就可以了，所以空间复杂度是O(1)。
