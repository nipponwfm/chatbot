import json
import random
from nlp import normalize, getBag, tokenization

URL = 'intents.json'
TAGS = []
VOCABULARY = []
TAG_PATTERN = []
DATUM = []

def readFile(url):
    with open(url, encoding='utf-8') as FILE:
        JSON = json.load(FILE)
        for data in JSON:
            DATUM.append(data)
            tag = data['tags']
            TAGS.append((tag, 0))
            for pattern in data['patterns']:
                _pattern = normalize(pattern)
                VOCABULARY.extend(tokenization(_pattern))
                TAG_PATTERN.append((tag, _pattern))
def training(inputBag):
    dup_tag_pattern = TAG_PATTERN.copy()
    dup_tags = TAGS.copy()
    #calculate the rate of each tags
    for pattern in TAG_PATTERN:
        hit = 0
        patternLength = len(pattern[1].split(" "))
        patternBag = getBag(pattern[1], VOCABULARY)
        for index in range(len(inputBag)):
            if (inputBag[index] == patternBag[index]
                or inputBag[index] and patternBag[index]): hit += patternBag[index]
        index = TAGS.index((dup_tag_pattern[dup_tag_pattern.index(pattern)][0], 0))
        if pattern[0] == dup_tags[index][0]:
            tmp = list(dup_tags[index])
            tmp[1] += hit/patternLength
            dup_tags[index] = tuple(tmp)
    #find BIGGEST rate
    max = 0.5
    index = -1
    for i in range(len(dup_tags)):
        if dup_tags[i][1] > max:
            max = dup_tags[i][1]
            index = i
    #response
    if index == -1: print("AI : Xin lỗi tôi không hiểu")
    else:
        responseLength = len(DATUM[index]['response'])
        print("AI: ",DATUM[index]['response'][random.randrange(0, responseLength)])
        if index == 1: return 0
        else: return 1

readFile(URL)
print('Chào mừng đến với ChatBot!\n')
while True:
    userInput = input("You: ")
    userInput = normalize(userInput)
    inputLength = len(userInput.split(" "))
    inputBag = getBag(userInput, VOCABULARY)
    if not training(inputBag): break
print('ChatBot kết thúc...')