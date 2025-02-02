#include<iostream>
using namespace std;

bool isPalindrome(int x) {
        int n = x;
        int rev = 0;
        while (x > 0) {
            rev = (rev * 10) + (x % 10);
            x = x / 10;
        }
        if (rev == n) 
            return true;
        else 
            return false;
    }
    
int main(){
    int x;
    cout<<"Enter a number: ";
    cin>>x;
    if (isPalindrome(x)) {
        cout <<" True" << endl;
    } else {
        cout <<" False" << endl;
    }
}