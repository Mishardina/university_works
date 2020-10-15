import pymorphy2
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
print("Введите название входного файла с исходным текстом")
inFileName = input()
fin = open(inFileName + '.txt', 'r', encoding = 'utf-8')
morph = pymorphy2.MorphAnalyzer()
i = 0
text = fin.readlines()
an_text = []
print(text)
for line in text:
    string = ''
    line = line.split()
    for word in line:
        a = morph.parse(word)
        if a[0][1].POS == 'ADVB':
            word = '>>>>' + word + '<<<< '
            string = string + word
            i += 1
        else:
            string = string + word + ' '
    string = string + '\n'
    an_text.append(string)
fin.close()
print(an_text)
print("Введите название выходного файла с проанализированным текстом")
outFileName = input()
fout = open(outFileName + '.txt', 'w')
for line in an_text:
    fout.write(line)
fout.close()
print(i)
