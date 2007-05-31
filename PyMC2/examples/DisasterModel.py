"""
A model for the D data with a changepoint

changepoint ~ U(0,111)
e ~ Exp(1.)
l ~ Exp(1.)
D[t] ~ Po(e if t <= s, l otherwise)
"""
__all__ = ['s','e','l','D']
from PyMC2 import parameter, data, node, discrete_parameter, DiscreteMetropolis
from numpy import array, log, sum, ones, concatenate, inf
from PyMC2 import uniform_like, exponential_like, poisson_like


D_array =   array([ 4, 5, 4, 0, 1, 4, 3, 4, 0, 6, 3, 3, 4, 0, 2, 6,
                    3, 3, 5, 4, 5, 3, 1, 4, 4, 1, 5, 5, 3, 4, 2, 5,
                    2, 2, 3, 4, 2, 1, 3, 2, 2, 1, 1, 1, 1, 3, 0, 0,
                    1, 0, 1, 1, 0, 0, 3, 1, 0, 3, 2, 2, 0, 1, 1, 1,
                    0, 1, 0, 1, 0, 0, 0, 2, 1, 0, 0, 0, 1, 1, 0, 2,
                    3, 3, 1, 1, 2, 1, 1, 1, 1, 2, 4, 2, 0, 0, 1, 4,
                    0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1])

# Define data and parameters

@discrete_parameter
def s(value=50, length=110):
    """Change time for rate parameter."""
    return uniform_like(value, 0, length)

@parameter
def e(value=1., rate=1.):
    """Rate parameter of poisson distribution."""
    return exponential_like(value, rate)

@parameter
def l(value=.1, rate = 1.):
    """Rate parameter of poisson distribution."""
    return exponential_like(value, rate)
        
@data(discrete=True)
def D(  value = D_array,
        s = s,
        e = e,
        l = l):
    """Annual occurences of coal mining disasters."""
    return poisson_like(value[:s],e) + poisson_like(value[s:],l)
