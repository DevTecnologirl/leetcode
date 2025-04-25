class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        d = {}

        for idx, x in enumerate(nums):
            if x in d and abs(idx - d[x] ) <= k:
                    return True
            else:
                d[x] = idx

        return False