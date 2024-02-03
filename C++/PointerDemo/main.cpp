#include <iostream>

using namespace std;

int main()
{
    int a=30,b=50;
    cout << "Value Of A                : " << a << endl;
    cout << "Address Of The A          : " << &a << endl;
    cout << "Value Of B                : " << b << endl;
    cout << "Address Of The B          : " << &b << endl;
    cout << "____________________________" << endl;
    int *s=&b;
    cout << "Value Of S                : " << s << endl;
    cout << "Address Of The S          : " << &s << endl;
    cout << "Stored Address Of The *S  : " << *s << endl;
    cout << "____________________________" << endl;
    int **k=&s;
    cout << "Value Of K                : " << k << endl;
    cout << "Addres Of The K           : " << &k << endl;
    cout << "Stored Address Of The **K : " << **k << endl;
    cout << "____________________________" << endl;
    void *v=&a;
    cout << "Value Of K                : " << v << endl;
    cout << "Address Of The K          : " << &v << endl;
    cout << "Stored Address Of The **K : " << *(int*)v << endl;
    cout << "____________________________" << endl;

    return 0;


}
