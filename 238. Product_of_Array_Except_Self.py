#Leetcode Problem : 238. Product of Array Except Self
# link: https://leetcode.com/problems/product-of-array-except-self/description/?envType=problem-list-v2&envId=prefix-sum
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_pref=[1]
        prod_suff=[1]
        ans=[]
        for i in nums:
            prod_pref.append(prod_pref[-1]*i)
        for i in range(len(nums)-1,-1,-1):
            prod_suff.insert(0,prod_suff[0]*nums[i])
        for i in range(len(nums)):
            ans.append(prod_pref[i]*prod_suff[i+1])
        return ans
        
        
