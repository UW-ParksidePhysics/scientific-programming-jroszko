import numpy as np
import matplotlib.pyplot as plt


def stress(strains, youngs_modulus):
    return youngs_modulus * strains


def strain(stresses, youngs_modulus):
    return stresses / youngs_modulus


def read_webpage():
    return webdata


def calculate_stress_and_strain(youngs_moduli, yield_strengths):
    stresses = []
    strains = []
    for index in range(len(youngs_moduli)):
        yield_strength = yield_strengths[index]
        E = youngs_moduli[index]
        maximum_strain = strain(yield_strength, E)
        deltaL = np.linspace(0, maximum_strain)
        epsilon = deltaL / L
        strains.append(epsilon)
        sigma = E * epsilon
        stresses.append(sigma)
    return stresses, strains


def plot_stress_strain(stresses, strains):
    for epsilon, sigma in zip(strains, stresses):
        plt.plot(epsilon, sigma)
    plt.show()
    return


youngs_moduli = np.array([2.9 * 10 ** 9, 2.5 * 10 ** 9])
yield_strengths = [50 * 10 ** 6, 63 * 10 ** 6]
L = 10
