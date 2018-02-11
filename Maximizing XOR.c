/*
Given two integers,  and , find the maximal value of  xor , where  and  satisfy the following condition:

L<=A<=B<=R

*/
#include <stdio.h>

int maximizingXor(int l, int r) {
    int ans=0, x;
    for(int i=l; i<=r; ++i){
        for(int j=i+1; j<=r; ++j){
            x=i^j;
            if(ans<x){
                ans=x;
            }
        }
    }
    return ans;
}

int main() {
    int l; 
    scanf("%i", &l);
    int r; 
    scanf("%i", &r);
    int result = maximizingXor(l, r);
    printf("%d\n", result);
    return 0;
}
