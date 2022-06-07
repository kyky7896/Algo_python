import sys

arr=[]
answer=[]
n=int(input()) ##계단의 개수

for i in range(n):
    m=int(input()) ##계단에 쓰여져 있는 점수
    arr.append(m)

answer.append(arr[0])
answer.append(max(arr[0]+arr[1],arr[1])) #시작점은 연속된 3계단에 포함x
answer.append(max(arr[0]+arr[2],arr[1]+arr[2]))

for i in range(3,n):
    answer.append(max(answer[i-2]+arr[i], answer[i-3]+arr[i]+arr[i-1]))
print(answer.pop())

'''
      0   1   2   3   4   5
arr=[10, 20, 15, 25, 10, 20]의 경우
- Sn이 arr[n]까지의 최댓값을 저장하는 수
1) arr[0] 만 있는 경우 => S0=arr[0]=10,
2) arr[0], arr[1] 만 있는 경우 => S1=max(S0+arr[1], arr[1])
3) arr[0], arr[1], arr[2]만 있는 경우 => S2=max(arr[1]+arr[2],arr[0]+arr[1])
                                    
맨 마지막 계단(5)이 밟혔다고 가정하면
그 이전의 계단은 END-1(4) 또는 END-2(3)일것임. 
1) END-1을 밟은 경우 S2(최댓값 저장한 변수)+arr[4]+arr[5]
2) END-2를 밟은 경우 S3(최댓값 저장한 변수)+arr[5]
1)2)중 max를 구하면 됨.

'''

