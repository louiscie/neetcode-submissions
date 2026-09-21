class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r =0, len(heights) -1
        max_vol = 0
        while l < r :
            smaller_height = min(heights[l], heights[r])
            water_vol = smaller_height* (r - l)
            max_vol = max(water_vol, max_vol)
            
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return max_vol


            