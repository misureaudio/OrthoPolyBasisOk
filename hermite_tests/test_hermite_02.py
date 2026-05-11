from hermite.high_precision import HermiteMPMath

H50 = HermiteMPMath(50, dps=100)
val = H50.evaluate("2.5") # mp.mpf with 100-digit precision
print(val)