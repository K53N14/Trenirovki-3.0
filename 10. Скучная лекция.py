word = input()
letters = {}
for i in range(len(word)):
    if word[i] not in letters.keys():
        letters[word[i]] = 0
    letters[word[i]] += (i + 1) * (len(word) - i)

letterssorted = sorted(letters.keys())

for key in letterssorted:
    print(f'{key}:',letters[key])