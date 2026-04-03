import random
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(point):
            return math.sqrt(point[0] ** 2 + point[1] ** 2)

        def partition(l, r):
            pivot = random.randint(l, r)
            points[pivot], points[r] = points[r], points[pivot]

            i = l
            for j in range(l, r):
                if distance(points[j]) < distance(points[r]):
                    points[i], points[j] = points[j], points[i]
                    i += 1

            points[i], points[r] = points[r], points[i]
            return i
        
        l, r = 0, len(points) - 1
        
        while l <= r:
            p = partition(l, r)

            if p == k:
                break
                
            if p < k:
                l = p + 1
            else:
                r = p - 1

        return points[:k]

        