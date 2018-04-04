class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max=0
        left = 0;right =len(height)-1
        while  left < right:
            water = min(height[left],height[right])*(right-left)
            if water > max: max=water
            if height[left] <= height[right]:
                left +=1
            else:
                right -=1
        return max
                
解题思路：我们从第一个高度为起始容器壁，那么我们直接以最后一个高度为终止壁，
如果a1 <= an，那么以a1为起始的容器最大是a1 * （n - 1），以a1为容器壁的最大容器计算出来的。
那么以a1为壁的所有情况不需要再考虑，接着考虑a2的；同理，如果a1 > an,an不再考虑，
考虑an-1，这有点类似"夹逼定理"。比较ai和aj（i<j）如果ai <= aj，i++；否者j ++直到i == j。这个算法的时间复杂度是（O（n））。
