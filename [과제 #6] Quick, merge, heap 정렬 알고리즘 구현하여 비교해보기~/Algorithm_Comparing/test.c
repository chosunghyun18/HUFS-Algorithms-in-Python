#include <stdio.h>
#include <stdlib.h>

typedef long long int int64;

int64 fact(int64 n){
    if (n<1) return 1;
    else return (n * fact(n-1));
}

int main(void){
    printf("%lld", fact(4));
}

