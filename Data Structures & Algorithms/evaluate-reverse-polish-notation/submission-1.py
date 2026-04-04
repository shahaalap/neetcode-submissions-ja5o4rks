class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c not in ["+", "-", "*", "/"]:
                stack.append(int(c))
            else:
                right = stack.pop()
                left = stack.pop()
                result = 0

                if c == "+":
                    result = left + right
                elif c == "-":
                    result = left - right
                elif c == "*":
                    result = left * right
                elif c == "/":
                    result = int(left / right)

                stack.append(result)

        return stack.pop()