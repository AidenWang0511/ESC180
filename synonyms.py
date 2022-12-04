'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 18, 2022.
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    sum = 0
    for k in vec1.keys():
        if k in vec2.keys():
            sum += vec1[k] * vec2[k]
    return sum / (norm(vec1) * norm(vec2))


def build_semantic_descriptors(sentences):
    sd = {}
    for l in sentences:
        for word in l:
            word = word.lower()
            if word not in sd.keys():
                sd[word] = {}



    pass

def build_semantic_descriptors_from_files(filenames):
    pass


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    pass


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass
