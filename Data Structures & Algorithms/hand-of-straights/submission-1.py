class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)
        sortedCounts = dict(sorted(counts.items()))

        for i in range(len(hand) // groupSize):
            firstkey = None
            for key in sortedCounts:
                if sortedCounts[key] > 0:
                    firstkey = key
                    break

            if firstkey is None:
                return False

            for key in range(key, key + groupSize):
                if key not in sortedCounts:
                    return False

                if sortedCounts[key] == 0:
                    return False
                else:
                    sortedCounts[key] -= 1

        return True
                
