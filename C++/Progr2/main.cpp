#include <iostream>

using namespace std;


int main()
{
    int x[10][20] =
    {
    {1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},
    {1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},
    {1,0,0,0,0,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1},
    {1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},
    {1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},
    {1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1},
    {1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1},
    {1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0},
    {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},
    {1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1}
    };

    for(int i = 0; i < 10; i++)
    {
        for(int c = 0; c < 20; c++)
        {
            if(x[i][c] == 1)
            {
                cout << "0";
                cout << "0";
            }
            else
            {
                cout << "  ";
            }
        }
        cout << endl;
    }
    return 0;

}