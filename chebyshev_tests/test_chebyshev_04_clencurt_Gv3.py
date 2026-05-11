from chebyshev.integration import clencurt

n_nodes, weights = clencurt(32)
s = sum(weights)

print('Nodes: %d, Weights: %d' % (len(n_nodes), len(weights)))
print('Sum of weights: %.15f' % s)
print('Error from 2.0: %.2e' % abs(s - 2.0))

# Result: 
# Nodes: 33, Weights: 33
# Sum of weights: 2.000000000000000
# Error from 2.0: 0.00e+00