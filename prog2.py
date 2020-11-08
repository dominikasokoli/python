samochody = ['syrena', 'polonez']
print(samochody[0])
print(samochody[1])

for s in samochody:
    print(s)
for idx in range( len(samochody)) :
    print("idx: " + str(idx) + " : " + samochody[idx])

print("len: {0}" .format(len(samochody)))
print("range: {0}" .format(range(3)))

for idx in range( len(samochody)):
    print("{0} {1}" .format(idx, samochody[idx]))
