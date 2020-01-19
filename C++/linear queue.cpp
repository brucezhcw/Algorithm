#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

using namespace std;

char s[20];
int q;

class node
{
	public:
		int data;
		node* next;
		node* front;
};
class linear
{
	public:
		linear();
		~linear();
		void push_front(int x);
		void push_back(int x);
		void pop_front();
		void pop_back();
		void reverse();
		int max();
	private:
		node* f;
		node* e;
};

linear::linear()
{
	f = NULL;
	e = NULL;
}
linear::~linear(){
	while (f != NULL)
	{
		node* p = f;
		f = f->next;
		delete p;
	}
	e = NULL;
}
void linear::push_front(int x)
{
	node* p = new node();
	p->data = x;
	p->next = f;
	p->front = NULL;
	if (f != NULL)
		f->front = p;
	f = p;
	if (p->next == NULL)
		e = p;
}
void linear::push_back(int x)
{
	node* p = new node();
	p->data = x;
	p->front = e;
	p->next = NULL;
	if (e != NULL)
		e->next = p;
	e = p;
	if (p->front == NULL)
		f = p;
}
void linear::pop_front()
{
	node* p = f;
	if (f != NULL)
	{
		f = f->next;
		if (f != NULL)
			f->front = NULL;
		else
			e = NULL;
		delete p;
	}
}
void linear::pop_back()
{
	node* p = e;
	if (e != NULL)
	{
		e = e->front;
		if (e != NULL)
			e->next = NULL;
		else
			f = NULL;
		delete p;
	}
}
void linear::reverse()
{
	int tmp;
	node *p, *q;
	p = f;
	q = e;
	while (p != NULL && p != q)
	{
		tmp = p->data;
		p->data = q->data;
		q->data = tmp;
		p = p->next;
		q = q->front;
	}
}
int  linear::max()
{
	int tmp;
	if (f != NULL)
	{
		tmp = f->data;
		node* p = f->next;
		while (p != NULL)
		{
			if (p->data > tmp)
				tmp = p->data;
			p = p->next;
		}
		return tmp;
	}
	return -1;
}


int main() {
	scanf("%d\n", &q);
	linear sequence;
	while (q--) {
		scanf("%s", s);
		//write your code
		if (s[0] == 'r')
			sequence.reverse();
		else if (s[0] == 'm')
			cout << sequence.max() << endl;
		else if (s[4] == 'f')
			sequence.pop_front();
		else if (s[4] == 'b')
			sequence.pop_back();
		else if (s[5] == 'f')
		{
			int x = 0;
			scanf("%s", s);
			char* p = s;
			while (*p != '\0' && *p >= '0' && *p <= '9')
			{
				x *= 10;
				x += *p - '0';
				p++;
			}
			sequence.push_front(x);
		}
		else if (s[5] == 'b')
		{
			scanf("%s", s);
			int x = 0;
			char* p = s;
			while (*p != '\0' && *p >= '0' && *p <= '9')
			{
				x *= 10;
				x += *p - '0';
				p++;
			}
			sequence.push_back(x);
		}
	}
	return 0;
}
