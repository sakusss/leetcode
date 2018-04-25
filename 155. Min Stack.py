
### 实现一个栈，带有出栈（pop），入栈（push），取最小元素（getMin）三个方法。要保证这三个方法的时间复杂度都是O(1)。
### 需要维护一个最小栈
### 开辟两个栈，一个栈是普通的栈，一个栈用来维护最小值的队列。
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
        if len(self.stack2) == 0 or x <= self.stack2[-1]:
            self.stack2.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        top = self.stack1[-1]
        self.stack1.pop()
        if top == self.stack2[-1]:
            self.stack2.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack1[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
