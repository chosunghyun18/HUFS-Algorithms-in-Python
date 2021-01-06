def print_subset(x):
    print([A[i] for i in range(len(x)) if x[i]])
​
def subset_sum(k):
    v_sum = 현재까지 선택한 값의 합
    if k == len(A):
        if v_sum == S:
            print_subset(x)
    else:
        # code for x[k] = 1 and x[k] = 0
​
​
# 아래 코드는 수정하지 말고 그대로 사용할 것
A = list(set(int(x) for x in input().split()))
A.sort()
S = int(input())
x = [0]*len(A)
subset_sum(0)
