from collections import deque


def solution(S, T):
    C = 0
    q = deque()
    q.append([S, T, C])  # 처음 큐

    while q:
        s, t, c = q.popleft()
        if s < t:
            q.append([s * 2, t + 3, c + 1])
            q.append([s + 1, t, c + 1])
        elif s == t:
            print(c)
            break


for _ in range(int(input())):
    S, T = map(int, input().split())
    solution(S, T)

                # 10,20,0
            # 20,23,1       11,20,1
    # 40,26,2  21,23,2   22,23,2  12,20,2