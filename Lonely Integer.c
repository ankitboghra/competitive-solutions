/*
Consider an array of  integers, , where all but one of the integers occur in pairs. In other words, every element in  occurs exactly twice except for one unique element.
Given , find and print the unique element.
*/
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int lonelyinteger(int a_size, int* a) {
    // Complete this function
    int ans;
    bool flag=false;

    for(int i=0; i<a_size; ++i){
        flag=false;
        for(int j=i+1; j<a_size; ++j){
            if(a[i] == a[j] && a[j]!=101){
//                printf("%d == %d\n", a[i], a[j]);
                a[j]=a[i]=101;
                flag=true;
                break;
            }
        }
        if(flag==false && a[i]!=101){
            //printf("Entered into flag : %d\n", a[i] );
            ans=a[i];
        }
    }
    return ans;
}

int main() {
    int n; 
    scanf("%i", &n);
    int *a = malloc(sizeof(int) * n);
    for(int a_i = 0; a_i < n; a_i++){
       scanf("%i",&a[a_i]);
    }
    int result = lonelyinteger(n, a);
    printf("%d\n", result);
    return 0;
}
