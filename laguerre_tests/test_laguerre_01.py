from laguerre.symbolic import LaguerreSymbolic
L3 = LaguerreSymbolic(3, alpha=0.5)
print(L3.expression) # L_3^(0.5)(x) as SymPy expression
print(L3.evaluate(2)) # Evaluate at x=2