def put_word_in_list():
    global word_counts
    word_list = open("PandP.txt", encoding="latin-1").read().split()
    for word in word_list:
        if word in word_counts.keys():
            word_counts[word] += 1
        else:
            word_counts[word] = 1

def top10(L):
    L.sort()
    return L[-10:]

def get_top_10(word_counts):
    temp_freq = {v: k for k, v in word_counts.items()}
    temp_freq = sorted(temp_freq.items(),reverse = True)
    res = []
    for i in range(10):
        res.append(temp_freq[i][1])
    return res


if __name__ == '__main__':
    word_counts = {}
    put_word_in_list()
    # print(word_counts)
    print(top10([10,8,9,7,4,8,7,7,3,56,768,1,1,1,1,1,1,3,4,7,76543,7654,7654,76,23,876,234,8]))
    print(get_top_10(word_counts))

