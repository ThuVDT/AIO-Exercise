class MyStack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def is_full(self):
        return len(self.stack_list) == self.capacity

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.stack_list.pop()

    def push(self, value):
        if self.is_full():
            return "Stack is full"
        else:
            return self.stack_list.append(value)

    def top(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.stack_list[-1]


stack1 = MyStack(capacity=5)

stack1.push(1)

stack1.push(2)

print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
