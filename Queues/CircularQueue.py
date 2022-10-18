class MyCircularDeque:
    def __init__(self, k: int):
        self.queue = []
        self.size = k

    def insertFront(self, value: int) -> bool:
        if len(self.queue) < self.size:
            self.queue.insert(0, value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.queue) < self.size:
            self.queue.insert(self.size-1, value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if len(self.queue) != 0:
            self.queue.pop(0)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if len(self.queue) != 0:
            self.queue.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        return self.queue[0] if len(self.queue) != 0 else -1

    def getRear(self) -> int:
        return self.queue[-1] if len(self.queue) != 0 else -1

    def isEmpty(self) -> bool:
        return True if len(self.queue) == 0 else False

    def isFull(self) -> bool:
        return True if len(self.queue) >= self.size else False
