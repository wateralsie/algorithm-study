#include <iostream>
#include <vector>

using namespace std;
int k;
int check;

char str[10];
bool taken[10];
vector<int> mAns;
vector<int> MAns;

bool compareNumbers(int a, int b, char k){
    if(k == '>'){
        return a>b;
    }
    else{
        return a<b;
    }
}
void findingNumbers(int idx, vector<int> ans){
    
    if(idx == k+1){
        if(check == 0){
            mAns = ans;
        }
        else{
            MAns = ans;
            
        }
        ++check;
        
        return;
    }
    
    for(int i = 0; i< 10; i++){
        if(!taken[i]){
            if(idx == 0 || compareNumbers(ans.back(), i, str[idx-1])){
                taken[i] = true;
                ans.push_back(i);
                findingNumbers(idx+1, ans);
                
                taken[i] = false;
                ans.pop_back();
            }
        }
    }
    
    
}
int main(void){
   
    char n;
    
    cin >> k;
    
    vector<int> answer;
    
    for(int i = 0; i < k ; i++){
        cin >> n;
        str[i] = n;
    }
    
    findingNumbers(0, answer);
    
    
    
    
    for(int i = 0; i< MAns.size(); i++){
        cout << MAns[i];
    }
    cout << '\n';
    
    for(int i = 0; i< mAns.size(); i++){
        cout << mAns[i];
        
    }
}

