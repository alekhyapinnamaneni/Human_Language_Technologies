# Alekhya Pinnamaneni
# axp190109
# CS 4395.001

import sys
import pathlib
import re
import nltk
nltk.download('punkt')
from nltk import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from random import seed, randint


# processes raw text and returns the tokens and nouns in the text
def preprocess(text):
    # convert text to lowercase and extract tokens
    token_list = word_tokenize(text.lower())
    # remove all non-alphabetical tokens
    token_list = [t for t in token_list if re.match(r'[^\W\d]*$', t)]
    # remove all stopwords
    token_list = [t for t in token_list if t not in stopwords.words('english')]
    # remove all tokens with a length of less than 6
    token_list = [t for t in token_list if len(t) > 5]

    # extract unique lemmas from the tokens
    wnl = WordNetLemmatizer()
    unique_lemmas = set([wnl.lemmatize(t) for t in token_list])

    # do part of speech tagging and print first 20 tags
    tag_list = nltk.pos_tag(unique_lemmas)
    print('\nFirst 20 tokens and their part of speech:\n\t', tag_list[0:20])

    # extract all nouns
    nouns_list = [t for (t, pos) in tag_list if pos == 'NN']

    # print number of tokens and number of nouns
    print('\nNumber of tokens: ', len(token_list))
    print('\nNumber of nouns: ', len(nouns_list))

    # return tokens and nouns
    return token_list, nouns_list


# guessing game function    (enter '!' to exit the game)
def guessing_game(words):
    print('\n\nLet\'s play a word guessing game!')
    seed(1234)
    end = False
    while not end:  # while user has not entered '!'
        word = words[randint(0, 50)]    # select a random word
        score = 5
        guess = ''  # Represents the letter the user guessed
        output = '' # Represents the progress the user has made so far (i.e. 'w _ r _')
        goal = ''   # Represents the final goal of the user (i.e. 'w o r d')
        for i in range(len(word)):
            output += '_ '
            goal += word[i] + ' '
        # Keep guessing until score is negative or user guessed the word
        while score >= 0 and output != goal:
            print(output)
            guess = input('Guess a letter: ')
            # If user enters '!', exit the game
            if guess == '!':
                print('Ending the game. See you next time!')
                end = True
                break
            # If correct guess, increment score and update output string
            if guess in word:
                score += 1
                indices = [m.start() for m in re.finditer(guess, goal)]
                for i in indices:
                    output = output[0:i] + guess + output[i + 1:]
                print('Right! Score is ', score)
                if output == goal:
                    print(output)
                    print('You solved it!\n\nCurrent score: ', score)
            # If wrong guess, decrement score
            else:
                score -= 1
                if score < 0:
                    print('Sorry, you\'re all out of guesses. Better luck next time!\n\nCurrent  score: ', score)
                else:
                    print('Sorry, guess again, Score is ', score)
        # Continue game if user didn't enter '!'
        if not end:
            print('\nGuess another word')


if __name__ == "__main__":
    # Check if user provided file name as a sys arg and quit program if not
    if len(sys.argv) < 2:
        print("Please enter a filename as a system arg")
        quit()

    # Open and read file using file name provided in sys arg
    rel_path = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(rel_path), 'r') as f:
        raw_text = f.read()

    # Calculate and print lexical diversity
    tokens = word_tokenize(raw_text)
    lexical_diversity = len(set(tokens)) / len(tokens)
    print(f'\n\nLexical diversity: {lexical_diversity:.2f}')

    # Preprocess raw text and extract tokens and nouns
    tokens, nouns = preprocess(raw_text)

    # Create dictionary with all the nouns and their counts
    dictionary = {}
    for noun in nouns:
        dictionary[noun] = tokens.count(noun)

    # Sort dictionary from most to least frequent words
    dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    words_list = []
    # Print the 50 most frequent nouns
    print("\n50 most common nouns:")
    for noun, count in dictionary[0:50]:
        print('\t', noun, count)
        words_list.append(noun)

    # Initiates guessing game (enter '!' to exit the game)
    guessing_game(words_list)