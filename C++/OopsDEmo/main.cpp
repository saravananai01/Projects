#include <iostream>

using namespace std;

int main()
{
    string name;
    cout <<"Enter Your Name :" << endl;
    cin >> name;
    cout << name << endl;
    fflush(stdin);
    cout <<"Enter Your Name :" << endl;
    getline(cin,name);
    cout << name << endl;

    string firstname;
    string lastname;
    cin >> firstname >> lastname;
    cout << firstname +" "


    return 0;
}





























/*
namespace Bike
{
    string BikeName="Mt15";

}

namespace Bike1
{
    string BikeName="Duke";

}

using namespace Bike;

int main()
{
   cout << BikeName << endl;

   cout << Bike1::BikeName << endl;
   return 0;
}
*/
