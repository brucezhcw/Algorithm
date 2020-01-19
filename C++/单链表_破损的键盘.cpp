
#include <cstdio>
#include<cstring>
#include<ctime>
using namespace std;
const int maxn=100000+5;
int last,cur,next[maxn];
char s[maxn];
int main()
{
while(scanf("%s",s+1)==1)
{
	int n=strlen(s+1);
	last=cur=0;
	next[0]=0;
	for(int i=1;i<=n;i++)
	{
		char ch=s[i];
		if(ch=='[')cur=0;
		else if(ch==']')cur=last;
		else
		{
			next[i]=next[cur];
			next[cur]=i;
			if(cur==last)last=i;
			cur=i;
		}
	}
	for(int i=next[0];i!=0;i=next[i])
		printf("%c",s[i]);
	printf("\n");
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

