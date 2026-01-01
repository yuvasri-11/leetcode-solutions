# k-sum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 0, 4)

    def kSum(self, nums: List[int], target: int, start: int, k: int) -> List[List[int]]:
        res = []
        if start == len(nums) or nums[start] * k > target or target > nums[-1] * k:
            return res
        if k == 2:
            return self.twoSum(nums, target, start)
        for i in range(start, len(nums)):
            if i == start or nums[i - 1] != nums[i]:
                # here is a hidden matching target==0
                # if not matching target, then kSum() will return empty list
                for sset in self.kSum(nums, target - nums[i], i + 1, k - 1):
                    # if kSum(k-1) return empty, it will not execute this line
                    res.append([ nums[i] ] + sset) # put nums[i] in a list
        return res

    def twoSum(self, nums: List[int], target: int, start: int) -> List[List[int]]:
        res = []
        lo, hi = start, len(nums) - 1
        while lo < hi:
            s = nums[lo] + nums[hi]
            if s < target or (lo > start and nums[lo] == nums[lo - 1]):
                lo += 1
            elif s > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                res.append([nums[lo], nums[hi]])
                # continue searching, could be multiple answers
                lo += 1
                hi -= 1
        return res

#########

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        if n < 4:
            return ans
        nums.sort()
        for i in range(n - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k, l = j + 1, n - 1
                while k < l:
                    x = nums[i] + nums[j] + nums[k] + nums[l]
                    if x < target:
                        k += 1
                    elif x > target:
                        l -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k, l = k + 1, l - 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
        return ans
