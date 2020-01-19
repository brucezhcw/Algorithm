#include<iostream>
//#include<vector>
//#include<queue>
#include <cstdio>
//#include<set>
#include<ctime>
//#include<algorithm>
//#include<cstdlib>
#include<cstring>
#include<cctype>
using namespace std;
class complex	
{
public:	
	complex(double r=0.0,double i=0.0){real=r;imag=i;}                                                              //¹¹Ôìº¯Êý
	complex operator + (complex c2); 
	complex operator - (complex c2); 
	void display();	
private:
	double real;
	double imag;
};	
complex complex::operator +(complex c2) 
{
	complex c;
	c.real=c2.real+real;
	c.imag=c2.imag+imag;
	return c;                                      //return complex(c.real,c.imag);   
}
complex complex::operator -(complex c2)  
{
	complex c;
	c.real=real-c2.real;
	c.imag=imag-c2.imag;
	return c;                                      //return complex(c.real,c.imag);
}
void complex::display()
{   cout<<"("<<real<<","<<imag<<")"<<endl; }
int main()
{
	complex c1(5,4),c2(2,10),c3;  
	cout<<"c1="; c1.display();
	cout<<"c2="; c2.display();
	c3=c1-c2;	
	cout<<"c3=c1-c2=";
	c3.display();
	c3=c1+c2;	
	cout<<"c3=c1+c2=";
	c3.display();
	printf("time used with %f second\n",(float)clock()/CLOCKS_PER_SEC);
	return 0;
}
