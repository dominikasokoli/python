basket_items = [ 'Harry Potter', '21 lessons for 21st Century', 'Crime and Punishment', 'Python for Data Analysis' ]
basket_author = ['J.K.Rowling', 'Yuval Noah Harari', 'Fiodor Dostojewski', 'Wes McKinney' ]
basket_ilosc = [2, 1, 1, 1]
basket_price_item = [30, 40, 30, 40]
price_dictionary = {'Harry Potter': 30, '21 lessons for 21st Century': 40, 'Crime and Punishment': 30, 'Python for Data Analysis': 40}

print("Welcome to our bookstore!\nCheck our best deals:")
szer = 60
print("-" * szer)
print("| Price($)|     Author       |        Title             |")
print("*" * szer)
print("| {:7.2f} | {:18s} | {:27s} |" .format(basket_price_item[0], basket_author[0], basket_items[0]))
print("| {:7.2f} | {:18s} | {:27s} |" .format(basket_price_item[1], basket_author[1], basket_items[1]))
print("| {:7.2f} | {:18s} | {:27s} |" .format(basket_price_item[2], basket_author[2], basket_items[2]))
print("| {:7.2f} | {:18s} | {:27s} |" .format(basket_price_item[3], basket_author[3], basket_items[3]))
print("-" * szer)

print("Which book would you like to add to your basket?")
input_title = input("Please write the title ")
print("How many copies of {0} would you like to add to your basket?" .format(input_title))
input_quantity = int(input("Please write the quantity "))
print("You’ve added {0} copy/copies of {1} to your basket!" .format(input_quantity, input_title))
print("Would you like to add another book to your basket?")

customer_input = input("yes or no?")
if customer_input == "no":
    print("Thank you for shopping with us!")
    if input_title in price_dictionary:
        print("Total price for {} copy/copies of {} is".format(input_quantity, input_title), price_dictionary[input_title] * input_quantity)
        
elif customer_input == "yes":
    print("Please write the title of book you would like to buy ")
    input_title_two = input()
    print("How many copies of {0} would you like to add to your basket?" .format(input_title_two))
    input_quantity_two = int(input("Please write the quantity "))
    print("You’ve added {0} copy/copies of {1} to your basket!" .format(input_quantity_two, input_title_two))
    if input_title_two in price_dictionary:
        print("Total price for {} copy/copies of {} is".format(input_quantity_two, input_title_two), price_dictionary[input_title_two] * input_quantity_two)
    if input_title in price_dictionary:
        print("Total price for {} copy/copies of {} is".format(input_quantity, input_title), price_dictionary[input_title] * input_quantity)
        

