rm#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// each of our text files contains 1000 words
#define LISTSIZE 1000

// values for colors and score (EXACT == right letter, right place; CLOSE == right letter, wrong place; WRONG == wrong letter)
#define EXACT 2
#define CLOSE 1
#define WRONG 0

// ANSI color codes for boxed in letters
#define GREEN "\e[38;2;255;255;255;1m\e[48;2;106;170;100;1m"
#define YELLOW "\e[38;2;255;255;255;1m\e[48;2;201;180;88;1m"
#define RED "\e[38;2;255;255;255;1m\e[48;2;220;20;60;1m"
#define RESET "\e[0;39m"

// user-defined function prototypes
string get_guess(int wordsize);
int check_word(string guess, int wordsize, int status[], string choice);
void print_word(string guess, int wordsize, int status[]);

int main(int argc, string argv[])
{
    // ensure proper usage
    // TODO #1
    if (argc != 2)
    {
        printf("Usage: ./wordle wordsize\n");
        return 1;
    }

    int wordsize = 0;

    // ensure argv[1] is either 5, 6, 7, or 8 and store that value in wordsize instead
    // TODO #2
    wordsize = atoi(argv[1]);
    if (wordsize < 5 || wordsize > 8)
    {
        printf("Error: wordsize must be 5, 6, 7, or 8\n");
        return 1;
    }

    // open correct file, each file has exactly LISTSIZE words
    char wl_filename[6];
    sprintf(wl_filename, "%i.txt", wordsize);
    FILE *wordlist = fopen(wl_filename, "r");
    if (wordlist == NULL)
    {
        printf("Error opening file %s.\n", wl_filename);
        return 1;
    }

    // load word file into an array of size LISTSIZE
    char options[LISTSIZE][wordsize + 1];

    for (int i = 0; i < LISTSIZE; i++)
    {
        fscanf(wordlist, "%s", options[i]);
    }

    // pseudorandomly select a word for this game
    // make sure it does not repeat any letter (this would cause bug)
    srand(time(NULL));
    int repcount = 0;
    string choice;
    do
    {
        choice = options[rand() % LISTSIZE];
        for (int c = 0; c < wordsize; c++)
        {
            for (int c2 = 0; c2 < wordsize; c2++)
            {
                if (choice[c] == choice[c2])
                {
                    repcount++;
                }
            }
        }
    }
    while (repcount > wordsize);

    // allow one more guess than the length of the word
    int guesses = wordsize + 1;
    bool won = false;

    // print greeting, using ANSI color codes to demonstrate
    printf(GREEN "This is WORDLE50" RESET "\n");
    printf("You have %i tries to guess the %i-letter word I'm thinking of\n", guesses, wordsize);

    // main game loop, one iteration for each guess
    int score;
    for (int i = 0; i < guesses; i++)
    {
        // obtain user's guess
        string guess = get_guess(wordsize);

        // array to hold guess status, initially set to zero
        int status[wordsize];

        // set all elements of status array initially to 0, aka WRONG
        // TODO #4

        for (int ini = 0; ini < wordsize; ini++)
        {
            status[ini] = 0;
        }

        // Calculate score for the guess
        score = check_word(guess, wordsize, status, choice);

        printf("Guess %i: ", i + 1);

        // Print the guess
        print_word(guess, wordsize, status);

        // if they guessed it exactly right, set terminate loop
        if (score == EXACT * wordsize)
        {
            won = true;
            break;
        }
    }

    // Print the game's result
    // TODO #7

    if (score == wordsize * 2)
    {
        printf("You won!\n");
    }
    else
    {
        printf("Sorry, the secret word was %s\n", choice);
    }
    // that's all folks!
    return 0;
}

string get_guess(int wordsize)
{

    // ensure users actually provide a guess that is the correct length
    // TODO #3

    string guess;
    do
    {
        guess = get_string("Input a %i-letter word: ", wordsize);
    }
    while (strlen(guess) != wordsize);
    return guess;
}

int check_word(string guess, int wordsize, int status[], string choice)
{
    // compare guess to choice and score points as appropriate, storing points in status
    // TODO #5
    int score = 0;
    for (int spot = 0; spot < wordsize; spot++)
    {
        if (guess[spot] == choice[spot])
        {
            status[spot] += EXACT;
            score += status[spot];
        }
        else
        {
            for (int spot2 = 0; spot2 < wordsize; spot2++)
            {
                if (guess[spot] == choice[spot2])
                {
                    status[spot] = CLOSE;
                    score += status[spot];
                }
            }
        }
    }


    return score;
}

void print_word(string guess, int wordsize, int status[])
{
    // print word character-for-character with correct color coding, then reset terminal font to normal
    // TODO #6

    for (int spt = 0; spt < wordsize; spt++)
    {
        if (status[spt] == EXACT)
        {
            printf(GREEN "%c", guess[spt]);
        }
        else if (status[spt] == CLOSE)
        {
            printf(YELLOW "%c", guess[spt]);
        }
        else
        {
            printf(RED "%c", guess[spt]);
        }
    }

    printf(RESET "\n");
    return;
}
