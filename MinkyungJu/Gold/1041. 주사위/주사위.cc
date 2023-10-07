#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<int> dieNumbers;
int n;

unsigned long greedy(void){
    
    unsigned long result = 0;
    unsigned long diceSideNum = n; 
    diceSideNum *= diceSideNum;
   
    if(n == 1){
        sort(dieNumbers.begin(), dieNumbers.end());
        for(int i = 0 ; i< 5; i++){
            result += dieNumbers[i];
        }
        return result;
    }
    
    
    int edgeNum = n+(n-1)+(n-1)+(n-2);
    int sideNum = n * 2;
    
    int sortNumbers[3];

    if(dieNumbers[0] < dieNumbers[5] ){
        sortNumbers[0] = (dieNumbers[0]);
        
    }
    else{
        sortNumbers[0] = (dieNumbers[5]);
    }
    
    if(dieNumbers[1] < dieNumbers[4]){
        sortNumbers[1] = (dieNumbers[1]);
    }
    else
        sortNumbers[1] = (dieNumbers[4]);
    
    if(dieNumbers[2] < dieNumbers[3]){
        sortNumbers[2] = (dieNumbers[2]);
    }
    else
        sortNumbers[2] = (dieNumbers[3]);
    
    sort(sortNumbers, sortNumbers+3);
    
    unsigned long oneSide;
    unsigned long twoSide;
    unsigned long thirdSide;
    
    oneSide = (diceSideNum * 2) + ((diceSideNum - n*2 )*2) + (diceSideNum - edgeNum ) ;
    
  
    if(sideNum != 0){
        twoSide =  (edgeNum - 4) + (n * 2) * 2;
      
        thirdSide = 4;
    }
    else{
        twoSide = diceSideNum;
        thirdSide = 4;
    }
    

    result += sortNumbers[0] * oneSide;
   
    result += sortNumbers[1] * twoSide;
   
    result += sortNumbers[2] * thirdSide;
    
    
    return result;
    
}
int main(void){
    
  
    int number;
    
    cin >> n;
    
    for(int i = 0; i< 6; i++){
        cin >> number;
        dieNumbers.push_back(number);
    }
    
    cout << greedy();
    
}
