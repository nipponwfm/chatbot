import re

def removeAccents(text):
    text = re.sub(u"[àáảãạâấầậẫẩăắặằẳặ]", 'a', text)
    text = re.sub(u"[éèẹẻẽêếềệểễ]", 'e', text)
    text = re.sub(u"[ìíịĩỉ]", 'i', text)
    text = re.sub(u"[òóỏọõôổỗổồốơớờởợỡ]", 'o', text)
    text = re.sub(u"[ùúụủũưựữửừứ]", 'u', text)
    text = re.sub(u"[ýỹỷỳỵ]", 'y', text)
    text = re.sub(u"[đ]", 'd', text)
    return text

def tokenization(text):
    return text.split()

def normalize(text):
    text = text.lower()
    text = removeAccents(text)
    return text

def getBag(sentence, VOCABULARY):
    result = []
    list_sentence = sentence.split(" ")
    for x in range(len(VOCABULARY)): result.append(0)
    for word in list_sentence:
        if word in VOCABULARY: result[VOCABULARY.index(word)] += 1
    return result