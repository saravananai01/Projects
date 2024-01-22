#include <iostream>

using namespace std;

class clgfees
{
  private:
    int fees;
  public:
      clgfees()
    {
      cout <<"Enter Your Name ";
      string name;
      cin >> name;
      cout <<"Welcome To The Fees Detaile's \n"<< name;
      }
      void setfees(int f)
      {
          fees=f;
      }
      int getfees()
      {
          return fees;
      }

      int getfeesprint()
      {

          cout << fees;
      }
       void setfeesprint1()
      {
          cout << fees;
      }
};

int main()
{
    clgfees cf;
    cout <<"  Enter Your Fees";
    int f;
    cin >> f;
    cf.setfees(f);
    cf.getfees();
    cout << cf.getfees() << endl;
    cf.getfeesprint();
    cf.setfeesprint1();
    return 0;
}
