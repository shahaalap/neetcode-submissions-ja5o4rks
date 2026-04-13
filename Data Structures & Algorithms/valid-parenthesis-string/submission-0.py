class Solution:
    def checkValidString(self, s: str) -> bool:
        quotes, stars = deque([]), deque([])

        for i, c in enumerate(s):
            if c == '(':
                quotes.append((c,i))
            elif c == '*':
                stars.append((c, i))
            else:
                if len(quotes) == 0 and len(stars) == 0:
                    return False
                elif len(quotes) > 0:
                    quotes.pop()
                else:
                    stars.pop()


        while len(quotes) > 0 and len(stars) > 0:
            q = quotes.pop()
            s = stars.pop()

            if q[1] > s[1]:
                return False

        return False if len(quotes) else True