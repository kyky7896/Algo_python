from curses import keyname


strings=["sun", "bed", "car"]
n=1
def solution(strings, n):
  dic={}
  answer=[]
  for i in range(len(strings)):
    dic[strings[i][n]]=strings[i]
  dic=dict(sorted(dic.items()))
  for j in dic.values():
    answer.append(j)
  return (answer)


def solution(strings, n):
  return (sorted(strings, key=lambda strings:(strings[n], strings)))
solution(strings,n)