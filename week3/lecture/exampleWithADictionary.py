sheLovesYou = [
'She', 'loves', 'you', 'yeah', 'yeah', 'yeah', 'She', 'loves', 'you', 'yeah', 'yeah', 'yeah', 'She', 'loves', 'you',
'yeah', 'yeah', 'yeah', 'You', 'think', 'you', 've', 'lost', 'your', 'love', 'Well', 'I', 'saw', 'her',
'yesterday-yi-yay', 'It\'s', 'you' 'she\'s', 'thinking', 'of', 'And', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',
'She', 'says', 'she', 'loves', 'you', 'And', 'you', 'know', 'that', 'can\'t', 'be', 'bad', 'Yes', 'she', 'loves', 'you',
'And', 'you', 'know', 'you', 'should', 'be', 'glad', 'She', 'said', 'you', 'hurt', 'her', 'so', 'She', 'almost', 'lost',
'her', 'mind', 'And', 'now', 'she', 'says', 'she', 'knows', 'You\'re', 'not', 'the', 'hurting', 'kind', 'She', 'says',
'she', 'loves', 'you', 'And', 'you', 'know', 'that', 'can\'t', 'be', 'bad', 'Yes', 'she', 'loves', 'you', 'And', 'you',
'know', 'you', 'should', 'be', 'glad', 'Oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah', 'She', 'loves', 'you',
'yeah', 'yeah', 'yeah', 'With', 'a', 'love', 'like', 'that', 'You', 'know', 'you', 'should', 'be', 'glad', 'You',
'know', 'it\'s', 'up', 'to', 'you', 'I', 'think', 'it\'s', 'only', 'fair', 'Pride', 'can', 'hurt', 'you', 'too',
'Apologize', 'to', 'her', 'Because', 'she', 'loves', 'you', 'And', 'you', 'know', 'that', 'can\'t', 'be', 'bad', 'Yes',
'she', 'loves', 'you', 'And', 'you', 'know', 'you', 'should', 'be', 'glad', 'Oo', 'she', 'loves', 'you', 'yeah', 'yeah',
'yeah', 'She', 'loves', 'you', 'yeah', 'yeah', 'yeah', 'With', 'a', 'love', 'like', 'that', 'You', 'know', 'you',
'should', 'be', 'glad', 'With', 'a', 'love', 'like', 'that', 'You', 'know', 'you', 'should', 'be', 'glad', 'With', 'a',
'love', 'like', 'that', 'You', 'know', 'you', 'should', 'be', 'glad', 'Yeah', 'yeah', 'yeah', 'Yeah', 'yeah', 'yeah',
'yeah']


"""
creating frequency dictionary mapping str:int
"""
def lyricsToFrequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

beatles = lyricsToFrequencies(sheLovesYou)
print(beatles)

"""
find the word that occur the most and how many times
"""
def mostCommonWords(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return words, best

"""
find the word that occur at least X times
"""
def wordsOften(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = mostCommonWords(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

print(wordsOften(beatles, 5))