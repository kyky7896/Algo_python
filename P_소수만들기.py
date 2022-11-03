import itertools

def prime(n):
  if n <= 1 :
    return False
  for a in range(2,n):
    if n % a == 0:
      return False
  return True

def solution(nums):
  per_list=list(itertools.combinations(nums, 3)) ##3개의 수를 구함
  num_list=[]
  for i in per_list:
    num_list.append(sum(i)) #3개를 합한걸 list에 더하고
  print(num_list)
  count=0 ## 몇개인지 세기위한 변수
  for j in num_list:
    if prime(j):
      print(j)
      count+=1
  print(count)
  return count


nums=[1,2,7,6,4]
solution(nums)