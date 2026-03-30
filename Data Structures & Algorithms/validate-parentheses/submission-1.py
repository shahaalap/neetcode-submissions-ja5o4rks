class Solution:
    def isValid(self, s: str) -> bool:
        def isOpen(s):
            return s in ['(','{','[']
        def isClose(s):
            return s in [')','}',']']
        def isMatching(open,close):
            if open == '(' and close == ')':
                return True
            elif open == '{' and close == '}':
                return True
            elif open == '[' and close == ']':
                return True
            else:
                return False

        stack = []

        for i in range(len(s)):
            c = s[i]
            if isOpen(c):
                stack.append(c)
            elif isClose(c) and len(stack) > 0:
                last = stack.pop()
                if not isMatching(last, c):
                    return False
            else:
                return False

        return len(stack) == 0
