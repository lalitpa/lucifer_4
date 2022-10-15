#include<bits/stdc++.h>
using namespace std;
int f(int n,vector<int>v)
{
    if(v[n]!=INT_MAX)
    {
        return v[n];
    }
    else if(n==0)
    {
         v[n]= 1;
    }
    else if(n<0)
    {
         v[n]= 0;
    }   
    else
    {
        v[n]=f(n-1,v)+f(n-2,v)+f(n-3,v);
    }
    return v[n];
}
int main()
{
    int dist=4;
    vector<int>v((pow(3,dist),INT_MAX));
    cout<<f(dist,v);
}