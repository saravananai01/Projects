#include <iostream>
using namespace std;

class myfirstclass
{
public:
    int a=50;
void mutiplay()
{   int x,y,z;
    cout <<"Enter The X Value\n";
    cin >> x;
    cout <<"Enter The Y Value\n";
    cin >> y;
    cout <<"Enter The Z Value\n"<<(x*y);
}
};

int addition()
{
    int a,b,c;
    cin >> a >> b;
    c=a+b;
    cout << c;
    return 0;
}

int main()
{
    addition();
    myfirstclass mfc;
    cout << mfc.a;
    mfc.mutiplay();
    return 0;
}
