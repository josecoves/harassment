import re
from collections import Counter, defaultdict

import math




def parse(line):
    #print line
    #words=re.split(' |.|. |-|/|#|,|, |\'' ,line)
    words=re.split(' |\n|\.|,|#|/|-',line)
    words=[word.lower() for word in words if(word and word[0]!='@' and word[0]!='\\' and word[0]!='&')]
    #print words
    return words

def file_2_tf_idf(file):
    print ('converting to tf-idf')
    vectors_bow = list()
    dfs = Counter()
    for line in file:
        label = int(line[0])
        document = line[1]
        vector = (label, Counter(document))
        vectors_bow.append(vector)
        dfs.update(vector[1].keys())
    D = float(len(vectors_bow))
    for token in dfs:
        dfs[token] = 1.0 / math.log(D / dfs[token])
    vectors_tfidf = list()
    for (label, bow) in vectors_bow:
        tfidf = {token: dfs[token] * count for (token, count) in bow.items()}
        vectors_tfidf.append((label, tfidf))
    print ('converted')
    return vectors_tfidf


def raw2clean(filename):
    # clean lines of tweets
    print ('cleaning')
    file=1 #=open(filename)
    with open(filename, 'r', encoding='utf8', errors='ignore') as fin:
        file=fin
    #with open(filename) as fin:
    #   file = fin.read(1888)
        clean=[]#parse(line) for line in file if (line and line[0]!='#')]
        for line in file:
            if len(clean)>10111:
                break
            if (line and line[0] != '#'):
                clean.append(parse(line))
    #for line in clean:
    #   print line
    print ('cleaned')
    return clean

def json2clean(filename):
    # clean lines of tweets
    file=open(filename)
    clean=[parse(line) for line in file if (line and line[0]!='_')]
    return clean

