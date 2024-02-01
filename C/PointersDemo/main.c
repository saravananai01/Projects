#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a=20,b=40;
    printf("Value of A               : %d\n",a);
    printf("Addres Of The A          : %d\n", &a);
    printf("------------------------\n");
    printf("VAlue Of B               : %d\n",b);
    printf("Addres Of The B          : %d\n", &b);
    printf("------------------------\n");
    int *p=&a;
    printf("Value Of P               : %d\n",p);
    printf("Addres Of The P          : %d\n", &p);
    printf("Stored Addres Of The *p  : %d\n", *p);
    printf("------------------------\n");
    int **s=&p;
    printf("Value Of S               : %d\n",s);
    printf("Addres Of The S          : %d\n", &s);
    printf("Stored Addres Of The **S : %d\n", **s);
    printf("------------------------\n");
     int ***k=&s;
    printf("Value Of K               : %d\n",k);
    printf("Addres Of The K          : %d\n", &k);
    printf("Stored Addres Of The ***K: %d\n", ***k);
    printf("------------------------\n");
    void *v=&a;
    printf("Value Of K               : %d\n",v);
    printf("Addres Of The K          : %d\n", &v);
    printf("Stored Addres Of The ***K: %d\n", *(int*)v);
    return 0;
}
