# Alekhya Pinnamaneni
# axp190109
# CS 4395.001

import sys
import pathlib
import pickle
import nltk
from nltk import word_tokenize
from nltk.util import ngrams


# extracts unigram and bigram dictionaries from text
def ngram(filename):
    with open(pathlib.Path.cwd().joinpath(filename), 'r') as f:
        text = ''.join(f.read().splitlines())
    tokens = word_tokenize(text)
    unigrams = list(ngrams(tokens, 1))
    bigrams = list(ngrams(tokens, 2))
    unigram_dict = {t: unigrams.count(t) for t in set(unigrams)}
    bigram_dict = {b: bigrams.count(b) for b in set(bigrams)}
    return unigram_dict, bigram_dict


if __name__ == "__main__":
    unigrams_english, bigrams_english = ngram("LangId.train.English")
    unigrams_french, bigrams_french = ngram("LangId.train.French")
    unigrams_italian, bigrams_italian = ngram("LangId.train.Italian")

    # pickle unigram and bigram dictionaries
    pickle.dump(unigrams_english, open('unigrams_english.pickle', 'wb'))
    pickle.dump(bigrams_english, open('bigrams_english.pickle', 'wb'))
    pickle.dump(unigrams_french, open('unigrams_french.pickle', 'wb'))
    pickle.dump(bigrams_french, open('bigrams_french.pickle', 'wb'))
    pickle.dump(unigrams_italian, open('unigrams_italian.pickle', 'wb'))
    pickle.dump(bigrams_italian, open('bigrams_italian.pickle', 'wb'))
