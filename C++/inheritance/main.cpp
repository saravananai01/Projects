#include <iostream>

using namespace std;

class Bike
    {
    private:
        string BkBrand;
        string BkModel;
        string Bkprice;


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
class sportsbikes :public Bkprice39t{
};

int main()
{
    sportsbikes sb;
    sb.setbikebrand();
    sb.setbikemodel();
    sb.setbkprice();
    cout <<"Ready To Race>>" << sb.getbikebrand() << endl;
    cout <<"Your BikeModel" << sb.getbikemodel() << endl;
    cout <<"Your BikePrice"<< sb.getbkprice() << endl;
    return 0;
}
