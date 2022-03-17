from random import choice

def losowanko():
    losowanie_pci = [0,1]
    losowanie_pci = choice(losowanie_pci)
    if losowanie_pci == 1:
        przymiotniki_m = open('./lista_slow/przymiotniki-m.txt', 'r').read()
        przymiotniki_m = przymiotniki_m.splitlines()

        rzeczowniki_m = open('./lista_slow/rzeczowniki-m.txt', 'r').read()
        rzeczowniki_m = rzeczowniki_m.splitlines()

        przymiotnik = choice(przymiotniki_m)
        rzeczownik = choice(rzeczowniki_m)

        #print(przymiotnik, rzeczownik)

    else:
        przymiotniki_w = open('./lista_slow/przymiotniki-w.txt', 'r').read()
        przymiotniki_w = przymiotniki_w.splitlines()

        rzeczowniki_w = open('./lista_slow/rzeczowniki-w.txt', 'r').read()
        rzeczowniki_w = rzeczowniki_w.splitlines()

        przymiotnik = choice(przymiotniki_w)
        rzeczownik = choice(rzeczowniki_w)

        #print(przymiotnik, rzeczownik)

    return przymiotnik, rzeczownik

print(losowanko())