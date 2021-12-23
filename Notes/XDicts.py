def make_letter_counts_dict(phrase):
    """Return dict of letters and # of occurrences in phrase."""

    letter_counts = {}

    for letter in phrase:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
        print("letter", letter,"letter_counts[letter]",letter_counts[letter], "letter_counts.get(letter, 0)",letter_counts.get(letter, 0) )
    return letter_counts

phrase = 'delicious knishes'
make_letter_counts_dict(phrase)