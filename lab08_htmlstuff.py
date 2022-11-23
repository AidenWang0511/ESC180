import urllib.request

def choose_variant(variants):
    str1 = variants[0].split()
    str1_1 = ""
    for i in str1:
        str1_1 += i+"+"
    str1_1 = str1_1[:-1]
    url1 = 'https://ca.search.yahoo.com/search?p=' + str1_1 + '&fr=yfp-t-s&fp=1&toggle=1&cop=mss&ei=UTF-8'
    f1 = urllib.request.urlopen(url1)
    page1 = f1.read().decode("utf-8")


    str2 = variants[1].split()
    str2_1 = ""
    for i in str2:
        str2_1 += i+"+"
    str2_1 = str2_1[:-1]

    url2 = 'https://ca.search.yahoo.com/search?p=' + str2_1
    f2 = urllib.request.urlopen(url2)
    page2 = f2.read().decode("utf-8")

    tempstr = page1.split(" search results</span></h2>")
    res1 = tempstr[0].split('fz-14 lh-22">About ')
    res1 = res1[1]
    res1 = int(res1.replace(",", ""))

    tempstr = page2.split(" search results</span></h2>")
    res2 = tempstr[0].split('fz-14 lh-22">About ')
    res2 = res2[1]
    res2 = int(res2.replace(",",""))


    print("res1:",res1)
    print("res2:",res2)
    if res1>res2:
        return variants[0]
    else:
        return variants[1]





if __name__ == '__main__':

    print(choose_variant(["five-year anniversary", "fifth anniversary"]))
