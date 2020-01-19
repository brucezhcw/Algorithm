#include <stdio.h>
#include <stdlib.h>
int step = 0;
FILE *fp;
void move(char x, char y)
{

	if (step % 5 == 0)
		printf("\n");
	printf("%c-->%c\t", x, y);
	fprintf(fp, "%c-->%c\t", x, y);
	step++;

}
void hanoi(int n, char one, char two, char three)
{
	if (n == 1)
		move(one, three);
	else
	{
		hanoi(n - 1, one, three, two);
		move(one, three);
		hanoi(n - 1, two, one, three);
	}

}

int main()
{
	int m, n = 1;
	errno_t err;
	if (err = fopen_s(&fp, "C:\\Users\\20600\\Desktop\\c.txt", "a+") != 0)
	{
		printf("failed to open the file\n\n"); return 1;
	}
	while (n == 1)
	{
		step = 0;
		printf("��������������\n");
		scanf_s("%d", &m);
		printf("�ƶ� %d �����ӵĲ��裺", m);
		hanoi(m, 'A', 'B', 'C');
		printf("\n�ƶ�������%d\n", step);
		printf("������ѡ������:1;��ֹ��ѡ�������������ּ� !\n");
		scanf_s("%d", &n);
	}
	return 0;
}


