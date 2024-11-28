#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long cc;

    cc = get_long("Card Number: ");

    long first = cc;
    do
    {
        first = (first / 10);
    }
    while (first >= 10);

//Validty Equation
    long concc = cc;
    long m = 10;
    int r;
    int x = 1;
    int s = 0;

    while (cc >= 1)
    {
        r = (cc % m);

        //Double every other number
        //If the number is more than 9, -9
        if (x < 0)
        {
            r *= 2;
            if (r > 9)
            {
                r -= 9;
            }
        }
        //Take digit and add on to pile
        s = (s + r);

        cc = (cc / m);
        x *= -1;
    }
    //Check to see if sum is divisible evely by 10
    s = (s % 10);
    if (s != 0)
    {
        printf("INVALID\n");
    }
    else
    {
        cc = (concc);

    //If 34 or 37 and 15 digits, execute amex code

        if ((cc > 340000000000000 && cc < 349999999999999) || (cc > 370000000000000 && cc < 379999999999999))
        {
            printf("AMEX\n");
        }

//If 51-55 and 16 digits, execute mc code

        else if ((cc > 5100000000000000) && (cc < 5599999999999999))
        {
            printf("MASTERCARD\n");
        }
//If 4 and within 13-16 digits, execute code for visa
        else if ((first == 4) && (cc >= 4000000000000) && (cc <= 4999999999999999))
        {
            printf("VISA\n");
        }
//If none, print invalid
        else
        {
            printf("INVALID\n");
        }
    }
}