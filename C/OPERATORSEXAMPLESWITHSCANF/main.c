#include <stdio.h>
#include <stdlib.h>
int Additionprogram(int a,int b);
int Subtractionprogram(int a,int b);
int Multiplicationprogram(int a,int b);
int Divisionprogram(int a,int b);
int Modulusprogram(int a,int b);
int Incrementprogram(int a);
int Decrementprogram(int b);
int AssignmentDemoOperators(int a,int b);
int ComparisonDemoOperators(int a,int b);
int LogicalDemoOperators();
int main()
{
   int a,b,c;
   printf("\nEnter The A Value:");
   scanf("%d",&a);
   printf("\nEnter The B Value:");
   scanf("%d",&b);
   Additionprogram(a,b);
   Subtractionprogram(a,b);
   Multiplicationprogram(a,b);
   Divisionprogram(a,b);
   Modulusprogram(a,b);
   Incrementprogram(a);
   Decrementprogram(b);
   AssignmentDemoOperators(a,b);
   ComparisonDemoOperators(a,b);
   LogicalDemoOperators();
   return 0;
}
int Additionprogram(int a,int b)
{
    printf("\nArithmeticOperators:\n");
     int d=a+b;
     printf("\n\tAdddition Value of a and b is...%d\n",d);
}
int Subtractionprogram(int a,int b)
{
     int d=a-b;
     printf("\n\tSubtraction Value of a and b is...%d\n",d);
}
int Multiplicationprogram(int a,int b)
{
    int d=a*b;
     printf("\n\tMultiplication Value of a and b is...%d\n",d);

}
int Divisionprogram(int a,int b)
{
    float d=(float)a/b;
    printf("\n\tDivision Value of a and b is...%.2f\n",d);

}
int Modulusprogram(int a,int b)
{
    int d=a%b;
    printf("\n\tModulus Value of a and b is...%d",d);
}
int Incrementprogram (int a)
{
    printf("\nIncrementprogram:\n");
    while(a<20)
    {
    printf("\n\tIncrement Value of a is...%d\n",a++);

    }

}
int Decrementprogram(int b)
{
    printf("\nDecrementprogram:\n");
    while(b>10)
    {

    printf("\n\tDecrement Value of b is...%d\n",b--);

    }

}
int AssignmentDemoOperators(int a, int b)
{
    int c,d,e,f,g;

    d=1;
    e=2;
    f=3;
    g=4;
    c=a;
    d+=b;
    e-=a;
    f*=b;
    g/=a;
    printf("\nAssignmentDemoOperators:\n\n\tThe Value is C=%d\n\n\tThe Value is D+=%d\n\n\tThe Value is E-=%d\n\n\tThe Value is F*=%d\n\n\tThe Value is G/=%d\n",c,d,e,f,g);
}
int ComparisonDemoOperators(int a,int b)
{
    int d,e,f,g,h,i;
    d=b<a;
    e=a>b;
    f=b<=a;
    g=a>=b;
    h=b!=a;
    i=b==a;
    printf("\nComparisonDemoOperators:\n\n\tThe Value is %d\n\n\tThe Value is %d\n\n\tThe Value is %d\n\n\tThe Value is %d\n\n\tThe Value is %d\n\n\tThe Value is %d\n",d,e,f,g,h,i);
}
int LogicalDemoOperators()
{
    printf("\nLogicalDemoOperators:\n");
    int a=10;
    a=5;
    if(a<10 && 5<a)
    {
     printf("\n\tThe Logical AND Value");

    }

    else if((a==11) || (a==12))
    {
    printf("\n\tThe Logical OR Value");
    }
    else if(!(a<20 && 15>a))
    {
    printf("\n\tThe Logical NOT Value");
    }
    else
    {
    printf("\n\tNo This Value");
    }
}
