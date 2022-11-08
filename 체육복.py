def solution(n, lost, reserve):
    set_reserve=set(reserve)-set(lost) #순수하게 보유하고 있는 사람들
    set_lost=set(lost)-set(reserve) #순수하게 잃어버린 사람들

    #reserve의 왼쪽을 빌려줘야함
    for i in set_reserve:
      if i-1 in set_lost:
        set_lost.remove(i-1)
      elif i+1 in set_lost:
        set_lost.remove(i+1)
    return n-len(set_lost)

n=5
lost=[2,4]
reserve=[1,3,5]
solution(n, lost, reserve)

