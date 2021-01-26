koszyk_items = [ 'mleko', 'czekolada', 'sok', 'piwo' ]
koszyk_ilosc = [2, 1, 3, 6]
koszyk_cena_item = [30, 40, 20, 6]

suma = 0.0
for idx in range(len(koszyk_items)):
    item = koszyk_items[idx]
    ile = koszyk_ilosc[idx]
    cena = koszyk_cena_item[idx] * ile
    # if ile > 2 and item == 'mleko':
    #     print('znizka dla mleka')
    print("{0} {1} {2}".format(item, ile, cena))
    suma = suma + cena

print("Wartosc koszyka {0} przed znizka".format(suma))
if len(koszyk_items) > 3:
    suma = suma - (suma *5)/100

if 'mleko' in koszyk_items and 'czekolada' in koszyk_items:
    print('Znizka!')
    suma = suma - (suma * 10)/100

print("Wartosc koszyka {0} po znizka".format(suma))
