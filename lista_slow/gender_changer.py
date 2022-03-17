

przymiotniki = open('przymiotniki-m.txt', 'r').read()
przymiotniki = przymiotniki.splitlines()

for p in przymiotniki:
    p = p[:-1]
    p = p + 'a'
    print(p)