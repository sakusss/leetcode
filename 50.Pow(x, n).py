class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1  ## 递归的最底层
        
        if n < 0 :
            
            return 1/self.myPow(x,-n)
        
        half = self.myPow(x,n//2)
        
        if n%2 == 1:
            
            return half*half*x
        else:
            
            return half*half
        
