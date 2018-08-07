# Hangman 0.2
# Jason Culligan

import random
import os

win = 1
gameswon = 0
runningtotal = 0
totgames = 0
word = ""
gallows = [
		" _______\n|/     |\n|     _O_\n|    / | \\\n|      |\n|     / \\\n|    /   \\\n|________",
		" _______\n|/     |\n|     _O_\n|    / | \\\n|      |\n|     / \\\n|\n|________",
		" _______\n|/     |\n|     _O_\n|    / | \\\n|      |\n|\n|\n|________",
		" _______\n|/     |\n|     _O_\n|    / | \\\n|\n|\n|\n|________",
		" _______\n|/     |\n|     _O_\n|\n|\n|\n|\n|________",
		" _______\n|/     |\n|      O\n|\n|\n|\n|\n|________",
		" _______\n|/     |\n|\n|\n|\n|\n|\n|________",
		" _______\n|/\n|\n|\n|\n|\n|\n|________"
]
while win == 1:
    win = 0
    used = ""
    tries = 7
    word = (random.choice(open('./wordlist.txt').readlines())).rstrip()
    os.system('clear')
    print "I've selected a word.  See if you can guess it.", word

# Print out underscores for each letter in the chosen word
    print "\n", gallows[tries], "\n", tries
    for i in word:
        print "_",

# Main loop
    while tries != 0:
        holder = ""
        print "\n"
        guess = raw_input("Pick a letter: ").lower()[:1]       
        if guess in used:
            for i in word:
                if i in used:
                    print i,
                    holder += i
                else:
                    print "_",
                    holder += "_"
            print "\n\n", "You've already used that letter.  Try a different one."
            print "\n\n", "You have", tries, "tries left"
            print "Letters used so far:", used
        else:
            used += guess
            os.system('clear')
            print "I've selected a word.  See if you can guess it.", word
            print "\n", gallows[tries], "\n", tries
            for i in word:
                if i in used:
                    print i,
                    holder += i
                else:
                    print "_",
                    holder += "_"

# WIN
            if "_" not in holder:
                print "\n\n""YOU WIN!!!!  You scored",tries, "out of 10.",2*"\n"
                gameswon += 1
                runningtotal += tries
                while True:
                    goagain = raw_input("Would you like another go? (yes or no) ").lower()
                    if goagain in ['yes', 'no', 'marmite']:
                        totgames += 1
                        break
                    else:
                        print "I don't understand that. Try 'yes' or 'no' instead."
                if goagain == "yes":
                    win = 1
                    tries = 0
                    os.system('clear')
                    break
                if goagain == "marmite":
                    print "Yep. Now you're fired.  Thanks Marmite. >:("
                    exit()
                else:
                    if gameswon == 1:
                        print "\nYou won 1 game. You got", runningtotal, "out of 10 which is", 100 * runningtotal / (totgames * 10),"%",2*"\n"
                    else:
                        print "You won", gameswon, "games. You got", runningtotal, "out of", (totgames * 10), "which is", 100 * runningtotal / (totgames * 10),"%",2*"\n"
                    exit()

            if guess not in word:
                tries -= 1
            os.system('clear')
            print "\n", gallows[tries], "\n", tries
            print "\n\n", "    You have", tries, "tries left"
            print "    Letters used so far:", used

#LOSE
    if win == 0:
        print "\n"
        print "Hard luck. The word I was thinking of was '%s'" % word, 2*"\n"
        totgames += 1
        if gameswon == 1:
            print "You won 1 game. You got", runningtotal, "out of", (totgames * 10), "which is", 100 * runningtotal / (totgames * 10),"%", 2*"\n"
            exit()
        if gameswon == 0:
            print "You got zero. Better luck next time!",2 *"\n"
        else:
            print "You won", gameswon, "games. You got", runningtotal, "out of", (totgames * 10), "which is", 100 * runningtotal / (totgames * 10),"%", 2*"\n"
        exit()
