#include<cstdio>
#include<ctime>
const int maxn=80;
int n,cnt=0,L,S[maxn];
using namespace std;
bool dfs(int cur)
{
	if(cnt++==n)
	{
		for(int i=0;i<cur;i++)
		printf("%c",'A'+S[i]);
		printf("\n");
		return 0;
	}
    else for(int i=0;i<L;i++)
	{
		S[cur]=i;
		int ok=1;
		for(int j=1;j*2<=cur+1;j++)
		{
			int equal=1;
			for(int k=0;k<j;k++)
			if(S[cur-k]!=S[cur-k-j])
			{
				equal=0;
				break;
			}
			if(equal)
			{
				ok=0;
				break;
			}
		}
		if(ok&&!dfs(cur+1)) return 0;
	}
	return 1;
}
int main()
{	
	 printf("please give the number of \"n\" and \"L\" :\n");
	 scanf("%d %d",&n,&L);
	 dfs(0);
	 printf("time used with %lf second\n",(double)clock()/CLOCKS_PER_SEC);
	 return 0;
}
