import numpy as np
import matplotlib.pyplot as plt


def stress(strains, youngs_modulus):
    return youngs_modulus * strains


def strain(stresses, youngs_modulus):
    return stresses / youngs_modulus


youngs_moduli = np.array([2.9 * 10 ** 9, 2.5 * 10 ** 9])
yield_strengths = [50 * 10 ** 6, 63 * 10 ** 6]
L = 10
maximum_strain = 10
deltaL = np.linspace(0, maximum_strain)

for index in range(len(youngs_moduli)):
    yield_strength = yield_strengths[index]
    E = youngs_moduli[index]
    maximum_strain = strain(yield_strength, E)
E_polyester = 10
maximum_strain = strain(yield_strength, E_polyester)
deltaL = np.linspace(0, maximum_strain)
L = 10
epsilon = deltaL / L
E = E_polyester
sigma = E * epsilon
plt.plot(epsilon, sigma)

E_nylon = 2.5 * 10 ** 9
deltaL = np.linspace(0, 25.2)
L = 10
epsilon = deltaL / L
E = E_nylon
sigma = stress(epsilon, E)
plt.plot(epsilon, sigma)
plt.show()
