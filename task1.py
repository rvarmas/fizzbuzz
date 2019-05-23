f = open('list1.txt')
f1 = open('output.txt', 'a')

Copythefileline=False

for line in f.readlines():

    if 'tests/file/myword' in line:
        Copythefileline=True

    if Copythefileline:
        f1.write(line)

f1.close()
f.close()
