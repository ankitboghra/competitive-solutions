#Hackerrank - Time Conversion

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

char* timeConversion(char* s) {
    //AM
    if(s[8]=='A'){
        if(s[0]=='1' && s[1]=='2'){
            s[0]=s[1]='0';
        }
    }        
    //PM
    else{
        if(s[0]=='1' && s[1]=='2'){
            
        }
        else
        {
            int time=0;
            int a=(int)(s[0] - 48);
            time=a*10;
            a=(int)(s[1] - 48);
            time+=a;

            time+=12;

            s[1]=(char)(time%10)+48;
            time=time/10;
            s[0]=(char)(time)+48;
        }
    }
    s[8]=0;
    return s;
}

int main() {
    char* s = (char *)malloc(512000 * sizeof(char));
    scanf("%s", s);
        int result_size;
char* result = timeConversion(s);
    printf("%s\n", result);
    return 0;
}
