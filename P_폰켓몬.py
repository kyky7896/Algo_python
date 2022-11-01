
nums=[3,1,2,3]
def solution(nums):
    set_nums=int(len(nums)//2)
    kind_nums=len(list(set(nums)))
    
    answer=kind_nums if (set_nums > kind_nums) else set_nums
    print(answer)
    
solution(nums)