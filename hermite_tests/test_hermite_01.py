from hermite.symbolic import HermiteSymbolic

H4 = HermiteSymbolic(4)
print(H4.expression) # 16x^4 - 48x^2 + 12
print(H4.evaluate(0)) # 12