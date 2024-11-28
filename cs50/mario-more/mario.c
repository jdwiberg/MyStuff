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

    // Print Pyramid
    //Set "m" modifier to 0
    int m = 0;
    //Set "x" (spaces) to (h - 1)
    int x = (h - 1);
    //Set "y" (hashtags) to (h - (h - 1))
    int y = (h - (h - 1));
//Print x spaces
    do
    {
        if (m < (h - 1))
        {
            do
            {
                printf(" ");
                x--;
            }
            while (x > (0 + m));
        }
        else
        {
            printf("");
        }
        x = (h - 1);
//Print y #'s
        do
        {
            printf("#");
            y++;
        }
        while (y < h - (h - 1) + m + 1);
        y = (h - (h - 1));

        //Print space
        printf("  ");

        //Print y #'s
        do
        {
            printf("#");
            y++;
        }
        while (y < h - (h - 1) + m + 1);
        y = (h - (h - 1));

        //Print \n and m++
        printf("\n");
        m++;
    }
    while (m < h);
}