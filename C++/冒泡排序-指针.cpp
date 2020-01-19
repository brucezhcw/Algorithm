#include<stdio.h> 
void sort(int *x,int n)
{
	int i,j,t;
	for(i=0;i<n-1;i++)
	{
		for(j=i+1;j<n;j++)
		if(*(x+j)>*(x+i))
		{
			t=*(x+i);
			*(x+i)=*(x+j);
			*(x+j)=t;
		}
	}
}

int main()
{
	int*p,a[10]={100,2,10,4,5,96,7,9,-23,13};
	p=a;
	sort(p,10);
	for(p=a;p<a+10;)
	{
		printf("%d  ",*p);
		p++;
	}
	printf("\n");
	return 0;
}
