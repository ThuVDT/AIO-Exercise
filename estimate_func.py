def factorial_func(x):
    mul_result = 1
    for i in range(1, x+1):
        mul_result *= i
    return mul_result

def approx_sin(x, n):
    approx_sin_result = 0
    for i in range(0, n+1):
        approx_sin_result += (-1)**i * (x**(2*i+1))/factorial_func(2*i+1)
    print(approx_sin_result)

def approx_cos(x, n):
    approx_cos_result = 0
    for i in range(0, n+1):
        approx_cos_result += (-1)**i * (x**(2*i))/factorial_func(2*i)
    print(approx_cos_result)

def approx_sinh(x, n):
    approx_sinh_result = 0
    for i in range(0, n+1):
        approx_sinh_result += (x**(2*i+1))/factorial_func(2*i+1)
    print(approx_sinh_result)

def approx_cosh(x, n):
    approx_cosh_result = 0
    for i in range(0, n+1):
        approx_cosh_result += (x**(2*i))/factorial_func(2*i)
    print(approx_cosh_result)


approx_sin(x=3.14, n=10)
approx_cos(x=3.14, n=10)
approx_sinh(x=3.14, n=10)
approx_cosh(x=3.14, n=10)

