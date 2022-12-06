import sys

new = ''
filePath = './tmp.txt'
exception = ['【','［','「','『','〈','〝']
lineChange = '\n\n'
with open(filePath, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i, l in enumerate(lines):
        old = l.strip()
        if i == len(lines)-1:
            lineChange = ''

        if old:
            if old[0] in exception:
                new += old + lineChange
            else:
                new += '　'+old + lineChange
        else:
            new += lineChange

with open('./tmp2.txt', 'w', encoding='utf-8') as f:
    f.write(new)

# pyinstaller 명령어: pyinstaller -w -F NovelConverter.py