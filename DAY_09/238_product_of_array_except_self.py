class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        suf = 1
        answer = []
        for i in range(len(nums)):
            answer.append(pre)
            pre = pre * nums[i]
        for j in range(len(nums)-1,-1,-1):
            answer[j] = answer[j] * suf
            suf = suf * nums[j]
        return answer