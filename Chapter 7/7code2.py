from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import re
import string

def cleanInput(input):
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def ngrams(input, n):
    input = cleanInput(input)
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i : i + n])
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
ngrams1 = ngrams(content, 2)
ngrams = {}
for i in ngrams1:
    j = str(i)
    ngrams[j] = ngrams.get(j, 0) + 1

ngrams = OrderedDict(sorted(ngrams.items(), key = lambda t : t[1], reverse = True))
fp = open("ngrams.txt", "w")
ngrams = str(ngrams)
fp.write(ngrams)
fp.write("2-grams count is : " + str(len(ngrams)))
fp.close()
#print(ngrams)
#print("2-grams count is : " + str(len(ngrams)))
