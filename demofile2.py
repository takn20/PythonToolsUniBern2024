import numpy as np
from demofile import myfun

def newfun( a ) :
    """
    A new function that uses imported function.

    Parameters
    ----------
    a : float

    Returns
    ----------
    float, half of the cosine of a
    """
    
    b = myfun( a )/2
    return b

print( newfun( np.pi ) )