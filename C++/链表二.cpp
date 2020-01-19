#include<stdio.h> 
#include<stdlib.h>
//#include<malloc.h>
struct node 
	{
		int date;
		struct node*next;	
	};
int search_k(struct node *list,int k)
{
	int count=0;
	struct node*p,*q;
	p=q=list->next;
	while(p!=NULL)
		{
			if(count<k)	count ++;
			else q=q->next;
			p=p->next;
		}
		if(count<k)	{printf("error!\n"); return 0;}
		else {printf("%d\n",q->date); return 1;}
}
int main()
{
	int n;
	struct node *p,*q,*head;
	head=q=p=(struct node*)malloc(sizeof(struct node));
	p=(struct node*)malloc(sizeof(struct node));
	q->next=p;
	q=p;
	printf("ÇëÊäÈëÊý¾Ý\n");
	scanf("%d",&p->date);
	while((p->date)!=000)
	{
	p=(struct node*)malloc(sizeof(struct node));
	scanf("%d",&p->date);
	q->next=p;
	q=p;
	}
	q->next=NULL;
		n=search_k(head,6);
		free(head); 
		printf("%d",n);
		return 0;
}
