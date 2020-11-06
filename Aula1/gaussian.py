from math import sqrt, pi, exp
m = 0
s = 2.
x = 1.
gaussiana = 1/(s*sqrt(2*pi))*exp(-1/2.*((x-m)/s)**2)
print(gaussiana)
