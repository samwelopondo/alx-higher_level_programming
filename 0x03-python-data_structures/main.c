#include <stdio.h>

/**
 * main - Entry point
 *
 * Return: Always 1 (Error)
 */
int main(void)
{
	char ch = 'a';
    int len = ch + 26;

    int cap1 = ch - 32;
    int len1 = cap1 + 26;

    while(ch < len)
    {
        if (ch == 'q' || ch == 'e')
        {
            ch++;
            continue;
        }
        putchar(ch++);
 
    }
    putchar('\n');

    while(cap1 < len1)
    {
        if (ch == 'Q' || ch == 'e')
        { ch++;   continue;}
        putchar(cap1++);
    }

    putchar('\n');
    return (0);
}
