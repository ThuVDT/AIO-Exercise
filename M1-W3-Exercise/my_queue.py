class MyQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue_list = []

    def is_empty(self):
        return len(self.queue_list) == 0

    def is_full(self):
        return len(self.queue_list) == self.capacity

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue_list.pop(0)

    def enqueue(self, value):
        if self.is_full():
            return "Queue is full"
        else:
            return self.queue_list.append(value)

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue_list[0]


queue1 = MyQueue(capacity=5)

queue1.enqueue(1)

queue1.enqueue(2)

print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())
