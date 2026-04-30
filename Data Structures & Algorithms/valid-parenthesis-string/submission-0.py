class Solution:
    def checkValidString(self, s: str) -> bool:
        left, star = [], []

        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == '*':
                star.append(i)
            else:
                if len(left):
                    left.pop()
                elif not len(left) and len(star):
                    star.pop()
                else:
                    return False

        while len(left) and len(star):
            if left.pop() > star.pop():
                return False

        return len(left) == 0

