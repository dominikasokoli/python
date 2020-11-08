produkt = {'SS12': {'nazwa': 'sukienka_trojka', 'rozmiary': ['s', 'l', 'xl']},
            'P12': {'nazwa': 'spodnie', 'rozmiary': ['s', 'xl']}
          }

for id in produkt:
    p = produkt[id]
    rozmiary = p['rozmiary']
    #print(p)
    #print(rozmiary)
    print(p['nazwa'])
    for r in rozmiary:
        print(r)



#statusy = {'Konta' : {'obecny_status': 'Aktywny', 'poprzedni_status': 'Pauza'},
#            'Subskrypcji' : {'obecny_status_sub': 'Aktywny', 'poprzedni_status_sub': 'Aktywny'}
#            }

#for id in statusy:
#    s = statusy[id]
#    print(s)
#    print(s['obecny_status'], ['obecny_status_sub'])
