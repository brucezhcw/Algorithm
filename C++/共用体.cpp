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
	printf("������ѧ��ѧ�ţ�\n");
	scanf("%d",&p1->no);
	printf("������ѧ���ɼ���\n");
	p2=(union stu*)malloc(sizeof(union stu));
	scanf("%f",&p2->score);
	printf("������ѧ��������\n");
	p=(union stu*)malloc(sizeof(union stu));
	scanf("%s",p->name);
	printf("%d\t%f\t%s\n",p1->no,p2->score,p->name);
		return 0;
}
