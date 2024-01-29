#include <iostream>

using namespace std;

class Namechecking
{

public:

      Namechecking()
      {
          cout << "\tWelcome To The Class'S... \n";
      }
      Namechecking(string Name)
      {
          cout << "Welcome To The...\n  "<<Name;
      }
      Namechecking(string Name,string Initial)
      {
          cout << "Welcome To The...\n  "<< Name + Initial;
      }
      Namechecking(string Name,string Initial,int Rnum)
      {
          cout << "Welcome To The...\n  "<< Name + Initial << Rnum;
      }
      void agechecking(string Name,string Initial,int Rnum,int age)
      {
          if(age>=20)
          {
              cout <<"You Are Eligible\n" <<Name + Initial << Rnum  << age;

          }
          else
        {
          cout <<"You Are Not Eligible\n" <<Name + Initial << Rnum << age;
          }
      }

    };


int main()
{
    Namechecking nc;
    cout << "Enter Your Name... ";
    string f_Name;
    cin >> f_Name;
    string a=f_Name;
    Namechecking nc1(a);
    cout << "\nEnter Your Initial... ";
    string f1_Name;
    cin >> f1_Name;
    string a1=f1_Name;
    Namechecking nc2(a,a1);
    cout << "\nEnter Your Registernumber... ";
    int Rnu1;
    cin >> Rnu1;
    int a2=Rnu1;
    Namechecking nc3(a,a1,a2);
    cout <<"Enter Your Age...\n";
    int age;
    cin >>age;
    int a3=age;
    nc.agechecking(a,a1,a2,a3);
    return 0;
}
