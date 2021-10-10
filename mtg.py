import nltk
import numpy as np

# corpus = nltk.corpus.gutenberg.raw('austen-sense.txt')
# corpus = nltk.word_tokenize(corpus.lower())

'''
- make dictionary with key = word, value = # of times word appears in corpus
- if n = 3, start with last 2 words in sentence
- if deterministic = True, choose word with highest probability
- if deterministic = False, 
CHECK: if n = 1
'''

'''takes starting section and text and returns dictionary with appreances of word following section'''
def make_dictionary(sentence, corpus, n):
    dic = {}
    lst = []
    # start = sentence[-(n-1):]
    for i in range(0, len(corpus)):
        section = corpus[i:i+(n-1)]
        if section == sentence[-(n-1):]:
            next = corpus[i+(n-1)]
            lst.append(next)
    for item in lst:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    return dic

def backoff(original, matching, n):
    while n > 1:
        dictionary = make_dictionary(original, matching, n)
        if dictionary == {}:
            n -= 1
        elif dictionary != {}:
            return max(dictionary, key = dictionary.get)    
    return np.random.choice(matching)



def next_word(original, matching, n):
    dictionary = make_dictionary(original, matching, n)
    if len(dictionary) == sum(dictionary.values()):
        return next(iter(dictionary))
    else:
        return max(dictionary, key = dictionary.get)

'''Final function to put things together'''
def finish_sentence(sentence, n, corpus, deterministic = False):
    final_lst = sentence
    while final_lst[-1] not in "?!." and len(final_lst) < 15:
        if deterministic == True:
            final_lst.append(next_word(sentence, corpus, n))
        elif deterministic == False:
            final_lst.append(backoff(sentence, corpus, n))
    return final_lst



# sentence = ["she", "was", "not"]
# n = 3
# deterministic = True
# results = ["she", "was", "not", "in", "the", "world", "."]

