#include <iostream>
#include <vector>


using namespace std;
vector<int> answer;
bool taken[9] = {false};

void Dfs(int M, int N, int id, int depth){
    
    
    if(depth == M){
        
        for(int i = 0; i< M; i++){
            cout << answer[i] << " ";
        }
        cout << '\n';
        return;
    }
    
    for(int i = 0; i < N; i++){
        if(taken[i] == true){
            continue;
        }
        if(id > i){
            continue;
        }
        
        answer.push_back(i+1);
        taken[i] = true;
        Dfs(M, N, i+1, depth + 1);
        
        answer.pop_back();
        taken[i] = false;
    }
    
    
    
    
}

int main(void){
    
    int M;
    int N;
    
    cin >> N;
    cin >> M;
    
    Dfs(M, N, 0,0);
    
}