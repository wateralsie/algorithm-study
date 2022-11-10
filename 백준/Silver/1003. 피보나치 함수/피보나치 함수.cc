#include <iostream>

using namespace std;
int oneNumber[40] = {0};
int zeroNumber[40] = {0};

int zeroFibonacci(int n){
    
    
    if(n == 0){
        zeroNumber[n] = 1;
        return zeroNumber[n];
    }
    else if(n == 1){
        zeroNumber[n] = 0;
        return zeroNumber[n];
    }
    
    if(zeroNumber[n] > 0){
        return zeroNumber[n];
    }
    
    zeroNumber[n] = zeroFibonacci(n-1) + zeroFibonacci(n-2);
    return zeroNumber[n];

}
int oneFibonacci(int n){
    
    if(n == 0){
        oneNumber[n] = 0;
        return oneNumber[n];
    }
    else if(n == 1){
     
        oneNumber[n] = 1;
        return oneNumber[n];
    }
    
    if(oneNumber[n] > 0){
        return oneNumber[n];
    }
    oneNumber[n] = oneFibonacci(n-1) + oneFibonacci(n-2);
    return oneNumber[n];
}
int main(void){
    
    int T;
    
    int N;
    cin >> T;
    while(T--){
        cin >> N;
        cout << zeroFibonacci(N) << " ";
        cout << oneFibonacci(N);
        cout << '\n';
    }
}
