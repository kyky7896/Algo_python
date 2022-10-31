from itertools import permutations


import itertools

number=[-2,3,0,2,-5]
def solution(number):
  count=0
  a=list(itertools.combinations(number,3))
  for i in a:
    if (sum(i)==0):
      count+=1
  print(count)

solution(number)