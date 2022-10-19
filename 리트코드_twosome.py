# def twoSum(nums,target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if (target==nums[i]+nums[j]):
#                 return [i,j]


nums=[2,7,9,11]
# 개선
def twoSum(nums, target):
    for i,num in enumerate(nums):
        res = target - num
        if res in nums[i+1::]:
            return [i, i+nums[i+1::].index(res)+1] #0(1)연산
            # 뒤에 nums~의 인덱스값은 0이 됨 . 
            # +i를 더해줘야함. i이후의 인덱스

#시간복잡도 -> O(N^2)

# 개선 
def twoSum(nums, target):
    dicts={}
    for i, num in enumerate(nums): #O(N)
        res=target-num
        if res in dicts: #O(1)
            return [i, dicts[res]]
        dicts[num]=i


#시간복잡도 -> O(N)
#공간복잡도 -> O(N)