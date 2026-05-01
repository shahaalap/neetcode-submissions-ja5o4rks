class MinStack:

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        minimum  = val
        if len(self.data) > 0:
            minimum = min(minimum, self.data[-1][1])

        self.data.append((val, minimum))

    def pop(self) -> None:
        self.data.pop()


    def top(self) -> int:
        return self.data[-1][0]
        

    def getMin(self) -> int:
        return self.data[-1][1]
