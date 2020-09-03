import numpy as np


def check_number(nr):
    global x
    global y
    text = 'First number: '

    if nr == 2:
        text = 'Second number: '
    
    while True:
        try:
            a = input(text)
            float(a)
        except ValueError:
            print("Not a number")
            continue
        else:                                
            break
    if nr == 1:
        x = float(a)
    else:
        y = float(a)

def check_symbol():
    global symbol
    while True:
        symbol = input("Math operation: ")
        if symbol == "+" or symbol == "-" or symbol == "*" or symbol == "/":
            break
        else:
            print("Not a math operation")

def get_result(x, y, symbol):
    global result     
    if symbol=="+":
        result = x+y
    if symbol=="-":
        result = x-y
    if symbol=="*":
        result = x*y
    if symbol=="/":
        result = x/y

def math():
    global history_elem
    try:
        result
    except NameError:
        check_number(1)
        check_symbol()
        check_number(2)
        get_result(x, y, symbol)  
        history_elem = np.array([x, y, symbol, result])      
    else:
        t = result
        check_symbol()
        check_number(2)
        get_result(result, y, symbol)
        history_elem = np.array([t, y, symbol, result]) 

def main():     
    a=0  
    while True:
        a += 1
        math() 

        if a==1:
            history = np.array([history_elem]);  
        else:
            history = np.append(history, [history_elem], 0)
        print(history)

        again = input('Another calculation? (Y/N)')
        if again == "N" or again == "n":
            break

main()
