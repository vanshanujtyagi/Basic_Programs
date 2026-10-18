#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a1,b1,a2,b2,x,r;
    vector<int> ans1,ans2;
    string name1,name2;

    cout << "WELCOME TO AURA BATTLE!" << "\n";
    cout << "Enter both player names" << "\n";
    cin >> name1 >> name2;
    cout << "Select number of rounds: " << "\n";
    cin >> r;

    srand(time(0));
    x=rand()%1000+1;

    for (int i=1;i<=r;i++)
    {
        cout << "" << "\n";
        cout << "Round " << i << "\n";
        cout << name1 << " numbers : ";
        cin >> a1 >> b1;
        cout << name2 << " numbers : ";
        cin >> a2 >> b2;
        cout << name1 << "'s loss : " << min(abs(x-a1),abs(x-b1)) << "\n";
        cout << name2 << "'s loss : " << min(abs(x-a2),abs(x-b2)) << "\n";
        ans1.push_back(min(abs(x-a1),abs(x-b1)));
        ans2.push_back(min(abs(x-a2),abs(x-b2)));
        cout << name1 << "'s Total Loss : " << accumulate(ans1.begin(),ans1.end(),0) << "\n";
        cout << name2 << "'s Total Loss : " << accumulate(ans2.begin(),ans2.end(),0) << "\n";
        cout << "" << "\n";
    }
    
    if (accumulate(ans1.begin(),ans1.end(),0) > accumulate(ans2.begin(),ans2.end(),0))
    cout << name2 << " Wins with " << abs(accumulate(ans1.begin(),ans1.end(),0)-accumulate(ans2.begin(),ans2.end(),0))<<" points!" <<"\n";
    else if (accumulate(ans1.begin(),ans1.end(),0) == accumulate(ans2.begin(),ans2.end(),0))
    cout << "Tie" << "\n";
    else
    cout << name1 << " Wins with " << abs(accumulate(ans1.begin(),ans1.end(),0)-accumulate(ans2.begin(),ans2.end(),0))<<" points!" <<"\n";
return 0;
}
