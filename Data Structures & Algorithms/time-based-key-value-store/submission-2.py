class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not len(self.data[key]):
            return ""

        array = self.data[key]
        if timestamp < array[0][0]:
            return ""

        i , j = 0, len(array) - 1

        while i <= j:
            mid = i + (j -  i)//2

            if array[mid][0] == timestamp:
                return array[mid][1]
            elif array[mid][0] < timestamp:
                i = mid + 1
            else:
                j = mid - 1
        
        return array[i - 1][1]
