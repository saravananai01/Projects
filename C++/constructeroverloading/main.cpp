#include <iostream>
using namespace std;

class myfirstclass
{
public:
    int x=0;
void addition(int a,int b)
{   int c;
     c=a+b;
    cout <<"C Value",c;
}
   void addition(float a,float b,float f)
{   float c;
     c=a+b+f;
    cout <<"C Value",c;
}
};
int main()
{   int v1,v2;
    myfirstclass mfc;
    cin >> v1 >> v2;
    mfc.addition(v1,v2);
    float v3,v4,v5;
    cin >> v3 >> v4 >> v5;
    mfc.addition(v3,v4,v5);
    return 0;
}
