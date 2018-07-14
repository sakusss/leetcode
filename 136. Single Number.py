class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in nums:
            
            if i in dict:
                
                dict[i] += 1
                
            else:
                
                dict[i] = 1
        
        return list(dict.keys())[list(dict.values()).index(1)]
        
        ## 自己想的方法，使用哈希表，难点在于从value值去找key值，但是用了额外的空间，时间复杂度是线性。
        
        -----位运算
        方法：两个相同的数字异或得0，一个数字和0异或结果是它本身。

使用异或运算

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from functools import reduce 
        return reduce(lambda a, b: a ^ b, nums)
        # return reduce(lambda a,b :a^b, nums)
        
        ## reduce 在python3中没有内置函数了
        ## 知识点两个 异或运算和lambda函数
        
