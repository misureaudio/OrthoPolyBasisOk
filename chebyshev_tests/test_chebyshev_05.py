# Test: Integrate f(t) = t^2 from 0 to 10. 
# Analytical result: [t^3/3] from 0 to 10 = 1000/3 = 333.333...
from chebyshev.integration import ChebyshevQuadrature, clencurt_integrate_interval
f = lambda t: t**2
result = clencurt_integrate_interval(f, 0, 10, 32)
print(f"Result: {result:.15f}") 
# Result: 333.333333333333314 (Perfect!)