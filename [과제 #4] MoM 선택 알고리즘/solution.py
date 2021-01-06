def find_median_five(L):
  if len(L)<=2 :return L[0]
  if len(L) == 3:
    a,b,c = L
    if a > b:
      return b if b>c else (c if a>c else a)
    else:
      return a if a>c else (c if b>c else b)
  if len(L) == 4:
    win1, los1 = L[0], L[1] if L[0] > L[1] else L[1], L[0]
    win2, los2 = L[2], L[3] if L[2] > L[3] else L[3], L[2]
    return los2 if los1 < los2 else los1

  if len(L)== 5:
    if L[0] > L[1]: win1, los1 = L[0], L[1]
    else: win1, los1 =  L[1], L[0]
    if L[2] > L[3]: win2, los2 = L[2], L[3]
    else: win2, los2 =  L[3], L[2]

    if win1> win2:
      if win1 > L[4] and win2>L[4]:
        if los1 > los2:
          return los2 if los2>L[4] else (L[4] if los1>L[4] else los1)
        else:
          return los1 if los1>L[4] else (L[4] if los2>L[4] else los2)
      else: return win2
    else:
      if win1> L[4] and win2 > L[4]:
        if los1 > los2:
          return los2 if los2>L[4] else (L[4] if los1>L[4] else los1)
        else:
          return los1 if los1>L[4] else (L[4] if los2>L[4] else los2)
      else: return win1



  # if len(L)== 5:
  #   if L[0] > L[1]: win1, los1 = L[0], L[1]
  #   else: win1, los1 =  L[1], L[0]
  #   if L[2] > L[3]: win2, los2 = L[2], L[3]
  #   else: win2, los2 =  L[3], L[2]

  #   if win1> win2:
  #     if win1< L[4]:
  #       win1 = L[4]
  #     else:
  #       win1 = los1
  #       los1 = L[4]
  #   else:
  #     if L[4]> los2:
  #       win2 = L[4]
  #     else:
  #       win2 = los2
  #       los2 = L[4]

  #   if win1 > win2:
  #     return win2 if win2>los1 else los1
  #   else:
  #     return win1 if win1>los2 else los2


# find_median_five([5,4,1,2,-5])




def MoM(L, k): # L의 값 중에서 k번째로 작은 수 리턴

  if len(L) == 1: # no more recursion
    return L[0]
  i = 0
  A, B, M, medians = [], [], [], []
  while i+4 < len(L):
    medians.append(find_median_five(L[i: i+5]))
    i+=5
  if i < len(L) and i+4 >= len(L):
    medians.append(find_median_five(L[i:]))

  mom = MoM(medians, (len(medians)+1)//2)
  for v in L:
    if v < mom: A.append(v)
    elif v > mom: B.append(v)
    else: M.append(v)

  if k <= len(A):
    return MoM(A, k )
  elif k > (len(A)+len(M)):
    return MoM(B, k-len(A)-len(M))
  else: return mom
# n과 k를 입력의 첫 줄에서 읽어들인다
# n개의 정수를 읽어들인다. (split 이용 + int로 변환)
# n, k  = map(int, input().split())
# L = list(map(int, input().split()))

"""10 3
-62 1 82 55 -48 63 47 -63 93 92
"""

n, k = 10, 3
L = list(map(int, '-62 1 82 55 -48 63 47 -63 93 92'.split()))


print(MoM(L, k))
