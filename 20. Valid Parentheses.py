class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack={')':'(',']':'[','}':'{'}
        stack_left ,stack_right = stack.values(),stack.keys()
        arr =[]
        if len(s)%2 == 1 :return False
        for c in s:
            if c in stack_left:
                arr.append(c)
            elif c in stack_right: 
                if arr and arr[-1] == stack[c]:
                    arr.pop()
                else:
                    return False
        if arr == [] :return True
        return False
                
               ## 时间复杂度和空间复杂度都是O(N)
               ## 判断括号的匹配度，现将左右分开，使用dict使其成对，如果是左括号，则入栈，如果是右括号，判断与栈顶元素是否相等
               ## 相等则出栈，不等返回错误。如果栈为空，而遇到右括号，同样返回错误
               ## 遍历完栈为空，则返回正确，否则错误
               ## 字符串长度不为偶数，直接结束，输出错误
               ## 借助栈的压入，弹出进行匹配
