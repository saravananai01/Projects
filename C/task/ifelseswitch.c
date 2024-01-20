# include<stdio.h>

int ifelseswitch()
{
 int d;
 int a;
 int b;
 int c;
 char e;
 printf("Enter how many value:");
 scanf ("%d", &d);
 if (d==2)
 {
  printf("Enter the valueof A:");
 scanf ("%d", &a); 
 printf("Enter the valueof B:");
 scanf ("%d", &b);  
 printf("Enter the operator:");
 scanf(" %c", &e);
 switch(e)
 {
    case '+':
       printf("The added value of A and B is:%d",a+b);
       break;
    case '-':
       printf("The subtracted value of A and B is:%d", a-b);
       break;
    case '*':
       printf("The Multiplied value of A and B is:%d", a*b);
       break;
       case '/':
       printf("The Divied value of A and B is:%d", a/b);
       break;
       case '%':
       printf("The Modulas value of A and B is:%d",a%b);
       break;
 }
 }
else{
    
printf("Enter the valueof A:");
 scanf ("%d", &a); 
 printf("Enter the valueof B:");
 scanf ("%d", &b);  
 printf("Enter the valueof C:");
 scanf ("%d", &c); 
 printf("Enter the operator:");
 scanf(" %c", &e);
 switch(e)
 {
    case '+':
       printf("the added value of A and B is:%d",a+b+c);
       break;
    case '-':
       printf("the subtracted value of A and B is:%d",a-b-c);
       break;
    case '*':
       printf("the Multiplied value of A and B is:%d",a*b*c);
       break; 
 } 

 }

return 0;
}
