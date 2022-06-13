# from sys import stdin
# n = int(stdin.readline())
# stack=[]
# for i in range(1,n+1):
#     stack.append(i)
# # print(stack)
# while(len(stack)>1):
#     stack.pop(0) #제일 앞에 있는거 삭제
#     stack.append(stack.pop(0)) # 제일 앞에 있는거 삭제+담아서 맨끝으로 append
# print(stack[0])

## 시간초과 뜸 

from collections import deque
n=int(input())
dq=deque(range(1, n+1)) #선언시부터 넣어줌

while len(dq)>1:
    dq.popleft()
    dq.append(dq.popleft())
print(dq.popleft())