#include <iostream>
using namespace std;

class myfirstclass
{
public:


    myfirstclass()
    {
        cout <<"Enter The Name...\n";
        string name;
        cin >> name;
        cout << "\tWelcome To The String " << name;

    }
void addition(int a,int b)
{
    int c;
    c=a+b;
    cout <<"First Function OverLoad\n" << c ;
}

void addition1(float a,float b,float f)
{
    float c;
    c=a+b+f;
    cout <<"Second Function OverLoad\n" <<c;
}

void addition1(float a,float b,float f,float e)
{
    float c;
    c=a+b+f+e;
    cout <<"Third Function OverLoad\n" <<c;
}
void addition(string Name,string name)
{
    cout <<"Name\n" << Name+name;
}
};

int main()
{
    myfirstclass mfc;
    int v1,v2;
    cin >> v1 >> v2 ;
    mfc.addition(v1,v2);
    float v3,v4,v5;
    cin >> v3 >> v4 >> v5;
    mfc.addition1(v3,v4,v4);
    float v6,v7,v8,v9;
    cin >> v6 >> v7 >> v8 >> v9;
    mfc.addition1(v6,v7,v8,v9);
    mfc.addition("Saro","Saravanan");
    return 0;
}
