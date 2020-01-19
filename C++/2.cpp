#include<cstdio>
#include<ctime>
#include <iostream>
//#include<cstring>
using namespace std;
class A
{
    public:
       void setA(int);
       void showA();
    private:
       int a;
};
class B
{
    public:
       void setB(int);
       void showB();
	private:
       int b;
};
class C : public A, private B
{
   public:
       void setC(int, int, int);
       void showC();
   private:
       int c;
};
void  A::setA(int x)
{   a=x;  }
void A::showA()
{ printf("%d  \n",a);}
void B::setB(int x)
{   b=x;  }
void B::showB()
{cout<<b<<'\n';}
void C::setC(int x, int y, int z)
{   
     setA(x); 
     setB(y); 
     c=z;
}
void C::showC()
{
	showA();
	showB();
	cout<<c<<'\n';
}
int main()
{	
	 C obj;
     obj.setA(5);
     obj.showA();
     obj.setC(6,7,9);
     obj.showC();
	printf("\ntime used with  %f   second\n",(double)clock()/CLOCKS_PER_SEC);
	return 0;
}
