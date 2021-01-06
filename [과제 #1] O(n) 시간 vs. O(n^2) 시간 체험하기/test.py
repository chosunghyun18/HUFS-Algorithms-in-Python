def doSomething(n):
    count = 0
    k =1
    while k*k <= n:
        count += 1
        k = k +1
    print("k", k)
    return count

print(doSomething(10))
