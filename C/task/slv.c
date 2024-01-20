#include<stdio.h>
#include<stdlib.h>

int forloop()
{
int i;
int j;
for(int i=1;i<10;i++)
{
    printf("*\n");
for(int j=0;j<i;j++)
    printf("*");
}

return 0;
}