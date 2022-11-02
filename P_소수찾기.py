## 에라토스테네세스의 체
## 소수인걸 판별하고 난 배수를 지운다
def solution(n):
  a=[False,False] + [True]*(n-1)
  print(a)

  primes=[]
  for i in range(2, n+1): # 2부터 n+1까지 for문
    if a[i] : #a[2]부터는 True
      primes.append(i) #2를 append
      print("append이후",primes)
      for j in range(2*i,n+1,i) :#2의 배수부터 n까지 2의간격으로
          a[j]=False #false로 바꿔라
  print(a)
  print(primes)
  return len(primes)

solution(10)