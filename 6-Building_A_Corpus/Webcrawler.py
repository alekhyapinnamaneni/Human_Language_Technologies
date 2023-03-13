# Alekhya Pinnamaneni
# axp190109
# CS 4395.001

from bs4 import BeautifulSoup
import requests
import urllib
from urllib import request
import re
import nltk
from nltk.corpus import stopwords
import math


def crawler(url):
    r = requests.get(url)
    urls_list = []
    data = r.text
    soup = BeautifulSoup(data, features='html.parser')
    counter = 0
    for link in soup.find_all('a'):
        link_str = str(link.get('href'))
        if 'Swift' in link_str or 'swift' in link_str:
            if '&' in link_str:
                i = link_str.find('&')
                link_str = link_str[:i]
            if link_str.startswith('http') and 'google' not in link_str and 'wiki' not in link_str:
                try:
                    # works
                    html = request.urlopen(link_str)
                    urls_list.append(link_str)
                    counter += 1
                except urllib.error.HTTPError:
                    print()

        if counter >= 15:
            break
    return urls_list


def scrape(urls):
    counter = 0
    for url in urls:
        html = request.urlopen(url)
        soup = BeautifulSoup(html, features='html.parser')
        for script in soup(['script', 'style']):
            script.extract()
        text = soup.get_text()
        with open(str(counter) + '.in.txt', 'w') as f:
            f.write(text)
        counter += 1


def cleanup(in_file_name, out_file_name):
    r = open(in_file_name, 'r')
    text = r.read()
    text_chunks = [chunk for chunk in text.splitlines() if not re.match(r'^\s*$', chunk)]
    text = ' '.join(text_chunks).replace('\t', '')
    sentences = nltk.tokenize.sent_tokenize(text, language='english')
    with open(out_file_name, 'w') as f:
        for i in range(len(sentences)):
            regex = re.compile('[^a-zA-Z ]')
            sentence = sentences[i]
            sentence = regex.sub('', sentence).lower() # removes all non-alphabetical characters
            stopwords_list = stopwords.words('english')
            sentence = ' '.join(t for t in sentence.split() if t not in stopwords_list)
            sentence = ' '.join(sentence.split())
            f.write(sentence + '\n')


def tf(file_name):
    f = open(file_name, 'r')
    text = f.read()
    tokens = nltk.word_tokenize(text)
    token_set = set(tokens)
    tf_dict = {t: tokens.count(t) for t in token_set}
    for t in tf_dict.keys():
        tf_dict[t] = tf_dict[t] / len(tokens)
    return tf_dict


def tfidf(tf, idf):
    tf_idf = {}
    for t in tf.keys():
        tf_idf[t] = tf[t] * idf[t]
    return tf_idf



def top_terms():
    tf_0 = tf('0.out.txt')
    tf_1 = tf('1.out.txt')
    tf_2 = tf('2.out.txt')
    tf_3 = tf('3.out.txt')
    tf_4 = tf('4.out.txt')
    tf_5 = tf('5.out.txt')
    tf_6 = tf('6.out.txt')
    tf_7 = tf('7.out.txt')
    tf_8 = tf('8.out.txt')
    tf_9 = tf('9.out.txt')
    tf_10 = tf('10.out.txt')
    tf_11 = tf('11.out.txt')
    tf_12 = tf('12.out.txt')
    tf_13 = tf('13.out.txt')
    tf_14 = tf('14.out.txt')
    vocab = set(tf_0.keys()).union(set(tf_1.keys())).union(set(tf_2.keys())).union(set(tf_3.keys())).union(set(tf_4.keys())).union(set(tf_5.keys())).union(set(tf_6.keys())).union(set(tf_7.keys())).union(set(tf_8.keys())).union(set(tf_9.keys())).union(set(tf_10.keys())).union(set(tf_11.keys())).union(set(tf_12.keys())).union(set(tf_13.keys())).union(set(tf_14.keys()))
    idf_dict = {}
    vocab_by_topic = [tf_0.keys(), tf_1.keys(), tf_2.keys(), tf_3.keys(), tf_4.keys(), tf_5.keys(), tf_6.keys(), tf_7.keys(), tf_8.keys(), tf_9.keys(), tf_10.keys(), tf_11.keys(), tf_12.keys(), tf_13.keys(), tf_14.keys()]
    for term in vocab:
        temp = ['x' for voc in vocab_by_topic if term in voc]
        idf_dict[term] = math.log((1 + 15) / (1 + len(temp)))
    tf_idf_0 = tfidf(tf_0, idf_dict)
    tf_idf_1 = tfidf(tf_1, idf_dict)
    tf_idf_2 = tfidf(tf_2, idf_dict)
    tf_idf_3 = tfidf(tf_3, idf_dict)
    tf_idf_4 = tfidf(tf_4, idf_dict)
    tf_idf_5 = tfidf(tf_5, idf_dict)
    tf_idf_6 = tfidf(tf_6, idf_dict)
    tf_idf_7 = tfidf(tf_7, idf_dict)
    tf_idf_8 = tfidf(tf_8, idf_dict)
    tf_idf_9 = tfidf(tf_9, idf_dict)
    tf_idf_10 = tfidf(tf_10, idf_dict)
    tf_idf_11 = tfidf(tf_11, idf_dict)
    tf_idf_12 = tfidf(tf_12, idf_dict)
    tf_idf_13 = tfidf(tf_13, idf_dict)
    tf_idf_14 = tfidf(tf_14, idf_dict)


starter_url = 'https://en.wikipedia.org/wiki/Taylor_Swift'
urls = crawler(starter_url)
scrape(urls)
for i in range(15):
    cleanup(str(i) + '.in.txt', str(i) + '.out.txt')
top_terms()
