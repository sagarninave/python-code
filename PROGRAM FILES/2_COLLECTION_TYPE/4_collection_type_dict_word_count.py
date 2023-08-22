fhandle = open('show.txt','r')
content = fhandle.read()
contentlist = content.split()
count = 0
wordsdict = dict()
for word in contentlist:
    wordsdict[word] = wordsdict.get(word,0) + 1

print('Total Words :',count)
print(wordsdict)
