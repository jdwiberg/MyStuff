#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    {
        int s;
        do
        {
            s = get_int("What is the starting size of the population?\n");
        }
        while (s < 9);


    // TODO: Prompt for end size

        int e;
        do
        {
            e = get_int("What is the ending size of the population?\n");
        }
        while (e <= s);

    // TODO: Calculate number of years until we reach threshold

        int t = 0;
        do
        {
            s = (s + (s / 3) - (s / 4));
            t++;
        }
        while (s < e);

    // TODO: Print number of years
        printf("It will take %i years.\n", t);
    }
}


