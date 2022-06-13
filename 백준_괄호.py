n=int(input())
for _ in range(n):
    m=input()
    stack=[]
    isVps=True
    for i in range(len(m)): 
        if m[i]=="(":
            stack.append(m[i])
        else:
            if not stack:
                isVps=False
                break
            else:
                stack.pop()
    
    if stack:
        isVps=False
    
    print('YES' if isVps else 'NO')

