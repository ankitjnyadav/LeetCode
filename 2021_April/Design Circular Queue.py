class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = []
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.queue.append(value)
        # print(self.queue)
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.queue.pop(0)
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """

        return -1 if self.isEmpty() else self.queue[0]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """

        return -1 if self.isEmpty() else self.queue[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return len(self.queue) <= 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return len(self.queue) == self.capacity
