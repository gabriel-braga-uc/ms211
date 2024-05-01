## This method approximates the root of a continuous function in a initial, pre determined, interval [a, b] by splitting this interval in half while still containing the real root in it, the size of the interval determines the precision of the approximation.
## Ideally the initial interval [a, b] should contain no more than 1 root and it should be as small as reasonably possible initially for better results.
import math
## Valores iniciais e Criterios ##
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
