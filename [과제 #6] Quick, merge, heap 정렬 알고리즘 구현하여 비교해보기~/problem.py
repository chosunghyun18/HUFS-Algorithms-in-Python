import random, timeit
​
##
## 여기에 세 가지 정렬함수를 위한 코드를...
##
​
def quick_sort(A, first, last):
  if first >= last : return A
  left, right = first + 1, last
  pivot = A[first]

  while left <= right:
    while left <= last and A[left] < pivot:
      left+=1
    while right > first and A[right] > pivot:
      right-=1

    if left <= right:
      A[left], A[right] = A[right], A[left]
      quick_sort(A, first, right-1)
      quick_sort(A, right+1, last)
​
​
# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#
​
def check_sorted(A):
  for i in range(n-1):
    if A[i] > A[i+1]: return False
  return True
​
#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0
​
n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
