#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <memory.h>
#include <windows.h>
#include <gl/gl.h>
using namespace std;
template <class T>
void bubble(T *item,int count)
{
	int i,j; 
	T t;
	for(i=1;i<count;i++) 
		for(j=count-1;j>=i;j--)
		if(item[j-1]>item[j])
		{
			t=item[j-1];
			item[j-1]=item[j];
			item[j]=t;
		}
}
int main()
{ 	
	char str[]="HUTREADHGKLP"; 
	bubble(str,strlen(str));
	cout<<"the sorted string is"<<str<<endl;
	int nums1[]={4,7,2,9,3,7,6,1};
	bubble(nums1,8);
	cout<<"the sorted numbers are";
	for(int i(0);i<8;i++)
	cout<<nums1[i]<<"  ";
	cout<<endl; 
	double nums2[]={2.3,5.3,6.7,3.9,7.2,15};
	bubble(nums2,6);
	cout<<"the sorted numbers are";
	for(int i(0);i<6;i++)
	cout<<nums2[i]<<"  ";
	cout<<endl;
	return 0;
}


