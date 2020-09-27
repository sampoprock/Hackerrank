# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# For better understanding, see the image below:

# banana.png

# Your task is to determine the winner of the game and their score.

# Input Format

# A single line of input containing the string .
# Note: The string  will contain only uppercase letters: .

# Constraints



# Output Format

# Print one line: the name of the winner and their score separated by a space.

# If the game is a draw, print Draw.

# Sample Input

# BANANA
# Sample Output

# Stuart 12


def minion_game(string):

    string=string.upper()

    ss,ks=0,0

    for i in range(len(string)):
        k=len(string)-i

        if s[i] in 'AEIOU':
            ks+=k
        else:
            ss+=k
    

    if ss>ks:
        print("Stuart", ss)
    elif ks>ss:
        print("Kevin", ks)
    else:
        print("Draw")

    # your code goes here

if __name__ == '__main__':