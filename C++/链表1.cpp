#include<stdio.h> 
#include<stdlib.h>
//#include<malloc.h>
struct stu
	{
		int no;
		float score;	
		struct stu*next;	
	};
	
int main()
{
	int i,n=0;
	struct stu*head=0,*p1,*p2,*p;
	p2=p1=(struct stu*)malloc(sizeof(struct stu));
	printf("请输入学生学号,成绩：\n");
	scanf("%d%f",&p1->no,&p1->score);
		while(p1->no!=0)
		{
			n=n+1;
			if(n==1)head=p1;
			else p2->next=p1;
			p2=p1;
			p1=(struct stu*)malloc(sizeof(struct stu));
			scanf("%d%f",&p1->no,&p1->score);
		}
		p2->next=NULL;
			p=head;
		while(p!=0)
		{
			printf("%-10d%10.2f\n",p->no,p->score);
			p=p->next;
		}
		return 0;
}
