#include<stdio.h> 
#include<stdlib.h>
//#include<malloc.h>
enum stu
	{
		y,e,s,w,l,q
	};
	
int main()
{
	enum stu m;
	scanf("%d",&m);
	switch(m)
	{
		case y: printf("%s","1");break;
		case e: printf("%s","2");break;
		case s: printf("%s","3/4");break;
		case w: printf("%s","5");break;
		case l: printf("%s","6");break;
		case q: printf("%s","7");break;
		default: break;
	}
		return 0;
}
