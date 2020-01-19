#include<cstdio> 
//#include<cstdlib>
#include<queue>
//#include<algorithm>
using namespace std;
int main()
{
	queue<int> s;
	int a[]={1,2,3,4,5,6};
	for(int i=0;i<6;i++)
	s.push(a[5-i]);
	for(int i=0;i<6;i++)
	{
		int x=s.front();s.pop();
		printf("%d",x);
	}
		return 0;
}
