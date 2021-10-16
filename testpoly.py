def f(x, coef):
    result = 0
    for i, val in enumerate(coef):
        result = result + (val*x**i)   # x**i is x^i
    return result

print( f(2.0,[1,2,1,5,6,7,8,9]) )
