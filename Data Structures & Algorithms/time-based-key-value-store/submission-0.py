class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.keys[key]:
            return ""

        values = self.keys[key]

        for i in range(len(values) - 1, -1, -1):

            if values[i][0] <= timestamp:
                return values[i][1]

        return ""

