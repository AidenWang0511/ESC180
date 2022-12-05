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
            for w in l:
                if w != word:
                    if w not in sd[word].keys():
                        sd[word][w] = 1
                    else:
                        sd[word][w] += 1
    return sd

def build_semantic_descriptors_from_files(filenames):
    txt = ""
    for i in filenames:
        txt += open(i, "r", encoding = "latin1").read() + " "

    txt = txt.replace("!", ".")
    txt = txt.replace("?", ".")
    txt = txt.replace(",", " ")
    txt = txt.replace("-", " ")
    txt = txt.replace("--", " ")
    txt = txt.replace(":", " ")
    txt = txt.replace(";", " ")
    txt = txt.replace("\n", " ")

    txt = txt.split(".")
    txt.pop()

    for i in range(len(txt)):
        txt[i] = txt[i].split(" ")
        while "" in txt[i]:
            txt[i].remove("")

    return build_semantic_descriptors(txt)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    res = choices[0]
    word = word.lower()
    maxSim = -10

    if word not in semantic_descriptors:
        return res

    for i in range(len(choices)):
        choices[i] = choices[i].lower()
        simVal = -1
        if choices[i] in semantic_descriptors:
            simVal = similarity_fn(semantic_descriptors[word], semantic_descriptors[choices[i]])
        if simVal > maxSim:
            maxSim = simVal
            res = choices[i]
    return res


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    numTrue = 0
    f = open(filename, "r", encoding = "latin1").read()
    f = f.split("\n")

    questions = []
    for q in f:
        if q != "":
            questions.append(q.split(" "))

    for q in questions:
        if most_similar_word(q[0], q[2:], semantic_descriptors, similarity_fn) == q[1]:
            numTrue += 1

    return numTrue / len(questions) * 100.0


import time
st = time.time()
sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt"])
fin = time.time()
res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
print("time taken:", fin-st)
print(res, "of the guesses were correct")



