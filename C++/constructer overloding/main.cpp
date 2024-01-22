#include <iostream>

using namespace std;

class constructersample
{

public :

      constructersample()
      {
          cout << "Welcome To The Class's... ";
      }
      constructersample(string name)
      {
          cout << "Welcome To The " << name;
      }

    };

int main()
{
    constructersample cse,cse1;
    string Name;
    cin >> Name;
    cse.constructersample(string Name);
    return 0;
}
