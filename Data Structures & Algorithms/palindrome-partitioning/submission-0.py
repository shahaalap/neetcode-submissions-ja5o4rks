class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []

        def isPalindrome(subs):
            x , y = 0 , len(subs) - 1
            while x <= y and subs[x] == subs[y]:
                x += 1
                y -= 1

            return x > y


        def helper(i, slate):
            if i == n:
                result.append(list(slate))
                return

            for j in range(i, n):
                if isPalindrome(s[i:j + 1]):
                    slate.append(s[i:j + 1])
                    helper(j + 1, slate)
                    slate.pop()

        helper(0, [])
        return result


                