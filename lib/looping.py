#!/usr/bin/env python3

def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
    
    print("Happy New Year!")

def square_integers(int_list):
    return [num * num for num in int_list]

def fizzbuzz():
    for i in range(1, 101):
        string = ''

        if i % 5 != 0 and i % 3 != 0:
            print(i)
            continue
        
        string += "Fizz" if i % 3 == 0 else ''
        string += "Buzz" if i % 5 == 0 else ''

        print(string)


# fizzbuzz()
# happy_new_year() in looping.py prints 10 to 1 countdown then "Happy New Year!" F     [ 33%]
# square_integers() in looping.py returns squared ints for [1, 2, 3, 4, 5] and [-1, -2, -3, -4, -5] F [ 66%]
#                                                                                      [ 66%]
# fizzbuzz() in looping.py prints 1 to 100 with fizz 3s, buzz 5s, fizzbuzz 3and5s F    [100%]