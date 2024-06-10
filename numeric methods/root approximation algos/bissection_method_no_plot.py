import math
roundfor = 100
a = 0
b = 4
max_it = 100
precision = 0.00001
## Função ##
def f(x):
    return(math.sin(x))
## Algoritmo atualiza intervalo ##
def whereRoot(a, b):
    midpoint = a + (b - a)/2
    if(f(a) * f(midpoint) < 0):
        return('left')
    elif(f(b) * f(midpoint) < 0):
        return('right')
    else:
        return('spotOn!')
rangeab = b - a
k = 0
## Algoritmo principal ##
while(k < max_it and b - a > precision):
    k += 1
    midpoint = (a + b)/2
    if(whereRoot(a, b) == 'right'):
        a = midpoint
        rangeab = (a+b)/2
    elif(whereRoot(a, b) == 'left'):
        b = midpoint
        rangeab = (a+b)/2
## Mostra Resultado ##
print(midpoint)
