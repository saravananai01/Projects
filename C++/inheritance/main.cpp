#include <iostream>

using namespace std;

class Bike
    {
    private:
        string BkBrand;
        string BkModel;


    public:

    void setbikebrand()
    {
        cout <<"Enter Your BikeName : ";
        cin >> BkBrand;
        cout <<"Ready To Race>>"<< BkBrand <<endl;
    }

    string getbikebrand()
    {
        return BkBrand;
    }
     void setbikemodel()
    {
        cout <<"Enter Your BikeModels : ";
        cin >> BkModel;
        cout <<"Ready To Race>>" <<BkModel<< endl;
    }

    string getbikemodel()
    {
        return BkModel;
    }
};

class Bkprice39t
{
    public:
    void setbkprice()
    {
        cout <<"Enter Your Bikemodelname : ";
        string Bkprice;
        cin >> Bkprice;
        cout <<"Your BikePrice" << Bkprice << endl;
    }

    string getbikeprice()
    {
        return Bkprice;
    }
};
class sportsbikes : public Bike,public Bkprice39t{
};

int main()
{
    sportsbikes sb;
    sb.setbikebrand();
    sb.setbikemodel();
    sb.setbkprice();
    return 0;
}
