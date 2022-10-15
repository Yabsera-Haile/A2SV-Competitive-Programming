class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if len(self.queue) != 0:
            result = self.queue.pop(0)
        return result

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return True if not self.queue else False
