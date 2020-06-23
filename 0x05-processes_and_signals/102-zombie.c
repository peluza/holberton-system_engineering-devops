#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
#include <sys/wait.h>

/**
 * infinite_while - the funtion infinite_while
 * Return: int
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Function that allows create process
 * Return: int
 */

int main(void)
{
	int my_pid = 0, count = 0, i = 5;

	while (count < i)
	{
		my_pid = fork();
		if (my_pid == 0)
			exit(0);
		else if (my_pid > 0)
			printf("Zombie process created, PID: %d\n", my_pid);
		else
			exit(1);
		count++;
	}
	infinite_while();
	return (0);
}