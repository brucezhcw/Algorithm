#include<iostream>
#include <cstdio>
#include<ctime>
using namespace std;
const int max=1000;
int main()
{
	int i=0,k=0,g=0,count=0;
	int p[50]={5};
	do{
		k+=p[i];
		g+=p[i];
		i++;
		if(k<2&&g<4) break;
		p[i]=k/2;  k=k%2;
		p[i]+=g/4;  g=g%4;	
	}
	while(1);
	for(int j=0;j<i;j++)
	count+=p[j];
	printf("%d\n%d\n",count,i);  
	printf("time used with   %f    second\n",clock()/CLOCKS_PER_SEC);
	printf("press \"0\" to exit\n");
	while(i!=0)scanf("%d",&i);
	return 0;
}
