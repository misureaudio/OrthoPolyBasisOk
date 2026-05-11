"""LAYER 4 — Quadrature orchestrator for Chebyshev polynomials."""
from __future__ import annotations
from typing import List, Callable, Tuple
import math
import numpy as np

def clencurt(n: int) -> Tuple[np.ndarray, np.ndarray]:
    if n == 0: return np.array([0.0]), np.array([2.0])
    if n == 1: return np.array([1.0, -1.0]), np.array([1.0, 1.0])
    theta = np.pi * np.arange(n + 1) / n
    nodes = np.cos(theta)
    c = np.zeros(n + 1)
    c[0::2] = 2.0 / (1.0 - np.arange(0, n + 1, 2) ** 2)
    v = np.concatenate([c[:n], c[n:n+1], c[n-1:0:-1]])
    w_full = np.real(np.fft.ifft(v))
    weights = np.zeros(n + 1)
    weights[0], weights[n] = w_full[0], w_full[n]
    weights[1:n] = 2.0 * w_full[1:n]
    return nodes, weights

def clencurt_quadrature(f: Callable[[float], float], n: int) -> float:
    nodes, weights = clencurt(n)
    return float(np.sum(weights * f(nodes)))

class ChebyshevQuadrature:
    def get_extrema_points(self, n: int) -> List[float]:
        if n < 0: return []
        if n == 0: return [0.0]
        return [math.cos(k * math.pi / n) for k in range(n + 1)]

    def clenshaw_curtis_quadrature(self, f: Callable[[float], float], n: int) -> float:
        return clencurt_quadrature(f, n)
    
    def integrate_on(self, f: Callable[[float], float], a: float, b: float, n: int = 32) -> float:
        """General purpose integrator for any finite interval [a, b]."""
        return clencurt_integrate_interval(f, a, b, n)

# Convenience aliases for orchestrators
clenshaw_curtis_integrate = clencurt_quadrature

def map_nodes_to_interval(nodes: np.ndarray, a: float, b: float) -> np.ndarray:
    """Linearly maps nodes from [-1, 1] to [a, b]."""
    return 0.5 * (b - a) * nodes + 0.5 * (b + a)

def clencurt_integrate_interval(f: Callable[[float], float], a: float, b: float, n: int = 32) -> float:
    """
    Integrates f(t) from a to b using Clenshaw-Curtis quadrature.
    Correctly scales the weights and maps the nodes.
    """
    if a == b: return 0.0
    
    # 1. Get canonical nodes and weights
    nodes_canonical, weights_canonical = clencurt(n)
    
    # 2. Map nodes to the new interval
    nodes_mapped = map_nodes_to_interval(nodes_canonical, a, b)
    
    # 3. Scale result by the Jacobian ( (b-a)/2 )
    # Integral_{a}^{b} f(t) dt = [(b-a)/2] * Sum( w_i * f(t_i) )
    jacobian = 0.5 * (b - a)
    return jacobian * np.sum(weights_canonical * f(nodes_mapped))