strings=["sun", "bed", "car"]
n=1

def solution(strings, n):
  return (sorted(strings, key=lambda strings:(strings[n], strings)))
solution(strings,n)