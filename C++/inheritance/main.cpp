#include <iostream>

using namespace std;

class Bike
    {
    private:
        string BkBrand;
        string BkModel;
        string Bkprice;
        string Bkkm;


    public:

    void setbikebrand()
    {
        cout <<"Enter Your BikeName : ";
        cin >> BkBrand;
    }

    string getbikebrand()
    {
        return BkBrand;
    }
     void setbikemodel()
    {
        cout <<"Enter Your BikeModels : ";
        cin >> BkModel;
    }

    string getbikemodel()
    {
        return BkModel;
    }
};

class Bkprice39t:public Bike
{
    public:
        string p="Bkprice";
    void setbkprice()
    {
        cout <<"Enter Your BikePrice : ";
        cin >> p;
    }

    string getbkprice()
    {
        return p;
    }
};
class sportsbikes :public Bkprice39t
{
    public:
    string A="Bkkm";

    void setflp()
    {
        cout <<"Enter Your BikeKm/h :";
        cin >> A;

        if(A=="5000Km")
        {
            cout << "Your BikeKm/h " + A + "Your Fule Price" <<endl;
        }
        else
        {
            cout << "Your Bike Km/h" + A + "Your Fule Price" <<endl;
        }

    }

    string getflp()
    {
        return A;
    }

};

int main()
{
    sportsbikes sb;
    sb.setbikebrand();
    sb.setbikemodel();
    sb.setbkprice();
    sb.setflp();
    cout <<"Ready To Race>>" << sb.getbikebrand() << endl;
    cout <<"Your BikeModel" << sb.getbikemodel() << endl;
    cout <<"Your BikePrice"<< sb.getbkprice() << endl;
    cout << "Your Your BikeKm/h " <<sb.getflp() << endl;
    return 0;
}
