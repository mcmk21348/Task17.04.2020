str_ = input("Введите текст: ")

znaki_prepinaniya = ['.',',',':',';','!','?']

wordList = str_.split()

i = 0
for word in wordList:
    if word[-1] in znaki_prepinaniya:
        wordList[i] = word[:-1]
        word = wordList[i]
    if word[0] in znaki_prepinaniya:
        wordList[i] = word[1:]
    i += 1

print(wordList)
