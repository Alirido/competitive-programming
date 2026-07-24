class MinStack:
  def __init__(self):
    self.stack = []
    self.minStack = []

  def push(self, value: int) -> None:
    self.stack.append(value)
    m = value if not self.minStack else min(value, self.minStack[-1])
    self.minStack.append(m)

  def pop(self) -> None:
    self.stack.pop()
    self.minStack.pop()

  def top(self) -> int:
    return self.stack[-1]      

  def getMin(self) -> int:
    return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()