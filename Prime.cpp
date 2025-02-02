#include<iostream>
using namespace std;

bool prime(int n){
    int cnt = 0;
    for (int i=1; i<=n; i++){
        if (n%i == 0){
            cnt = cnt+1;
        }
    }

    if (cnt == 2){
        return true;
    }
    else {
        return false;
    }
}
int main(){
    int n;
    cout<<"enter no. ";
    cin>>n;
    if (prime(n)){
        cout<<"prime no.";
    }
    else{
        cout<<"not a prime";
    }
}