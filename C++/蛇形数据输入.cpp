#include<stdio.h>
#include<time.h>
#include<string.h>
#define max 20
int a[max][max];
int main()
{
	int n,x,y,tot=0;
	scanf("%d",&n);
	memset(a,0,sizeof(a));
	tot=a[x=0][y=n-1]=1;
	while(tot<n*n)
	{
		while(x+1<n&&!a[x+1][y])
			a[++x][y]=++tot;
		while(y-1>=0&&!a[x][y-1])
			a[x][--y]=++tot;
		while(x-1>=0&&!a[x-1][y])
			a[--x][y]=++tot;
		while(y+1<n&&!a[x][y+1])
			a[x][++y]=++tot;
	}
	for(x=0;x<n;x++)
	{
		for(y=0;y<n;y++)
		printf("%4d",a[x][y]);
		printf("\n");
	}
	printf("\ntime used=%.6f\n",(double)clock()/CLOCKS_PER_SEC);
	return 0;
}
	//FILE *out;
	//out=fopen("data.ddt","w+");
	//fprintf(out,"%d  %d  %.3f \n",min,max,(double)s/n);
	//fprintf(out,"\ntime used=%.6f\n",(double)clock()/CLOCKS_PER_SEC);
	//fclose(out);
