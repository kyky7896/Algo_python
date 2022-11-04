def solution(N, stages):
  answer=[]
  s_len=len(stages)
  result={}
  for i in range(1,N+1): ##1
    cnt=0
    for step in stages:
      if step == i:
        cnt+=1
    if cnt == 0:
      result[i]=0
    else:
      result[i]=(cnt/s_len)
    s_len=s_len-cnt
  answer=sorted(result, key=lambda x : result[x], reverse=True) ##result[1]


### 잘못접근함 

stages=[2, 1, 2, 6, 2, 4, 3, 3]
N=5
solution(N,stages)