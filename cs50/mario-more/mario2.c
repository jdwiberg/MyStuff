#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get height
    int h;
    do
    {
        h = get_int("Height: ");
    }
    while (h < 1);

    //Build half pyramid
    int m = 0;
    int y = (h - (h - 1));
    int x = (h - 1)
    do
    {
        printf("#");
        y++;
    }
    while (y < 1 + m)


}