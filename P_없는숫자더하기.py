def solution(numbers):
    numbers.sort() ## numbers를 sort해라
    list_num=[i for i in range(0,10)] # 0부터 9까지를 list_num에 담아라 

    while len(numbers)>0:
      a=numbers.pop() ## 주어진 numbers를 pop한걸 a에 담고
      if a in list_num: ##list_num에 있는가?
        list_num.pop(a)
    return sum(list_num)

numbers=[1,2,3,4,6,7,8,0]
solution(numbers)