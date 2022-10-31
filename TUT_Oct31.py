f = open("data2.txt")
text = f.readlines()
for line in text:
    if ("lol") in line.lower():
        print(line[:-1])

def dict_to_str(d):
    res = ""
    for k,v in d.items():
        res += str(k) + ", " + str(v) + "\n"
    return res[:-1]

def dict_to_str_sorted(d):
    l = sorted(d)
    res = ""
    for k in l:
        res += str(k) + ", " + str(d[k]) + "\n"
    return res[:-1]

print(dict_to_str({1:2,2:3,5:6}))
print("--------------")
print(dict_to_str_sorted({6:2,2:3,10:6}))

