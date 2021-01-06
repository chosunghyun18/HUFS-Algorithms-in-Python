def fibo(n):
    if(n ==0 or n==1):
        return print(1)
    a = 1
    b = 1
    while(n-2 >=0):

        old = a

        a = b+a
        b = old

        n -=1
    return a

if __name__ == "__main__":
    print(fibo(6))
