import numpy as np

# Kepler's Third Law to Find T (Orbital Period Value) Based on a (Semi-Major Axis Value)
def find_orbital_period(semi_major_axes):
    """
    Calculate the orbital period
    T = sqrt(a^3)
    
    Parameters:
    semi_major_axes: Semi-major axes of the planets
    
    Returns:
    np.array: Orbital period
    """
    return np.sqrt(np.array(semi_major_axes)**3)