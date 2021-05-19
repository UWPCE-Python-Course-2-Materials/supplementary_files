import numpy

def f(x):
    return x**2

def integrate(f, a, b, N):
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx

def integrate_numpy(f, a, b, N):
    '''
    Source: https://helloacm.com/how-to-compute-numerical-integration-in-numpy-python/
    '''
    x = numpy.linspace(a+(b-a)/(2*N), b-(b-a)/(2*N), N)
    fx = f(x)
    area = numpy.sum(fx)*(b-a)/N
    return area
