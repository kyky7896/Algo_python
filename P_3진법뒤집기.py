def solution(n):
    answers=''
    while n > 0 :
      a = n % 3 #나머지 
      b = n // 3 #몫
      n = b
      answers+=str(a)
    answers=int(answers,3) 
    return answers