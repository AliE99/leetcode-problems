class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            k = i + 1
            j = len(nums) - 1

            while k < j:
                res = nums[i] + nums[j] + nums[k]
                if res == 0:
                    result.append([nums[i], nums[k], nums[j]])
                    k += 1

                    while nums[k] == nums[k - 1] and k < j:
                        k += 1

                elif res < 0:
                    k += 1
                else:
                    j -= 1

        return result


# [-3, -1, 4]
# [-2, -1, 3]
# [-1, -1, 2]

nums = [-1, 0, 1, 2, -1, -4]
# nums = [0, 1, 1]
# nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
print(Solution().threeSum(nums=nums))
