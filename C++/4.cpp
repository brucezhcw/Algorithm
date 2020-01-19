//#include<iostream>
#include <cstdio>
#include<ctime>
#include<cmath>
using namespace std;
const int maxn=16;
/*
bool is_prime(int i)
{
	if(i==2)return true;
	int j;
	for(j=2;j<=sqrt(i);j++)
	if(i%j==0)break;
	return j>sqrt(i);
}
*/
void dfs(int n,int *A,int cur)
{
	for(int i=0;i<cur;i++) 
		printf("%d",A[i]);
		printf("\n");
		int s=cur?A[cur-1]+1:0;
		for(int i=s;i<n;i++)
		{
			A[cur]=i;
			dfs(n,A,cur+1);
		}
}
int main()
{
	
	int n,A[maxn];
	scanf("%d",&n);
	dfs(n,A,0);
	printf("time used with %lf second\n",(double)clock()/CLOCKS_PER_SEC);
	return 0;
}
