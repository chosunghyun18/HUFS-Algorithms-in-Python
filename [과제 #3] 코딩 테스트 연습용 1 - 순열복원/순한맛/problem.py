def reconstruct(S, L):
  # S, L로부터 A를 재구성해 리턴
  # 이 함수를 작성합니다~
​

# S와 L을 차례로 읽어들임
S = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
A = reconstruct(S, L)

print(A)

​

# 1. 본인이 작성한 알고리즘의 수행시간을 간략히 분석해보자
# 2. 수행시간 T(n)을 Big-O료 표기해보자
