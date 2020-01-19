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
		printf("请输入盘子数：\n");
		scanf_s("%d", &m);
		printf("移动 %d 个盘子的步骤：", m);
		hanoi(m, 'A', 'B', 'C');
		printf("\n移动步数：%d\n", step);
		printf("继续请选择数字:1;终止请选择其他任意数字键 !\n");
		scanf_s("%d", &n);
	}
	return 0;
}


