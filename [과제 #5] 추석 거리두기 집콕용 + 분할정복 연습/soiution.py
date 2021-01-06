def guess_two_missing_numbers(n, S, T):
  s_sum = sum(range(1,n+1))
  t_sum = n * (n+1) * (2*n+1) /6
  two_sum = int(s_sum - S)
  two_sum_sqr = t_sum - T

  for end in range(n, two_sum//2, -1):
    start = two_sum - end
    if (end**2 + start**2 )== two_sum_sqr:
      return start, end
  # return a, b  # a < b are two missing numbers


# n = int(input())
# S, T = [int(x) for x in input().split()]

n =10
S, T = 44, 312


a, b = guess_two_missing_numbers(n, S, T)
print(a, b)

