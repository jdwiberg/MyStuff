import csv
import sys

# AGATC,TTTTTTCT,AATG,TCTAG,GATA,TATC,GAAA,TCTG
def main():

    # TODO: Check for command-line usage
    if len(sys.argv) == 3:
        db = sys.argv[1]
        sq = sys.argv[2]
    else:
        print('Usage: python dna.py data.csv sequence.txt')
        sys.exit()
    if 'large.csv' in sys.argv[1]:
        dna_str = ('AGATC', 'TTTTTTCT', 'AATG', 'TCTAG', 'GATA', 'TATC', 'GAAA', 'TCTG')
    elif 'small.csv' in sys.argv[1]:
        dna_str = ('AGATC', 'AATG', 'TATC')



    # TODO: Read DNA sequence file into a variable
    with open(f'{sq}', 'r') as sequence_csv:
        sequence = csv.reader(sequence_csv)

    # TODO: Find longest match of each STR in DNA sequence
        longest_matches = []
        for n in range(len(dna_str)):
            for line in sequence:
                sequence_list = (line)
            my_seq = sequence_list[0]
            my_ref = dna_str[n]
            counter = 0
            i = 1
            while True:
                if (my_ref * i) in my_seq:
                    counter += 1
                    i += 1
                else:
                    longest_matches.append(counter)
                    break
        results = {}
        for i in range(len(dna_str)):
                results[f'{dna_str[i]}'] = longest_matches[i]


    # TODO: Check database for matching profiles

    # TODO: Read database file into a variable
    with open(f'{db}', 'r') as large_csv:
        database = csv.DictReader(large_csv)
        for line in database:
            database_list = (line)
            counter = 0
            for i in range(len(dna_str)):
                x = database_list[f'{dna_str[i]}']
                y = results[f'{dna_str[i]}']
                if f'{x}' == f'{y}':
                    counter += 1
                    if counter == len(dna_str):
                        print(database_list['name'])
                        return

    print('No match')
    return

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
