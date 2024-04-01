## This method approximates the root of a continuous function in a initial, pre determined, interval [a, b] by splitting this interval in half while still containing the real root in it, the size of the interval determines the precision of the approximation.
## Ideally the initial interval [a, b] should contain no more than 1 root and it should be as small as reasonably possible initially for better results.

def f(x):
    return(x**2 + x*3 + 4)

print(f(10))