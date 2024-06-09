import random
import math

def is_int(num_samples):
    return num_samples.isnumeric()

def calc_abs(y, y_hat):
    return abs(y - y_hat)

def calc_square(y, y_hat):
    return (y - y_hat)**2

def calc_regression_loss():
    num_samples = input('Input number of samples (integer number) which are generated: ')
    if is_int(num_samples) == False:
        print('number of samples must be an integer number')
        return
    
    loss_name = input('loss_name: ')

    num_samples = int(num_samples)
    final_loss = 0

    for i in range(num_samples):
        y = random.uniform(0,10)
        y_hat = random.uniform(0,10)

        if loss_name == 'MAE':
            loss = calc_abs(y, y_hat)
        elif loss_name == 'MSE'or loss_name == 'RMSE':
            loss = calc_square(y, y_hat)
        final_loss += loss
        
        print(f'loss name: {loss_name}, sample: {i}, pred: {y}, target: {y_hat}, loss: {loss}')
    
    final_result = final_loss/num_samples
    if loss_name == 'RMSE':
        final_result = math.sqrt(final_result)
    print(f'{loss_name}: {final_result}')

calc_regression_loss()
