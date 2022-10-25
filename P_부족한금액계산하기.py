def solution(price, money, count):
    total_price=0
    for i in range(count+1):
        total_price+=price*i
    money-=total_price
    if money > 0:
        money=0
    return abs(money)