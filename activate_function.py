import math

def is_number(x):
    try:
        float (x)
    except ValueError:
       return False
    return True

def sigmoid_func(x):
    return 1/(1 + math.e**(-x))

def relu_func(x):
    if x <= 0:
        return 0
    else:
        return x

def elu_func(x):
    if x <= 0:
        return 0.01*(math.e**x - 1)
    else:
        return x
    
def calc_activation_func(x, acti_func):
    result = None
    if acti_func == 'sigmoid':
      result = sigmoid_func(x)
    elif acti_func == 'relu':
      result = relu_func(x)
    elif acti_func == 'elu':
      result = elu_func(x)
    return result


def calc_activate_func():
    x = input("Input x = ")
    if is_number(x) == False:
        print('x must be a number')
        return
    
    acti_func = input("Input activation Function (sigmoid|relu|elu): ")
    if acti_func != 'sigmoid' and acti_func != 'relu' and acti_func != 'elu':
        print(f'{acti_func} is not supported')
        return 

    x = float(x)
    
    print(f'{acti_func}: f({x}) = {calc_activation_func(x, acti_func)}')

calc_activate_func()