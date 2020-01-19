#include<stdio.h>
void quiksort(int a[],int low,int high)
{
	int i = low;
	int j = high;
	int temp = a[i];
	if( i < j)
	{
		while(i < j)
		{
			while((a[j] >= temp)&&(i < j))
				{
					j--;
				}
				a[i] = a[j];
			while((a[i] <= temp) && (i < j))
				{
					i++;
				}
				a[j]= a[i];
		}
		a[j] = temp;				//		a[i] = temp; 
		quiksort(a,low,i-1);
		quiksort(a,j+1,high);
	}
	else
		{
			return;
		}
}
int main()
{
	int i,arry[14];
	printf("please enter an array include 14 int numbers\n");
	for(i=0;i<14;i++)
	scanf("%d",arry+i); 
	quiksort(arry,0,13);
	for(i=0;i<14;i++)
		{
			printf("%d ",arry[i]);
		}
	printf("\n");
	return 0;
} 
