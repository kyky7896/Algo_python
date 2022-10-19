import heapq as hq
import sys

imput=sys.stdin.readline
min_heap=[] #양수들만 최소힙에 보관
max_heap=[] #음수들만 최대힙에 보관 =>하나씩 pop할때마다 큰값부터 뺌
for _ in range(int(input())):
    x=int(input())
    if x:
        if x > 0 : #양수일때는
            hq.heappush(min_heap, x)
        else:
            hq.heappush(max_heap, -x) #maxheap으로 바꿈
    else: 
        if min_heap: #
            if max_heap:
                if min_heap[0] < abs(-max_heap[0]):
                    print(hq.heappop(min_heap))
                # elif min_heap[0] > abs(max_heap[0]):
                #     print(hq.heappop(max_heap))
                else: #같은경우 음수쪽 풀력
                    print(-hq.heappop(max_heap)) 

            else: #max힙 비어있는경우
                print(hq.heappop(min_heap))
        else: #min_heap이 비어있는경우
            if max_heap: 
                print(-hq.heappop(max_heap))
            else:
                print(0)