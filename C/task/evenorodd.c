#include<stdio.h>
#include<stdlib.h>

int evenoroddnumber()
{
    int a;
    printf("Enter The A Value ");
    scanf("%d",&a);
 if(a%2==0)
    {
        printf("Even Number");
    }

    else
    {
        printf("Odd Number");
    }
    return 0;
}