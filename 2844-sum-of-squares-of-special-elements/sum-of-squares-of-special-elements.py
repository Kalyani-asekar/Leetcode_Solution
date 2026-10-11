class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        sum=0
        
        for i in range(n+1):
            if n%(i+1)==0:
                sum+=nums[i]*nums[i]
            else:
                pass
        return sum

        