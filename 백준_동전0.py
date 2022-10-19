import math

N,K=map(int, input().split())
c_list=[int(input()) for _ in range(N)]

count=0
while(len(c_list)!=0): #0일때까지 while문 
    pop=c_list.pop(-1) #맨 마지막에서 하나씩 꺼냄
    lastMod=(K/pop) #K원과 / pop(-1)을 나눈 값
    if(lastMod>=1): #이 값이 1이상이면
        count+=math.floor(lastMod) #count에 버림값을 넣음
    K=K%pop #그리고 나머지값을 K에 저장
print(count)
