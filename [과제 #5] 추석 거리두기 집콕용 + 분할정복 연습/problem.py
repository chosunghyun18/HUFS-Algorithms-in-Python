def guess_two_missing_numbers(n, S, T):
  # code here
  return a, b  # a < b are two missing numbers
​
n = int(input())
S, T = [int(x) for x in input().split()]
a, b = guess_two_missing_numbers(n, S, T)
print(a, b)
