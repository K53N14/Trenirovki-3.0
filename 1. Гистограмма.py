text = []
with open('input.txt', 'r') as f:
    for line in f:
        text.append(line.strip())
text = ''.join(text)
ansdct = {}
maxval = 0
for char in text:
    if char != ' ':
        if char not in ansdct.keys():
            ansdct[char] = 0
        ansdct[char] += 1
        if ansdct[char] > maxval:
            maxval = ansdct[char]

sorteddict = sorted(ansdct.keys())

for i in range(maxval, 0, -1):
    nowline = []
    for key in sorteddict:
        if ansdct[key] >= i:
            nowline.append('#')
        else:
            nowline.append(' ')
    print(''.join(nowline))

print(''.join(sorteddict))

