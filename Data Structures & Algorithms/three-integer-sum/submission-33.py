class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        res = []
        for i in range(len(nums)-2):
            
            l= i+1
            r = len(nums)-1
            print(l, r)
            while l < r:
                sum = nums[l] + nums[r] + nums[i]
                if sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1
                else:
                    list = sorted([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    if list in res:
                        continue
                    else:
                        res.append(list)
                        continue
        return res

