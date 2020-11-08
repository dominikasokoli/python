name = input('podaj nazwe pizzy')
pizza = {'size': 'medium',
        'price': 20,
        'delivery': 2}
for key, value in pizza.items():
    print("{1}".format(key, value))

pizza['nazwa'] = name
print(pizza)
