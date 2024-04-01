## This method approximates the root of a continuous function in a initial, pre determined, interval [a, b] by splitting this interval in half while still containing the real root in it, the size of the interval determines the precision of the approximation.
## Ideally the initial interval [a, b] should contain no more than 1 root and it should be as small as reasonably possible initially for better results.
import matplotlib.pyplot as plt

##Tweaks##
step = 0.0001
roundfor = 10
a = -1
b = 1
max_it = 100
precision = 0.0001
actual_root_in_range_x = (-3)/2 + ((1)*(13**(1/2)))/2 ## Still will be wrong because computers
plt.plot([0,0], [0,0], color = 'red', label = 'divisions')
def f(x):
    return(x**2 + x*3 - 1)

def whereRoot(a, b):
    midpoint = a + (b - a)/2
    if(f(a) * f(midpoint) < 0):
        return('left')
    elif(f(b) * f(midpoint) < 0):
        return('right')
    else:
        return('spotOn!')

img_f = []
dom_f = []
rangeab = b - a
i = a

while(i <= b):
    img_f.append(round(f(i), roundfor))
    dom_f.append(round(i, roundfor))
    i += step

plt.plot([a,b], [0,0], color = "black", label = "x-axis")
plt.plot(dom_f, img_f, color = "red", label = "(x, f(x))")
plt.plot([0,0], [min(img_f), max(img_f)], color = 'black', label = 'y-axis')

k = 0
while(k < max_it and rangeab > precision):
    k += 1
    ##print("Iteracao:", k)
    
    midpoint = a + (b - a)/2
    ##print(whereRoot(a, b))
    if(whereRoot(a, b) == 'right'):
        a = midpoint
        plt.plot([midpoint,midpoint], [min(img_f), max(img_f)],'--', color = 'red')
        rangeab = (a+b)/2
    elif(whereRoot(a, b) == 'left'):
        b = midpoint
        plt.plot([midpoint,midpoint], [min(img_f), max(img_f)],'--',color = 'red')
        rangeab = (a+b)/2
    ##print("[~~~~~~~~~~~~~~~~~~]")

plt.plot([a,b], [0, 0], color = 'blue', label = 'Final estimate')
plt.plot(actual_root_in_range_x, 0, '.', label = 'Actual Root', color = 'black')
print("Actual root:  X =", round(actual_root_in_range_x, 5))
print("Interval containing X: [" + str(round(a, 5)) + ', ' + str(round(b, 5)) + ']')
print("Approx root: ~X =", round((a+b)/2, 5))
print('Relative error:', round((((((a+b)/2) - actual_root_in_range_x)**2)**(1/2))/actual_root_in_range_x, 5))
plt.legend()
plt.show()