#include<stdio.h> 
#include<stdlib.h>
//#include<malloc.h>
union stu
	{
		int no;
		float score;	
		char name[20];
	};
	
int main()
{
	union stu *p1,*p2,*p;
	p1=(union stu*)malloc(sizeof(union stu));
	printf("请输入学生学号：\n");
	scanf("%d",&p1->no);
	printf("请输入学生成绩：\n");
	p2=(union stu*)malloc(sizeof(union stu));
	scanf("%f",&p2->score);
	printf("请输入学生姓名：\n");
	p=(union stu*)malloc(sizeof(union stu));
	scanf("%s",p->name);
	printf("%d\t%f\t%s\n",p1->no,p2->score,p->name);
		return 0;
}
