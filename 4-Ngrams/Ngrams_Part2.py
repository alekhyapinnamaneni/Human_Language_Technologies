# Alekhya Pinnamaneni
# axp190109
# CS 4395.001

import pickle
import pathlib
import nltk
from nltk import word_tokenize
from nltk.util import ngrams


# computes probability using Laplace smoothing
def probability(line, unigram_dict, bigram_dict, v):
    tokens = word_tokenize(line)
    bigrams = list(ngrams(tokens, 2))
    prob = 1
    for bigram in bigrams:
        n = bigram_dict[bigram] if bigram in bigram_dict else 0
        d = unigram_dict[bigram[0]] if bigram[0] in unigram_dict else 0
        prob = prob * ((n + 1) / (d + v))
    return prob


if __name__ == "__main__":
    # open and read in pickled dictionaries
    unigrams_english = pickle.load(open('unigrams_english.pickle', 'rb'))
    bigrams_english = pickle.load(open('bigrams_english.pickle', 'rb'))
    unigrams_french = pickle.load(open('unigrams_french.pickle', 'rb'))
    bigrams_french = pickle.load(open('bigrams_french.pickle', 'rb'))
    unigrams_italian = pickle.load(open('unigrams_italian.pickle', 'rb'))
    bigrams_italian = pickle.load(open('bigrams_italian.pickle', 'rb'))

    # read in test file
    with open(pathlib.Path.cwd().joinpath('LangId.test'), 'r') as f:
        lines = f.read().splitlines()

    f = open('LangId.results', 'w')
    vocab_size = len(unigrams_english) + len(unigrams_french) + len(unigrams_italian)
    for line in lines:
        # calculate probability of each language
        english_prob = probability(line, unigrams_english, bigrams_english, vocab_size)
        french_prob = probability(line, unigrams_french, bigrams_french, vocab_size)
        italian_prob = probability(line, unigrams_italian, bigrams_italian, vocab_size)

        # write to results file based on which language has the highest probability
        if english_prob > french_prob and english_prob > italian_prob:
            result = str(lines.index(line) + 1) + " English\n"
        elif french_prob > english_prob and french_prob > italian_prob:
            result = str(lines.index(line) + 1) + " French\n"
        else:
            result = str(lines.index(line) + 1) + " Italian\n"
        f.write(result)
    f.close()

    # compare predicted and correct classifications to get accuracy and incorrect items
    with open(pathlib.Path.cwd().joinpath('LangId.sol'), 'r') as f:
        sol_lines = f.read().splitlines()
    with open(pathlib.Path.cwd().joinpath('LangId.results'), 'r') as f:
        result_lines = f.read().splitlines()
    correct = 0
    incorrect = []
    for i in range(len(sol_lines)):
        if sol_lines[i] == result_lines[i]:
            correct += 1
        else:
            incorrect.append(i + 1)
    print('Accuracy = ', round((correct / len(sol_lines)) * 100, 2), '%', sep='')
    print('Incorrectly classified lines: ', incorrect)
