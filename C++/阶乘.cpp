#include <iostream>
#include<ctime>
#include<cstdio>
using namespace std;
int main()
{ 
	int a=0,i;
	double c=1;
	cout<<"请输入整形数据：\n"; 
	cin>>a;
		for(i=1;i<=a;i++)
		c*=i; 
	cout<<a<<" 的阶乘是 "<<c<<endl;
	printf("\ntime used with  %f   second\n",(double)clock()/CLOCKS_PER_SEC);
	return 0;
}
