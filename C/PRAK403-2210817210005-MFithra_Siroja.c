#include<stdio.h>

int main(void){
int a,b,c,d; 
scanf("%d",&a); scanf("%d",&b);
if (a>b){
    for(c=a,d=b;c>=b,d<=a;c--,d++){printf("%d %d",c,d);
        if(c>b){
            printf(" - ");
}}}
else{
    for(c=a,d=b; c<=b,d>=a;c++,d--){printf("%d %d",c,d);
        if(c<b){
            printf(" - ");
}}}
}