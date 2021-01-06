def find_median_five(L):
  # (L의 다섯개의 값 중에서 중간값을 찾아 리턴하는 코드)
​
def MoM(L, k): # L의 값 중에서 k번째로 작은 수 리턴

  if len(L) == 1: # no more recursion
    return L[0]
  i = 0
  A, B, M, medians = [], [], [], []
  while i+4 < len(L):
    medians.append(find_median_five(L[i: i+5]))
    #(1번)
  if i < len(L) and i+4 >= len(L):
    #(2번)

  mom = MoM("""3번""")
  for v in L:
    if v < mom: # 4번
    elif v > mom: #5번
    else: #10번
​
  if ("""6번""": return MoM(("""8번""")
  elif ("""7번""": return MoM(("""9번""")
  else: return mom
​
# n과 k를 입력의 첫 줄에서 읽어들인다
# n개의 정수를 읽어들인다. (split 이용 + int로 변환)
print(MoM(L, k))
