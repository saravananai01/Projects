#include <iostream>

using namespace std;

int main()
{
    int a=30,b=50;
    cout << "Value Of A              : " << a << endl;
    cout << "Addes Of The A          : " << &a << endl;
    cout << "Value Of B              : " << b << endl;
    cout << "Addes Of The B          : " << &b << endl;
    cout << "---------------------------" << endl;
    int *s=&b;
    cout << "Value Of S              : " << s << endl;
    cout << "Addes Of The S          : " << &s << endl;
    cout << "Stored Addes Of The *S  : " << *s << endl;
    cout << "---------------------------" << endl;
    int **k=&s;
    cout << "Value Of K              : " << k << endl;
    cout << "Addes Of The K          : " << &k << endl;
    cout << "Stored Addes Of The **K : " << **k << endl;
    cout << "---------------------------" << endl;
    void *v=&a;
    cout << "Value Of K              : " << v << endl;
    cout << "Addes Of The K          : " << &v << endl;
    cout << "Stored Addes Of The **K : " << *(int*)v << endl;

    return 0;

}
