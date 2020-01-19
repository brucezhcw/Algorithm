#include<stdio.h>
#include<time.h>
#include<string.h>
#define max 1010
int main()
{
	int n,a[max],b[max],kase=0;
	while(scanf("%d",&n)==1&&n)
	{
		printf("Game %d:\n",++kase);
		for(int i=0;i<n;i++)
		 scanf("%d",&a[i]);
		  for(;;)
		  {
		   int A=0,B=0;
		    for(int i=0;i<n;i++)
			{
				scanf("%d",&b[i]);
				if(a[i]==b[i])
					A++;
			}
			if(b[0]==0)	break;
			for(int d=1;d<=9;d++)
			{
				int c1=0,c2=0;
				for(int i=0;i<n;i++)
				{
					if(a[i]==d)c1++;
					if(b[i]==d)c2++;
				}
				if(c1<c2)
				  B+=c1;
				else
				  B+=c2;
			}
			printf("    (%d,%d)\n",A,B-A);
		  }
	}

	printf("\ntime used=%.6f\n",(double)clock()/CLOCKS_PER_SEC);
	return 0;
}
	//FILE *out;
	//out=fopen("data.ddt","w+");
	//fprintf(out,"%d  %d  %.3f \n",min,max,(double)s/n);
	//fprintf(out,"\ntime used=%.6f\n",(double)clock()/CLOCKS_PER_SEC);
	//fclose(out);
