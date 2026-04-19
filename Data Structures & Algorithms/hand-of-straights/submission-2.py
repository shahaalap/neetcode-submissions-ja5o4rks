class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)
        sortedCounts = dict(sorted(counts.items()))

        for i in range(len(hand) // groupSize):
            firstkey = None

            if len(sortedCounts) > 0:
                firstkey = next(iter(sortedCounts))

            
            if firstkey is None:
                return False

            for key in range(firstkey, firstkey + groupSize):
                if key not in sortedCounts:
                    return False

                sortedCounts[key] -= 1
                if sortedCounts[key] == 0:
                    del sortedCounts[key]

        return True
                
