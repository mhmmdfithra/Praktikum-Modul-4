#include<stdio.h>

int main(void){
int a,b,c,d,hasil,total;
scanf("%d %d", &a, &b);
for (c=1;c<=a;c++){
     for(d=c;d>0;d--){printf("(%d * %d)", d,b);
         if(d>1){
            printf(" + ");}}
    hasil += (c)*b;
    printf(" = %d\n", hasil);
    total += hasil;
    }
printf("%d", total);
}