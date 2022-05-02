import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
import lxml.html


def read_webpage(link):
    # Import material name, Young's modulus and yield strength
    webdata = pd.read_html(link)
    rope_data = webdata[6]
    rope_data.columns = rope_data.iloc[0]
    rope_data = rope_data.drop([0])
    return rope_data


def convert_dataframe_to_lists(dataframe):
    # Manipulates imported Pandas dataframe to return desired data in
    # nested list
    lists = [dataframe[np.nan].tolist()]
    quantity_headers = ["Young's  modulus  (GPa)", "Strength  (MPa)"]
    for header in quantity_headers:
        lists.append(dataframe[header].astype(float).tolist())
    return lists


def calculate_stress(strains, modulus):
    # Calculates stress from strain and Young's modulus
    stress = modulus * strains
    return stress


def calculate_strain(stress, modulus):
    # Calculates strain from stress and Young's modulus
    strain = stress / modulus
    return strain


def calculate_stress_and_strain(youngs_moduli_array, yield_strength_array, length):
    # Calculates stesses for an list of Young's moduli up to their
    # yield strengths for give rope length
    stress_array = []
    strain_array = []
    for index in range(len(youngs_moduli_array)):
        yield_strength = yield_strength_array[index]
        E = youngs_moduli_array[index]
        maximum_strain = calculate_strain(yield_strength, E)  # mm
        delta_length = np.linspace(0, maximum_strain)
        epsilon = delta_length / (length * 1000)
        strain_array.append(epsilon)
        sigma = E * epsilon
        stress_array.append(sigma)
    return stress_array, strain_array


def plot_stress_strain(stress_data, strain_data, labels):
    # Plots stress and strains with materials labels
    for epsilon, sigma, label in zip(strain_data, stress_data, labels):
        plt.plot(epsilon, sigma, label=label)
    plt.xlabel('Strain (ε)')
    plt.ylabel('Stress (σ) [GPa]')
    plt.xlim([0., np.max(strain_data)])
    plt.ylim([0., np.max(stress_data)])
    plt.legend()
    plt.show()
    return


if __name__ == '__main__':
    # Source data URL
    url = 'http://www-materials.eng.cam.ac.uk/mpsite/short/OCR/ropes/default.html'
    # Arbitrary unstretched rope length
    unstretched_length = 10  # m

    rope_dataframe = read_webpage(url)
    rope_quantity_lists = convert_dataframe_to_lists(rope_dataframe)
    rope_stresses, rope_strains = calculate_stress_and_strain(rope_quantity_lists[1], rope_quantity_lists[2], unstretched_length)
    plot_stress_strain(rope_stresses, rope_strains, rope_quantity_lists[0])
