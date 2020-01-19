#include<iostream>
#include<vector>
#include<queue>
#include <cstdio>
#include<set>
#include<ctime>
//#include<algorithm>
using namespace std;
typedef long long LL;
const int coeff[3]={2,3,5};
int main()
{
	priority_queue<LL,vector<LL>,greater<LL> > pq;
	set<LL>s;
	pq.push(1);
	s.insert(1);
	for(int i=1;;i++)
	{
		LL x=pq.top();  pq.pop();
		printf("%10d",x);
		if(i==1500)
		{
			cout<<'\n'<<"第1500个丑数为：  \n"<<x<<endl;break;
		}
		for(int j=0;j<3;j++)
		{
			LL x2=x*coeff[j];
			if(!s.count(x2))
				{
					s.insert(x2);pq.push(x2);
					if(s.count(x2)%5==0)cout<<endl;
				}
		}
	}
	printf("time used with  %8.6f  second",(double)clock()/CLOCKS_PER_SEC);
	return 0;
}






/*
template<typename T>
struct point
{
	T x,y;
	point(T x=0,T y=0)					//:x(x),y(y)
	{
			this->x=x;
			this->y=y;
		printf("point结构体调用一次\n"); 
	}
};
int main()
{
	point<int> a(9);
	point<float> b(1.33,2.668);
	printf("%d %d\n%.2f %.2f\n",a.x,a.y,b.x,b.y);
	//cout<<a.x<<" "<<a.y<<'\n'<<b.x<<" "<<b.y<<endl;
	printf("time used with  %8.6f  second",(double)clock()/CLOCKS_PER_SEC);
	return 0;
}
*/

