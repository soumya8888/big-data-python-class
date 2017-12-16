import argparse
from string import ascii_letters
from operator import itemgetter

# Build my Parser with help for user input
parser = argparse.ArgumentParser()
parser.add_argument('msg', help='Message to count letters in')
parser.add_argument('--letters', '-l',  help='Frequency of letters',
            action='store_true',dest='letters', default=None)
parser.add_argument('--bigrams', '-b',  help='Frequency of bigrams',
            action='store_true',dest='bigrams', default=None)
parser.add_argument('--trigrams', '-t',  help='Frequency of trigrams',
            action='store_true',dest='trigrams', default=None)
args = parser.parse_args()
args = parser.parse_args()

if args.letters:
    letter_dict = {}
    for letter in args.msg:
        if letter in ascii_letters:
            try:
                letter_dict[letter] += 1
            except KeyError:
                letter_dict[letter] = 1

    print "="*5, 'Letters', "="*5
    for letter in sorted(letter_dict.items(), key=itemgetter(1), reverse=True):
        print letter

if args.bigrams:
    bigram_dict = {}
    bigram_holder = []
    for letter in args.msg:
        if letter not in ascii_letters:
            bigram_holder = []
            continue
        else:
            bigram_holder.append(letter)

        if len(bigram_holder) == 2:
            bigram = bigram_holder[0] + bigram_holder[1]
            try:
                bigram_dict[bigram] += 1
            except KeyError:
                bigram_dict[bigram] = 1

            last = bigram_holder.pop()
            bigram_holder = []
            bigram_holder.append(last)

    print "="*5, 'Bigrams', "="*5
    for bigram in sorted(bigram_dict.items(), key=itemgetter(1), reverse=True):
        print bigram

if args.trigrams:
    trigram_dict = {}
    trigram_holder = []
    for letter in args.msg:
        if letter not in ascii_letters:
            trigram_holder = []
            continue
        else:
            trigram_holder.append(letter)

        if len(trigram_holder) == 3:
            trigram = trigram_holder[0] + trigram_holder[1] + trigram_holder[2]
            try:
                trigram_dict[trigram] += 1
            except KeyError:
                trigram_dict[trigram] = 1

            l1 = trigram_holder.pop()
            l2 = trigram_holder.pop()
            trigram_holder = []
            trigram_holder.append(l2)
            trigram_holder.append(l1)

    print "="*5, 'Trigrams', "="*5
    for trigram in sorted(trigram_dict.items(), key=itemgetter(1), reverse=True):
        print trigram