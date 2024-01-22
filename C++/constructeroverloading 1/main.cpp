#include <iostream>
using namespace std;

class myfirstclass
{
public:

void addition(int a,b)
{
    cout <<"C Value",(a+b);
}
   void addition(float c,d,e)
   {
    cout <<"C Value",(c+d+e);
}
};
int main()
{    myfirstclass mfc;
    int a,b;
    cin >> a >> b;
    mfc.addition(a,b);
    float c,d,e;
    cin >> c >> d >> e;
    mfc.addition(c,d,e);
    return 0;
}
