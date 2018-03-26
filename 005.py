class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        def ispalin(a):
            i=0
            while i < (len(a)+1)/2:
                if a[i]==a[len(a)-i-1]:
                    i += 1
                else:
                    return False
            return True
                    
        if len(s)==1:
            return s
        else:
            a=[]  
            max=0
        
            for i in range(len(s)):
                for j in range(len(s)+1):
                    if i<=j and ispalin(s[i:j]):
                        if j-i+1 >= max:                  
                            a.append(s[i:j])
                            max = j-i+1
            return a[-1]
                
