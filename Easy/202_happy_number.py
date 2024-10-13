class Solution:
    def isHappy(self, n: int) -> bool:
        my_set = set()
        while True:
            res = 0
            for i in str(n):
                res += int(i) * int(i)
            if res == 1:
                return True
            if res in my_set:
                return False

            my_set.add(res)
            n = res

print(Solution().isHappy(2))
